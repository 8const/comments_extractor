from functions import *
import pandas as pd

DRIVER_PATH = 'c:\\webdrivers\\chromedriver.exe'
URL = "https://www.youtube.com/watch?v=IHNzOHi8sJs"

source = get_page_source(URL, DRIVER_PATH, 30)

data = get_data_from_source(source)
df = pd.DataFrame(data)
df.to_csv("data.csv")

