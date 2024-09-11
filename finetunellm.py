import time
import csv
import google.generativeai as genai
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

genai.configure(transport='grpc')
model_names = ['allcode']#防止報錯，建議留一個model以免搞混
for name in model_names:
    try:
        genai.delete_tuned_model(f'tunedModels/{name}')
    except Exception as e:
        print(f"Error deleting model {name}: {e}")


def read_user_code(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def csv_to_list_of_dicts(csv_file):
    data = []
    with open(csv_file, 'r') as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            data.append({'text_input': row['rejected'],
                         'output': row['vulnerability']})
    return data


fine_tuning_data = csv_to_list_of_dicts('pythondata.csv')
for i, m in zip(range(4), genai.list_tuned_models()):
    print(m.name)
my_finetuned_model_name = "allcode" #確認model name沒有重複

# safety_settings=safety_settings,
operation = genai.create_tuned_model(
    source_model='models/gemini-1.0-pro-001',
    training_data=fine_tuning_data,
    id=my_finetuned_model_name,
    epoch_count=15, #少資料集的情況下，建議10~15，目前測的結果最好
    temperature=0.9,
    batch_size=4,
    learning_rate=0.001,
)
model = genai.get_tuned_model(f'tunedModels/{my_finetuned_model_name}')
for status in operation.wait_bar():
    time.sleep(10)
print(model.state)
print(operation.metadata)

model = operation.result(timeout=1000)
snapshots = pd.DataFrame(model.tuning_task.snapshots)
print(sns.lineplot(data=snapshots, x='epoch', y='mean_loss'))

'''看情況加入，這下面只是測試code
model = genai.GenerativeModel(
    model_name=f'tunedModels/{my_finetuned_model_name}')
prompt = '''
    Given the following Python code, identify any potential security vulnerabilities based on OWASP TOP 10 2021, and provide suggestions to fix them.

    Code:

    Vulnerabilities:

    fix code:
    '''
result = model.generate_content(prompt)
print(result.text)
'''
