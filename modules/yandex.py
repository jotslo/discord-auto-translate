import json, requests

url = "https://translate.yandex.net/api/v1.5/tr.json/translate"

def translate(message, api_key):
    # request translation from [detect] -> english
    data = {"key": api_key, "text": message, "lang": "en"}
    response = json.loads(requests.post(url, data=data).text)

    # check whether successful & return translation
    if response["code"] == 200:
        return response["text"][0]
    else:
        return message