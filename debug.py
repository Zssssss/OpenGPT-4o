
import json
temp = str({'generated_text': ' I'm sorry to hear that you're feeling sad. Let's try to find some information that might help you feel better. Here's a general query about stress management techniques:```json{  "name": "general_query",  "arguments": {    "prompt": "Can you suggest some effective stress management techniques?"  }}```If you'd like, I can also try to find some inspiring quotes or funny jokes to cheer you up. Just let me know!'})
# 清理字符串
# 移除多余的反斜杠
cleaned_temp = temp.replace("\\", "")
# 将单引号替换为双引号
cleaned_temp = cleaned_temp.replace("\'", "\"")

# 尝试将清理后的字符串转换为字典
try:
    # 由于字符串中包含多余的空格和特殊字符，我们需要进一步清理
    # 移除多余的空格和特殊字符
    cleaned_temp = cleaned_temp.replace(" I'm", "\"I'm").replace("Let's", "\"Let's").replace("Here's", "\"Here's")
    cleaned_temp = cleaned_temp.replace("```json", "").replace("```", "")
    cleaned_temp = cleaned_temp.strip("\"")
    data = json.loads(cleaned_temp)
    print("转换成功，字典内容如下：")
    print(data)
except json.JSONDecodeError as e:
    print("JSON解析错误：", e)
# res = json.loads(temp)