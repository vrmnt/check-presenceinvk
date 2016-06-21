#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import bs4
import requests
from sys import argv
from settings import base_url
from settings import response


class User():
	burl = base_url['vk']

	def __init__(self, id=''):
		self.id = id

	def get_status(self):
		print('Проверяю на наличие соединения...')
		if(self._check_connecting()):
			print('Верифицирую...')
			if(self._verify_id(self.id)):
				print("----------------------------OK")
				print('Получаю html...')
				html = self._get_html(User.burl + self.id)
				print("----------------------------OK")
				print('Парсю...')
				status = self._parse(html)
				print("----------------------------OK")
				return status
			else:
				return response['100']
		else:
			return response['110']

	def _check_connecting(self):
		try:
			requests.get('https://new.vk.com/', timeout=5)
		except requests.exceptions.ConnectionError:
			return False
		else:
			return True	

	def _verify_id(self, id):
		if((id == '0') or (id == '') or (id.isdigit() == False)):
			return False
		else:
			return True

	def _get_html(self, url):
		ihtml = requests.get(url)
		return ihtml.content

	def _parse(self, ihtml):
		soup = bs4.BeautifulSoup(ihtml)

		online_status = soup.find('div', {'id': 'profile_online_lv'})
		offline_status = soup.find('div', {'id': 'profile_time_lv'})
		check_stat = soup.find('div', 'page_current_info')

		if(online_status != None):
			# online or offline or absence
			try:
				offline_status.b.decompose()
			except AttributeError:
				pass
			
			if(offline_status == None):
				# Online
				return online_status.contents[0]
			elif(offline_status.string == None):
				# Absence
				return response['520']
			else:
				# Offline
				return offline_status.string
		elif((online_status == None) and (offline_status == None) and (check_stat != None)):
			# Deleted or hidden
			return check_stat.string
		else:
			# not exist
			return response['530']

if __name__ == '__main__':
	if(len(argv) > 1):
		id = argv[1]
	else:
		id = input()
	user = User(id)
	print(user.get_status())