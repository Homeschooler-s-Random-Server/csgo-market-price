#!/usr/bin/env python3.9

import requests

for i in range(0, 3):

	file = open('clone_{}.html'.format(i+1), 'wb')

	page = requests.get('https://steamcommunity.com/market/search?category_730_Type%5B%5D=tag_CSGO_Type_Knife&appid=730#p1_name_asc')

	file.write(page.content)

	file.close()

print('done')
