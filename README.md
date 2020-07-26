About:
 
    Script main.py does a YouTube search. 
    Then it extracts vectors (username, comment, link) and writes them to data.csv for each comment under each video of search results.

Environment setup:

    1. Install libraries that you do not have yet with:

                           $pip install beautifulsoup4 
                           $pip install selenium
                           $pip install requests
                           $pip install pandas

    2. Get chromedriver for your system from https://chromedriver.chromium.org/
       (if os == Windows put it in c:\\webdrivers\\chromedriver.exe and skip next step)
        Unfortunately WSL users should use Windows here since environment has to have GUI Chrome

    3. Edit DRIVER_PATH in main.py such that it contains true path to your webdriver.


How to run in shell:

    $./main.py "SEARCH_QUERY" "N" (on UN*X)
    main.py "SEARCH_QUERY" "N" (on Windows)

    SEARCH_QUERY is what YouTube will display resuts for
    Comments are extracted from first N videos with filters: today, sort by view count.


Modifications:

    Edit search_youtube_functions.py to change those filters.
    Edit video_page_functions.py to change number of scrolls on each video's page.

 
It works quite well for getting less than ~700 comments from a single video.
Unfortunately, with higher quantities YouTube lags and stops loading more comments.
Sometimes it can get as much as 1100.
But we can't recommand expecting 700+ to work every time.

