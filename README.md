Script main.py extracts comments from youtube and writes them to data.csv. Selenium is
used for opening URLs in browser, scrolling and getting the page source. Beautiful soup is
used for parsing that source.
 
It works quite well for getting less than ~700 comments from a single video.
Unfortunately, with higher quantities YouTube lags and stops loading more comments.
Sometimes it can get as much as 1100.
But we can't recommand expecting 700+ to work every time.
