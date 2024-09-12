
## Project structure 

![image](https://github.com/user-attachments/assets/4faf920e-cf15-413b-b7b8-a8708921b05f)

The location of the original dataset needs to be preprocessed, otherwise training cannot be performed.

https://huggingface.co/datasets/CyberNative/Code_Vulnerability_Security_DPO/tree/main

You can use our processed csv directly in colab

https://huggingface.co/datasets/nomiaow/badcode/resolve/main/ALL_code.csv

### Preprocessing
+ Convert output.json to generate data.csv. Users can select files for training according to their needs.
+ data.csv is the same csv file as pythondata.csv
+ output.json only contains python data
+ The ALLcodedet folder contains all the code used for data preprocessing

### Register google cloud (no money required, but please follow the steps below and don’t bind your card!!!)

![image](https://github.com/user-attachments/assets/0bd67832-0ba6-4fa1-8ab5-a603b92e212d)


Before training the program, you need to register with Google Cloud and complete the OAuth related settings. If the number of requests exceeds the number, you may need to swipe your card. Please refer to this article for details.
+ First go to google cloud to enable API -> Generative Language API

![image](https://github.com/user-attachments/assets/18be6fa6-ddd4-483e-b64e-c9e1c6401f19)


+ [Quick Start Guide to Authentication with OAuth](https://ai.google.dev/gemini-api/docs/oauth)

After you get the client_secret.json file from OAuth, please go to google cloud cli and execute the following command. Don’t forget that the location of client_secret.json must be in the directory where you downloaded the command, and confirm that your cloud has a list of allowed testers. After following this command, you will need to log in to the tester's account.

+ `gcloud auth application-default login --client-id-file client_secret.json --scopes=https://www.googleapis.com/auth/cloud-platform --scopes=https://www.googleapis.com/auth/generative-language.tuning`

![image](https://github.com/user-attachments/assets/b7af2675-c49d-471a-88de-51649437c28e)


```bash
Credentials saved to file: [/<YOUR_HOME_DIR>/.config/gcloud/application_default_credentials.json]

These credentials will be used by any library that requests Application Default Credentials (ADC).
```
+ Application_default_credentials.json must be generated to run the code normally

### train

Remember to run this command
+ pip install google-generativeai

The main training program is finetunellm.py. During training, please make sure you obtain client_secret.json in OAuth and import our data.csv data set. Please make sure they are all in the same directory.

+ After training, run the elev.py program to enter the code you want to detect. Remember! If you only use data.csv, then finetunellm.py is a program that only trains python and is not written properly! So please only enter xxx.py (Enter the name of the code file to be tested according to the training program)

The running result is as shown in the figure

![image](https://github.com/user-attachments/assets/7af23a6e-a51d-4080-b078-61a71d97a793)

![image](https://github.com/user-attachments/assets/152585e1-b48c-4014-a38d-fcd31a51c86a)


+ data.csv only contains python data sets
+ If you want to train multiple improper programming methods, the data set is placed in the ALLcodedet folder
+ install_mode file will be generated after each training
+ Requirements.txt contains the packages that need to be downloaded. In fact, more or less installation content may be required.
+ The un_sec_code folder contains some examples of incorrect code writing, which can be tested when executing elev.py


### Use the RAG application to instrument your code
1. Please refer to the rag folder and [README.md](./rag/README.md)
2. To run locally, please refer to [Setup](./rag/docs/setup.md)

- Example:

https://github.com/user-attachments/assets/02f93c97-469d-4609-8d2e-efe5cfd07655



### Related reference articles
+ https://ai.google.dev/gemini-api/docs/model-tuning/python
+ https://www.kaggle.com/code/bhavikjikadara/gemini-api-with-python
+ 
### No training required
If you don’t want to train, you can go to google gemini to get the developer API, which is free as long as the requests per minute do not exceed the official limit.
+ [GeminiAPI](https://ai.google.dev/gemini-api?gad_source=1&gclid=Cj0KCQjwsPCyBhD4ARIsAPaaRf0hB9zSvwr530f4nt47I5Vr8wfllZyFwQIqlppBKxtoMRwB7iY9lEgaAoo0EALw_wcB&hl=zh-tw)
+ [Get Gemini API Key](https://aistudio.google.com/app/apikey)
  
After getting the API, use notraintogemini.py directly.

The running results are as follows

https://github.com/user-attachments/assets/323782f8-d4a0-449c-827e-08069f8a7ec6

https://github.com/user-attachments/assets/768c471b-1ac0-4ab1-8c20-dc6281d8a2bd

### Developer
+ Noflag
+ Jimmy Liao

![image](https://github.com/user-attachments/assets/c85edf1c-f8d0-4bc2-8e6a-5792096217d5)

### Become a contributor?
Send a PR to add new features and we will review it!

### Future Work
+ test results
 + web display
 + PDF report
+RAG
+ Ollama
...

### Shared speech

https://hackmd.io/@HWDC/2024/%2FtZ-N1r47RumqlLrggI7LoA


## This unit is not responsible for any expenses incurred. Please keep your magic card safe.
