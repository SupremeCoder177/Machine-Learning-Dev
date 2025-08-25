# utility class for all download scripts in this folder

import requests
import threading
from time import sleep


class Animation:

	def download_anim(self):
		frames = ['|', '\\', '-', '|', '/']
		for i in range(len(frames)):
			print(f"\rDownloading...{frames[i]}", end="")
			sleep(0.1)
		

class Util:

	def __init__(self):
		self.data = {}

	def check_connection(self) -> bool:
		try:
			requests.get("https://www.google.com")
			return True
		except requests.ConnectionError as e:
			return False

	def clear_search_string(self, search):
		return "+".join(search.split(' '))

	def download(self, url):
		thread = threading.Thread(target = self.start_download, args = [url])
		thread.start()
		while thread.is_alive():
			Animation().download_anim()
		print()
		return self.data

	def start_download(self, url):
		res = requests.get(url)
		context_type = res.headers.get("Context-Type", "")
		
		if "application/json" in context_type:
			self.data = res.json()
		else:
			res.encoding = 'utf-8'
			self.data = res.text

