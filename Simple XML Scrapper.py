from bs4 import BeautifulSoup
import requests
import ctypes
import os
import sys

#-----------getting data from user-----------#
xml_file = str(input("Enter the XML file link: ")) #sample: https://victoriousseo.com/post-sitemap.xml
number_of_scrapped_articles = int(input("Enter the articles: "))
saving_path = str(input("Enter the saving path: ")) 

#-----------parsing the xml file & getting the links in 'loc' tag-----------#
req = requests.get(xml_file)
soup = BeautifulSoup(req.text, 'lxml')
article_link = soup.find_all('loc')

#-----------looping over links and saving them (+the content) in files-----------#
for i in range(number_of_scrapped_articles):
    
    #replacing tags with space to clean the output
    clean_link = str(article_link[i+1]).replace('</loc>', '').replace('<loc>', '')

    #saving links to file
    with open (saving_path + '\links.txt', mode = 'a', encoding = 'utf-8') as links_file:
        links_file.write(clean_link + '\n')

    #getting content and saving it to file
    for piece_of_text in BeautifulSoup(requests.get(clean_link).content, 'lxml').body.strings:
        with open (saving_path + '\content.txt', mode = 'a', encoding = 'utf-8') as content_file:
            content_file.write(piece_of_text + '\n')

    #stating the end of a single scrap before the loop continues
    with open (saving_path + '\content.txt', mode = 'a', encoding = 'utf-8') as content_file:
        content_file.write('\n' + '-----------end of this article-----------' + '\n')

#-----------simple saving validation-----------#
links_file_validation = os.path.exists(saving_path + '\links.txt')
content_file_validation = os.path.exists(saving_path + '\content.txt')
if links_file_validation and content_file_validation == True:
    print(ctypes.windll.user32.MessageBoxW(0, 'Your files has been marvelously saved, program will exit now', "Success!"))
if links_file_validation == False:
    ctypes.windll.user32.MessageBoxW(0, 'A problem has occured with the links file, program will exit now', "Warning!")
if content_file_validation == False:
    ctypes.windll.user32.MessageBoxW(0, 'A problem has occured with the content file, program will exit now', "Warning!")

#exiting the program in case the code got stuck for some reason here
sys.exit()
