# import the required libraries
from bs4 import BeautifulSoup
import requests
from requests import Response
# set the target url
url = 'https://theyfightcrime.org/'
# create two lists of two characters
HE = []
SHE = []
# repeat 50 times
for i in range(0, 50):
    # make requests to the website
    response = requests.get(url)
    # parse the html and scrap the content
    content = BeautifulSoup(response.content, "html.parser")
    characters_box = content.find("td")
    characters = characters_box.text.strip()
    # split the content of two characters from the original paragraph
    pure_characters = characters.split("They fight crime!")[0]
    # divide the characters into he_sentence and she_sentence
    He_sentence = pure_characters.split( 'She')[0]
    She_sentence = 'She' + pure_characters.split( 'She')[1]
    # append each result into the lists
    HE.append(str(He_sentence))
    SHE.append(str(She_sentence))
# write the list into two files
with open('HE.txt', mode='wt', encoding='utf-8') as file1:
    file1.write('\n'.join(HE))
with open('SHE.txt', mode='wt', encoding='utf-8') as file2:
    file2.write('\n'.join(SHE))





