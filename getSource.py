def getSource(URL)
    import time
    from selenium import webdriver
    from bs4 import BeautifulSoup
    driver = webdriver.Chrome('c:\\webdrivers\\chromedriver.exe')
    driver.get(URL)
    time.sleep(5)
    print(' scrolling')
    print("")
    for j in range(1, 7):
        time.sleep(2)
        height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0," +str(10000*j) +");")
        printProgressBar(j, 6)
        time.sleep(2)
        if driver.execute_script("return document.documentElement.scrollHeight") == height:
            print("")
            break
    return driver.page_source
