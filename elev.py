import os.path
from llama_index.core import (
    Settings,
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from llama_index.llms.gemini import Gemini
from llama_index.core.llms import ChatMessage
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
import time
import csv
import google.generativeai as genai
import pandas as pd
import seaborn as sns
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import warnings
warnings.filterwarnings('ignore')
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]

generations = {
    "temperature": 1,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 10000,
}


def detect_and_fix_code(file_path):
    user_code = read_user_code(file_path)

    prompt = f"""

    According to the python code I gave you, output this code to user again!(Because user need to confirm whether the code you see is the same as what the user gave you)\
    According to owasp top 10 2021, check whether there are vulnerabilities in this program. \
    First output(ex: A0x ...) which owasp top 10 2021 attack type it belongs to\
    Top 10:2021 List\
    + A01 Broken Access Control\
    + A02 Cryptographic Failures\
    + A03 Injection\
    + A04 Insecure Design\
    + A05 Security Misconfiguration\
    + A06 Vulnerable and Outdated Components\
    + A07 Identification and Authentication Failures\
    + A08 Software and Data Integrity Failures\
    + A09 Security Logging and Monitoring Failures\
    + A10 Server Side Request Forgery (SSRF)\
    If there are no vulnerabilities, say no. \
    If there are vulnerabilities, point out the vulnerabilities that may be caused. \
    Tell me what type of vulnerability is in owasp top 10 2021.\
    What attacks will be exploited in this code\
    How to write the python code to fix the vulnerability (here refers to the correct way to write the python code, Not just describing code problems, but writing correct code(Output complete code))

    Code to be checked is:
    {user_code}
    Owasp top 10 type:

    Vulnerabilities:

    Fix python code:

    """
    '''
    response = model.generate_content(
        prompt,
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }
    )
    '''
    response = model.generate_content(
        prompt,
        generation_config=generations,
        safety_settings=safety_settings
    )

    return response.text


def read_user_code(file_path):
    with open(file_path, 'r') as file:
        return file.read()


model = genai.GenerativeModel(model_name=f'tunedModels/llmssdlc',
                              generation_config=generations,
                              safety_settings=safety_settings)


def main():
    file_path = input(
        "Enter the path to the Python code file you want to check: ")

    result = detect_and_fix_code(file_path)
    print(result)


if __name__ == "__main__":
    main()
