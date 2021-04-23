import concurrent.futures
import urllib.request
import newspaper
from newspaper import Article

URLs = ['http://www.foxnews.com/',                                                      #the URLs to get the headers from
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'https://theguardian.com',]

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:                          #assigning the time out request to conn
        return conn.read()

def concurrent_URLs_example():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:              #assigning the concurrent thread workers as the executor
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLs}       #loading the URL into the executor
        for future in concurrent.futures.as_completed(future_to_url):                   #for loop of future URLs
            url = future_to_url[future]                                                 #assiging the future URL to the current URL
            try:
                data = future.result()                                                  #assiging the rults to the data
                result = newspaper.build(url, memoize_articles=False)                   #building the results
            except Exception as exc:                                                    #creating an exception
                print('%r generated an exception: %s' % (url, exc))                     #printing the exception
            else:
                print('\n''The headlines from %s are' % url, '\n')                      #printing out the headlines
                for i in range(1,6):                                                    #for loop of the first 5 articles
                    art = result.articles[i]                                            #assigning the arcticle results
                    art.download()                                                      #empty list of downloaded results
                    art.parse()                                                         #empty list of parsed results
                    print(art.title)                                                    #printing the result title
                

def get_headlines():                                                                    
    for url in URLs:                                                                    #for loop of the URLs
        result = newspaper.build(url, memoize_articles=False)                           #building the results
        print('\n''The headlines from %s are' % url, '\n')                              #printing the headlines
        for i in range(1,6):                                                            #for loop of the first 5 articles
            art = result.articles[i]                                                    #assigning the arcticle results
            art.download()                                                              #empty list of downloaded results
            art.parse()                                                                 #empty list of parsed results
            print(art.title)                                                            #printing the result title
        print(art.title)                                                                #printing the result title

if __name__ == '__main__':
    import timeit
    #elapsed_time = timeit.timeit("concurrent_URLs_example()", setup="from __main__ import concurrent_URLs_example", number=2)/2          
    elapsed_time = timeit.timeit("get_headlines()", setup="from __main__ import get_headlines", number=2)/2#the time when using concurrency
    print(elapsed_time)                                                                 #printing the elapsed time