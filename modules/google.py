import json, requests

url = "https://translation.googleapis.com/language/translate/v2"

def translate(message, api_key):
    # request translation from [detect] -> english
    data = {"key": api_key, "q": message, "target": "en"}
    response = json.loads(requests.post(url, data=data).text)

    # check whether successful & return translation
    if response["code"] == 200:
        return response["data"]["translations"][0]["translatedText"]
    else:
        return message