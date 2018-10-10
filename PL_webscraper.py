from textblob import TextBlob 
import sys
import re
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

pl_url = 'https://www.premierleague.com/players'

# opening connection, grabbinig the page
uClient = uReq(pl_url)
page_html = uClient.read()

uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

players = page_soup.findAll('tr')

filename = 'PremierLeaguePlayers.csv'
f = open(filename,'w')
headers = "Player Name, Player Position, Player Country\n"
f.write(headers)

for player in players[1:]:
	player_name = player.a.text
	player_pos = player.find('td',{"class":"hide-s"}).text
	player_country = player.find('span',{"class":"playerCountry"}).text

	f.write(player_name + "," + player_pos + "," + player_country + "\n")

	print("Player name is " + player_name)
	print("Player position is " + player_pos)
	print("Player country is " + player_country + "\n\n")

f.close()