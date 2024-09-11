import warnings
# import pathlib
# import textwrap
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
# from IPython.display import display, Markdown
# import json


# if in Colab, use Markdown from IPython.display
# if in Jupyter Notebook, use Markdown from IPython.display
# def to_markdown(text):
#     if isinstance(text, str):
#         text = text.replace('•', '*')
#         return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
#     else:
#         return Markdown(text)


warnings.filterwarnings("ignore")

# 記得更新api key
genai.configure(
    api_key="AIzaSy..."
)

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash'
)


def detect_and_fix_code(code):
    prompt = f"""
    Given the following Python code, identify any potential security vulnerabilities based on OWASP TOP 10 2021, and provide suggestions to fix them.

    Code:
    {code}

    Vulnerabilities:
    """
    response = model.generate_content(
        prompt,
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }
    )

    if response.candidates and response.candidates[0].content:
        return response.text
    else:
        print("Response parts:", response.parts)
        if response.candidates:
            print("Safety ratings:", response.text.safety_ratings, end='\n')
            print("Finish reason:", response.text.finish_reason, end='\n')
        return "Unable to detect vulnerabilities. Please try again later."


def read_user_code(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def main():
    file_path = input(
        "Enter the path to the Python code file you want to check: ")
    user_code = read_user_code(file_path)

    result = detect_and_fix_code(user_code)

    if isinstance(result, str):
        print(result)
    else:
        print(result)


if __name__ == "__main__":
    main()
# app.py
