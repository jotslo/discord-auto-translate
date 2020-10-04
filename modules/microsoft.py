import json, requests, pdb

url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=en"

def translate(message, api_key):
    # request translation from [detect] -> english
    data = [{"Text": message}]
    headers = {"Ocp-Apim-Subscription-Key": api_key, "Content-Type": "application/json"}
    response = requests.post(url, data=str(data), headers=headers)
    
    # check whether successful & return translation
    if response.status_code == 200:
        return json.loads(response.text)[0]["translations"][0]["text"]
    else:
        return message
