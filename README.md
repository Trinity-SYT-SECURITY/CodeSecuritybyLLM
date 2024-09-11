原數據集位置，需經預處理，不然無法進行訓練

https://huggingface.co/datasets/CyberNative/Code_Vulnerability_Security_DPO/tree/main

### 預處理
+ 從 output.json 轉換產生 data.csv，使用者可以根據需求去選擇檔案進行訓練
+ data.csv 跟 pythondata.csv 是一樣的csv檔案
+ output.json 只包含 python 的數據
+ ALLcodedet 資料夾下包含了所有用來進行資料預處理的程式碼

### 註冊 google cloud (不用錢，但請遵照以下方法，不要綁卡!!!)

![gcloud](https://github.com/user-attachments/assets/9b79fc04-0c99-465f-b921-c3dc78ad286a)


訓練該程式前需要先註冊好 google cloud 並將 OAuth 相關設定搞定，超過請求數有可能你需要刷卡，詳情請參考這篇文章
+ 先到google cloud啟用API -> Generative Language API

![image](https://github.com/user-attachments/assets/e0745c09-eb8f-423d-a2ce-a7d00c9629cc)

+ [透過 OAuth 進行驗證的快速入門導覽課程](https://ai.google.dev/gemini-api/docs/oauth)

當你從 OAuth 拿到 client_secret.json 的檔案後，請到 google cloud cli 去下這下面指令，不要忘記 client_secret.json 的位置要在下指令的目錄中，並確認你的 cloud 有允許的測試人員名單，在該指令下後會需要登入到該測試人員的帳號
+ `gcloud auth application-default login --client-id-file client_secret.json --scopes=https://www.googleapis.com/auth/cloud-platform --scopes=https://www.googleapis.com/auth/generative-language.tuning`

![image](https://github.com/Trinity-SYT-SECURITY/LLM-PYSec/assets/96654161/24d3be84-dc33-43fd-a7e2-c9f5839d6432)

![image](https://github.com/Trinity-SYT-SECURITY/LLM-PYSec/assets/96654161/49f95989-fb74-4a2c-aa9d-cee619506a06)

```bash
Credentials saved to file: [/<YOUR_HOME_DIR>/.config/gcloud/application_default_credentials.json]

These credentials will be used by any library that requests Application Default Credentials (ADC).
```
+ 有產生 application_default_credentials.json 才能正常運行程式碼

### 訓練

記得運行該指令
+ pip install google-generativeai

主要訓練程式為 finetunellm.py，訓練時請確保你在OAuth中有取得 client_secret.json，並將我們的 data.csv 資料集匯入，請確認都在同個目錄底下 

+ 訓練後運行 elev.py 的程式去將你想要檢測的程式碼輸入進去，記住! 如果只使用 data.csv，那麼 finetunellm.py 這程式僅訓練 python 不當寫法! 所以請只輸入 xxx.py (根據訓練程式去輸入要檢測的程式碼檔案名稱)

運行結果如圖

![image](https://github.com/Trinity-SYT-SECURITY/LLM-PYSec/assets/96654161/070358ea-910c-4023-b971-94d0146b212a)

![image](https://github.com/Trinity-SYT-SECURITY/LLM-PYSec/assets/96654161/bb430650-dc3c-45da-a496-dae9e4845fa3)

+ data.csv 只包含 python 的資料集
+ 若想訓練多個不當程式寫法，該資料集放在 ALLcodedet 資料夾下
+ install_mode 檔案在每次訓練後會產出
+ requirements.txt 內是需要下載的套件，實際可能需要更多或更少安裝內容
+ un_sec_code 的資料夾下包含了一些範例的不正確程式碼寫法，可以在執行 elev.py 時進行測試


### 使用 RAG 應用程式檢測程式碼
1. 請參考 rag 資料夾以及 [README.md](./rag/README.md)
2. 本地端運行，請參考 [Setup](./rag/docs/setup.md)

- 範例:
![](./rag/demo.gif)


### 相關參考文章
+ https://ai.google.dev/gemini-api/docs/model-tuning/python
+ https://www.kaggle.com/code/bhavikjikadara/gemini-api-with-python

### 不用訓練
如果不想訓練，可以到 google gemini 去取得開發人員 API，在每分鐘請求不超過官方限制的情況下是免費的
+ [GeminiAPI](https://ai.google.dev/gemini-api?gad_source=1&gclid=Cj0KCQjwsPCyBhD4ARIsAPaaRf0hB9zSvwr530f4nt47I5Vr8wfllZyFwQIqlppBKxtoMRwB7iY9lEgaAoo0EALw_wcB&hl=zh-tw)
+ [Get Gemini API Key](https://aistudio.google.com/app/apikey)

取得到 API 後直接使用 notraintogemini.py

運行結果如下

https://github.com/Trinity-SYT-SECURITY/LLM-PYSec/assets/96654161/b4df42e0-bb4c-4643-8853-62117a8ff396

### 開發人員
+ Noflag
+ Jimmy Liao

### 成為貢獻者?
發送PR新增功能，我們這會進行審核!

### Future Work
+ 檢測結果
  + 網頁顯示
  + PDF 報告
+ RAG
+ Ollama
...


## 若產生任何的費用，本單位不負責，請保管好你的魔法小卡
