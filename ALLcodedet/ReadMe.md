### 這邊是多程式進行訓練的數據

不過如果數據量太大會遇到這問題，很大機率是因為你的資料量超過了 gemini 免費處理數據的額度

![image](https://github.com/Trinity-SYT-SECURITY/LLM-CodeSec/assets/96654161/369afc00-c695-41d7-8b30-1024dc75efd2)

+ delcsv.py 可以幫你刪減過多的csv數據，不過使用時請小心XD
+ ALL_codedel.csv 是可以進行訓練的數據內容，如果使用ALL_code.csv會超過免費額度，你可能要付費去請求更大的處理數據量~
+ secure_programming_out.json 是處理好的json數據集，它轉成了ALL_code.csv進行訓練
+ secure_programming_dpo.json 直接匯入會無法訓練，未經處理的原始數據
+ pythondata.csv 只包含 python 數據
