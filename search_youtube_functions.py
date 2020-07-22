import requests
search_result = lambda string: requests.get("https://www.youtube.com/results?search_query="+string+"&sp=CAMSBAgCEAE%253D").text

def URLs_from_search_result(source):
    
    '''returns list of video URLs that are on the source of a YouTube search results page:
    URLs_from_search_result(string) --> list'''
    
    indexes_of_URLs = [i for i in range(len(source)) if source.startswith('{"url":"/watch?', i)]
    return ['https://youtube.com/' + source[j+9 : j+28] for j in indexes_of_URLs]

def fresh_videos_from_query(query):
    
    '''returns list of YouTube video URLs from a particular search query:
       fresh_videos_from_query(string) --> list'''
    
    return URLs_from_search_result(search_result(query))

