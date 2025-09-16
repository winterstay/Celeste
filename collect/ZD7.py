import requests

url = "https://stock.cheesefortune.com/api/v2/userSelectStrategy/info/384985"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=utf-8",
    "Host": "stock.cheesefortune.com",
    "Referer": "https://stock.cheesefortune.com/strategy/detail/384802?strategyTab=%E8%B4%A8%E5%9C%B0%E4%BC%B0%E5%80%BC",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
    "deviceType": "pc",
    "requestFrom": "wechat",
    "runtimeType": "browser",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "timeStamp": "1757819156687",
    "token": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1MjM2QSIsInN1YiI6IlhWb0RhZk1DRmFvNDhZTng2b2Vib2RLcGtPc2lWQ3ZKMnREL0FTVkdnOXlTWmNRblpOOGo3WDdoZmJ0L2JFMzJNRG0vOFpFcnFubzNVTWM1Sm9EYW1BYkx3enRwQjFCMzRPQ3ZEK21LT1l0VUdIaEdIZEtOeHBvOC9ZS1ZmZmJnIiwiaWF0IjoxNzU3MTM5Nzk0LCJleHAiOjIwNzI0OTk3OTR9.Adg_cj2VQt7Wja5epNgLBHR1YvfwX0rGtxy3OeQRgps",
    "zstokv1": "74e95ff6815d7750daacab0cec4efd24"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data['datas']['list'])  # 直接打印datas中的list数据
#公司-估值-趋势-带息债务-现金短债比