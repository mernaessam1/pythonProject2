'''
scraping in parsehub:showtimes
to find movie_title', 'show_time', 'information_url'
'''
import requests
import bs4
import pandas as pd
#بنخزن فيه الصفحه بتاعتنا
url="https://parsehub.com/sandbox/showtimes"
result = requests.get(url)
sourse=result.content
#print(sourse)
soup =bs4.BeautifulSoup(sourse,"html.parser")
#print(soup)
titles = []
urls = []
time = []
# a find link tages
#The movie title and information URL
page=0
for i in range(1 , 8):
    page=page+i
    url = "https://parsehub.com/sandbox/showtimes"
    url = url + str(page)

    movie_title = soup.find_all('a', {'class': 'title'})  # <a> HTML tags, which has the class name of title.
    information_url = soup.find_all('a', {'class': 'title'})
    show_time = soup.find_all('span', 'imax')  # span> tag with a class name of imax.
    for movie in range(len(movie_title)):
        titles.append(movie_title[movie].string)

    # print(titles)
    for movie in range(len(show_time)):
        time.append(show_time[movie].string)
    # print(time)
    for movie in range(len(information_url)):
        urls.append(information_url[movie].get('href'))
    # print(urls)

    raw_data = {
        'movie_title': titles,
        'show_time': time,
        'information_url': urls
    }

    dataframe = pd.DataFrame(raw_data, columns=['movie_title', 'show_time', 'information_url'])

    # for show all the colum and row by side
    #pd.set_option('display.expand_frame_repr', False)
#for print all the value in the datagram :
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)


print(dataframe)

