import requests

url = 'https://reqbin.com/echo/post/json'

#myheaders = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36", "Content-Type": "application/json"}

myheaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36" , "Content-Type": "application/json"}

myobj = {'Id': '12345', 'Customer': 'John Smith', 'Quantity': 1, 'Price': 10.00}

r = requests.post(url, json=myobj, headers=myheaders)

print(r)          # <Response [200]>

print(r.text)     # {"success":"true"}
                  #

print(r.json())   # {'success': 'true'}
