#parsing isn't perfect and some comments can be split 
def listOfCommentsFrom(URL): 
    import time
    #selenium can be a bit tricky to install
    from selenium import webdriver
    #soup's pip name is neither "bs4", nor "BeautifulSoup"
    from bs4 import BeautifulSoup

    #initialises webdriver.
    #make sure the PATH leads to your webdriver
    #download it and add to path if you don't have it already
    driver = webdriver.Chrome('c:\\webdrivers\\chromedriver.exe')
    
    #opens chrome with given URL
    driver.get(str(URL))
    time.sleep(10)
    
    #gets page's height that will be used for scrolling
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    time.sleep(3)
    
    #scrolling sycle; it brakes on the bottom
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    #wait to load page
        time.sleep(5)

    #calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    #gets html
    x = driver.page_source

    #closes chrome
    driver.close()
    
    #this step might not be nessesairy
    x = str(x)
    
    #soup is now a special object we can easily parce
    soup = BeautifulSoup(x)
    
    #getting comments with shit; put a different discriminator to get different stuff
    comments_with_shit = soup.find_all(id="content-text")
    
    #new soup object to remove some shit
    soup = BeautifulSoup(str(comments_with_shit), "html.parser")
    
    #just a function over a list to clean it up from extra shit like "[", ","; 5 is chosen arbitrary
    clearTrash = lambda list: [e for e in list if len(str(e))>5]    

    return clearTrash([s for s in soup.strings])