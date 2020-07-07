# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 30, fill = '|', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


#parsing isn't perfect and some comments can be split 
def commentsFrom(URL): 
    import time
    #selenium can be a bit tricky to install
    from selenium import webdriver
    #soup's pip name is neither "bs4", nor "BeautifulSoup"
    from bs4 import BeautifulSoup

    #initialises webdriver.
    #make sure the PATH leads to your webdriver
    #download it and add to path if you don't have it already
    driver = webdriver.Chrome('c:\\webdrivers\\chromedriver.exe')
    
    #opens chrome with a given URL
    driver.get(str(URL))
    time.sleep(5)
    
    print(' scrolling')
    print("")
    
    #scrolling sycle; it brakes on the bottom or on max range;
    for j in range(1, 7):
        time.sleep(2)
        height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0," +str(10000*j) +");")
        printProgressBar(j, 6)
        time.sleep(2)
        if driver.execute_script("return document.documentElement.scrollHeight") == height:
            print("")
            break

    #gets html
    x = driver.page_source

    #closes chrome
    driver.close()
    
    #this step might not be nessesairy
    x = str(x)
    print("")
    print(" parsing")
    #soup is now a special object we can easily parce
    soup = BeautifulSoup(x)
    
    #getting comments with shit; put a different discriminator to get different stuff
    comments_with_shit = soup.find_all(id="content-text")
    
    #new soup object to remove some shit
    soup = BeautifulSoup(str(comments_with_shit), "html.parser")
    
    #just a function over a list to clean it up from extra shit like "[", ","; 5 is chosen arbitrary
    clearTrash = lambda list: [e for e in list if len(str(e))>5]    
    print(" ready")
    return clearTrash([s for s in soup.strings])