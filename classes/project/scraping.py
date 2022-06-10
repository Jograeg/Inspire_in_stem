import imp
import requests
from bs4 import BeautifulSoup as bs

user_name = "Jograeg"# input("#Enter your user name")
url = "https://github.com/"+user_name #input("Enter site Url")
results = requests.get(url)

soup = bs(results.content, "html.parser")
profile_pic = soup.find('img',{'alt':'Avatar'}) ['src']
print(profile_pic)
