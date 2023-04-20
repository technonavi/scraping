from bs4 import BeautifulSoup
import requests
import re
import csv
souphiduke=[]
soupnews=[]
souphref=[]
def sitesearch():
 url = 'https://www.nhs.co.jp/company/pressrelease/'
 html = requests.get(url)
 soup = BeautifulSoup(html.content, 'html.parser')
 return soup
def sitescraping(sitesoup):
 souplist=sitesoup.find_all("dl")
 soupdd =souplist[0].find_all("dd")
 soupdt =souplist[0].find_all("dt")
 for countdd in range(len(soupdd)):
  soupnewstextformer=soupdd[countdd].text
  soupnewstextre=strip(soupnewstextformer)
  
  souphiduketextformer=soupdt[countdd].text
  souphiduketextre=strip(souphiduketextformer)
  
  soupnews.insert(countdd,soupnewstextre)
  souphiduke.insert(countdd,souphiduketextre)

def strip(soupformer):
 souptextre=soupformer.replace("\n","")
 return(souptextre)
def writecsv():
 with open("scrapingnittetu.csv", "w", newline="") as file:
  writer = csv.writer(file)
  csvwrite=[["日付","ニュース内容"]]
  for count in range(len(souphiduke)):
   csvwrite2=[]
   csvwrite2.insert(0,souphiduke[count])
   csvwrite2.insert(1,soupnews[count])
   csvwrite.append(csvwrite2)
  writer.writerows(csvwrite)
  print(souphiduke)
  print(soupnews)
sitesoup=sitesearch()
sitescraping(sitesoup)
writecsv()
