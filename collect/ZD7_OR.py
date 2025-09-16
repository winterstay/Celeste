import requests
import json

url = "https://stock.cheesefortune.com/api/v2/select/select"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=utf-8",
    "Host": "stock.cheesefortune.com",
    "Origin": "https://stock.cheesefortune.com",
    "Referer": "https://stock.cheesefortune.com/strategy/screenerResult?tempId=%C2%ABr1%C2%BB",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
    "deviceType": "pc",
    "requestFrom": "wechat",
    "runtimeType": "browser",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "timeStamp": "1757819683381",
    "token": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1MjM2QSIsInN1YiI6IlhWb0RhZk1DRmFvNDhZTng2b2Vib2RLcGtPc2lWQ3ZKMnREL0FTVkdnOXlTWmNRblpOOGo3WDdoZmJ0L2JFMzJNRG0vOFpFcnFubzNVTWM1Sm9EYW1BYkx3enRwQjFCMzRPQ3ZEK21LT1l0VUdIaEdIZEtOeHBvOC9ZS1ZmZmJnIiwiaWF0IjoxNzU3MTM5Nzk0LCJleHAiOjIwNzI0OTk3OTR9.Adg_cj2VQt7Wja5epNgLBHR1YvfwX0rGtxy3OeQRgps",
    "zstokv1": "ea717b17977473e57cb832094b2ef62b"
}

payload = {
    "seqFlags": ["PLATES","BASIC_ST","SCORE_COMPANY","SCORE_VALUE","SCORE_TREND","DEMINING_INTDEBTTOTOTALCAP","DEMINING_CURRENCYRATIO"],
    "plates": "1,2",
    "basic_st": 1,
    "score_company_left": 7,
    "score_company_right": 10,
    "score_value_left": 0,
    "score_value_right": 10,
    "score_trend_left": 0,
    "score_trend_right": 10,
    "demining_intdebttototalcap_left": 0,
    "demining_intdebttototalcap_right": 30,
    "demining_currencyRatio_left": 1,
    "demining_currencyRatio_right": "Infinity"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())