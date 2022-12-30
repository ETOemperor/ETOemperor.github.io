import requests
import time
import random
ua={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
}
ip={
    "http":"http://127.0.0.1:500"
    "https""https://127.0.0.1:500"
}
a=0
while a!=100:
    for i in range(random.randint(3243, 5656)):
        resp=requests.get("https://1ac50418.r8.cpolar.top",headers=ua,proxies=ip)
        print(resp)
        resp.close()
    a=random.ranint(1,50)