from search_youtube_functions import *
from video_page_functions import *
import pandas as pd
import sys

DRIVER_PATH = 'c:\\webdrivers\\chromedriver.exe'
QUERY = sys.argv[1]
LEN = int(sys.argv[2])
urls = fresh_videos_from_query(QUERY)
data = [['Constantine', 'is awesome', 'https://github.com/ConstantineLarionoff/comments_extractor/tree/master']]
data = pd.DataFrame(data, columns = ['name', 'comment', 'link']) 

i = 1

for link in urls[0:LEN]:
    print("Link #", i, "out of ", LEN)
    i += 1
    new_data = get_data_from_source(get_page_source(link,DRIVER_PATH, 10)) 
    new_data = pd.DataFrame(new_data, columns = ['name', 'comment', 'link'])
    data = data.append(new_data)

data.to_csv("data.csv")
print("End")

