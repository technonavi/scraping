from bs4 import BeautifulSoup
from urllib import request
import re

response = request.urlopen('https://www.fukoku-rubber.co.jp/company/outline.html')
soup = BeautifulSoup(response)
s = soup.text
soup_text = soup.get_text(strip=True)

response.close()

sougyou_front= re.findall('創.*日',soup_text)
try:
 sougyou_limit = sougyou_front[0][0:30]
 sougyou_back = re.findall('創.*日',sougyou_limit)
except:
 sougyou_back = sougyou_front
sougyou_answer =  sougyou_back[0][2:]
print(sougyou_back)
print(sougyou_answer)

