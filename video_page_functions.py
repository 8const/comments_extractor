from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Prints iterations progress
def progress_bar(iteration, total, prefix = '', suffix = '', decimals = 1,
        length = 30, fill = '|', print_end = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = print_end)
    if iteration == total: 
        print()
 

def get_page_source(URL, DRIVER_PATH, n):

    '''returns source of scrolled page with comments loaded
    n is number of scrolls
    DRIVER_PATH is a string with path to chromedriver'''
 
    driver = webdriver.Chrome(DRIVER_PATH)
    print(" started webdriver")
    driver.get(URL)
    print(" sleeping 5s")
    time.sleep(5)
    print(' scrolling')
    print("")
    for j in range(1, n+1):
        driver.execute_script("window.scrollTo(0," +str(30000*j) +");")
        progress_bar(j, n)
        time.sleep(0.5)

        
    source = driver.page_source
    print("")
    print(" got the source") 
    driver.close()
    print(" driver closed")
    return source 

  
def get_URL_from_HTML(s):

    '''just a small function to parse html
       takes string, searches for href="
       returns youtube.com/ + link after href'''
    
    link = 'youtube.com/'

    i = s.find('href="') + 6
    while s[i+1] != '"':
        i+=1
        link = link + s[i]
    return(link)


def get_channel_URL(source, name):

    '''finds channel URL in source given name'''

    n = source.find(name)
    soup = BeautifulSoup(source[n-200: n+50], features="html.parser")
    for s in soup.find_all(id="author-text"):
        if name in str(s):
            block = str(s)
    return get_URL_from_HTML(block)


def get_data_from_source(source):

    '''takes youtube video page source
       returns list of lists of name, comment, channel_URL'''
 
    print(" extracting data from source")
    print("")
    soup = BeautifulSoup(source, features="html.parser")
    text = list(soup.stripped_strings)
    data = []
    for i in range(0, len(text)):
        progress_bar(i, len(text)-1)

        if "•" in text[i]:
            name = text[i-2]
            j = i
            try:
                while not "Show less" in text[j]:
                    if not "•" in text[j]:
                        pass
                        comment = text[j]
                    j+=1
                data.append([name, comment, get_channel_URL(source, name)])
            except:
                pass
    print("")
    print(" finished extracting data")
    return data 
