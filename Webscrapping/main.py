import requests
from bs4 import BeautifulSoup as bs

#taking username input
user = input('Input Github Username: ')
url = 'https://github.com/' + user
req = requests.get(url)
#finding content in form of html
soup = bs(req.content,'html.parser')
#searching the tag
pic = soup.find('img',{'alt':'Avatar'})['src']
#printing the link for the picture
print(pic)