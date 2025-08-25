# this script accesses the gutenburg api to download the book in json format and store it into the Books folder

import requests
from sys import exit
from utils import Util

u = Util()
if not u.check_connection():
	print("Connect to the internet first !")
	exit()

BASE_URL = "https://gutendex.com/books"
SAVE_DIRECTORY = "F:\\Machine Learning\\Datasets\\Books"

print("Welcome........")
while True:
	print("Enter the name of a book to download it, or enter EXIT (all caps) to end program")
	name = str(input(">"))

	if name == "EXIT":
		break

	try:
		res = requests.get(f'{BASE_URL}?search={u.clear_search_string(name)}')
		if res.status_code == 200:
			data = res.json()
			if not data["results"]:
				print("No such book was found by the API")
			else:
				download_url = data["results"][0]["formats"]['text/plain; charset=us-ascii']
				u.download(download_url)
				with open(f'{SAVE_DIRECTORY}/{name}.txt', "a") as book:
					for ch in u.data:
						try:
							book.write(ch)
						except Exception as e:
							continue
	except Exception as e:
		print("An error has occured: ", e)


	
