# refer to https://ithelp.ithome.com.tw/articles/10220161

import requests

def main():
	response = requests.get('https://httpbin.org/ip')

	print("show response.text")
	print(response.text)
	print("\n")

	print("show reponse.encoding")
	print(response.encoding)
	print("\n")

	print("show reponse.status_code")
	print(response.status_code)
	print("\n")

	print("show reponse.headers")
	print(response.headers)
	print("\n")

	print("show reponse.headers Content-Type")
	print(response.headers['Content-Type'])
	print("\n")

	print("show reponse json data")
	print(response.json()['origin'])
	print("\n")

main()

'''
$ python3 request_ex1.py
show response.text
{
  "origin": "1.162.184.158"
}



show reponse.encoding
utf-8


show reponse.status_code
200


show reponse.headers
{'Date': 'Fri, 26 Aug 2022 17:03:36 GMT', 'Content-Type': 'application/json', 'Content-Length': '32', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}


show reponse.headers Content-Type
application/json


show reponse json data
1.162.184.158
'''
