import requests

url = "https://no-more-waiting-4-lunch-atest20061206.replit.app/update_right/"

while True:
	count = input("Please enter count: ")
	print("You entered:", count)
	try:
		payload = url + f"{count}/{count*12}/YaoyutongaiWangjiayuan"
		response = requests.post(payload)
	except Exception as e:
		print(e)