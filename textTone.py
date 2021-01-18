import requests

def getResponse(text):
    headers={
        "x-rapidapi-key": "b34786e198mshac69d114b56dcd0p1a76aejsn1778692afa01",
        "x-rapidapi-host": "twinword-language-scoring.p.rapidapi.com",
        "useQueryString": "true"
    }
    data={
        "text": text
    }
    response = requests.get("https://twinword-language-scoring.p.rapidapi.com/text/", headers=headers, params=data)
    return response.json()