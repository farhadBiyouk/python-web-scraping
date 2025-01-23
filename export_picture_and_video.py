from bs4 import BeautifulSoup
import requests
import re
import random


def download(url):
	"""
	this method use download video and image
	"""
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	links = soup.select_one(
		'html body section.mainbody main div#page.inner-video div.container div.row div.col-12.col-lg-9 div.row div.col-12 div.video-all-dtl div.video-info div.video-actions div.action-vr.dlbtn div.dropdown-menu a.dropdown-item')
	link = links['href']
	with requests.get(link, stream=True) as req:
		with open('video1.mp4', 'wb') as f:
			for video in req.iter_content(chunk_size=1024):
				f.write(video)
	
	print('done!')


download('url')
