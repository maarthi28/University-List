import requests
from bs4 import *
code={'andhra pradesh':'andhra',
      'jharkhand':'jharkhad',
      'pondicherry':'pondichery',
      'uttar pradesh':'utta pradesh',
      'mizoram':'mizorm'}
class University:
    def __init__(self):
        print("---------------------------------WELCOME------------------------------")
    def find(self,place):
        if place=='andhra pradesh' or place=='jharkhand' or place=='pondicherry' or place=='uttar pradesh' or place=='mizoram':
            place=code[place]
        place=place.replace(' ','-')
        url="http://www.learntechww.com/govn-" +place +".html"
        try:
            data=requests.get(url)
            soup=BeautifulSoup(data.text,"html.parser")
            data1=soup.find('div',{'class':'innerpage'})
            data2=data1.find_all('li')
            for i in data2:
                print("\n* "+i.get_text())
        except:
            print("OOPS!!!NOT FOUND...")

u=University()
choice='y'
while choice=='y':
    place=input("\nEnter the State to list Government Universities : ").lower()
    u.find(place)
    choice=input("\nEnter 'Y' to continue, 'N' to quit  : ").lower()
print("\nTHANK YOU !!!")    

