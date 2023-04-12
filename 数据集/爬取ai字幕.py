import requests
import json

url = "https://www.bilibili.com/video/BV1TW411n7T1/?p="
page = "3"
url_num = url + page

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Content-Type": "application/json"

}

param = {
    "auth_key": "1681287550-bb6f48732a254394a91baac41e1ec26f-0-defcb128e78bd5440fbeacc1f2e73a54"

}

response = requests.get(url = url, params=param, headers=headers)
list_data = response.json()

fp = open("./test01.json", mode='w', encoding = 'utf-8')
json.dump( obj = list_data, fp=fp, ensure_ascii = False, indent=4, sort_keys=True)
print("Success! ")