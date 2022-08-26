import requests

def main():
	response = requests.get('https://httpbin.org/ip')
	print('my ip is {0}'.format(response.json()['origin']))

main()

# Result:
# $ python3 ip_by_httpbin.py
# my ip is 1.162.184.151
