# %%
import requests
from bs4 import BeautifulSoup
import time

# %%
# All the pages
url_ = 'https://movie.douban.com/top250'
url0 = url_
# %%
while url_ is not None and url_ is not '':
    # %%
    time.sleep(0.5)
    header = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.369'
    }
    response = requests.get(url_, headers=header)
    print(response)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    movie_list = soup.find('ol', class_='grid_view')
    movies = movie_list.find_all('li')

# %%
    cnames = []
    enames = []
    infos = []
    marks = []
    urls = []
    for movie in movies:
        names = movie.find_all('span', class_='title')
        cnames.append(names[0].get_text())
        if len(names) > 1:
            enames.append(names[1].get_text())
        else:
            enames.append('')

        info = (movie.find('p').get_text()).replace('\n', ',')
        infos.append(info)

        url = movie.find('a')['href']
        urls.append(url)
        mark = movie.find('span', class_='rating_num').get_text()
        marks.append(mark)

# # %%
# for ename in enames:
#     print(ename)
#     print(type(ename))
# %%
    with open("top_movies.csv", 'a', encoding='utf-8') as f:
        for i in range(len(cnames)):
            print(i)
            try:
                line = cnames[i] + ','
            except IndexError:
                print('Indexerror1')
                line += ','
            try:
                line = line + enames[i] + ','
            except:
                print('Error2')
                line += ','

            try:
                line += infos[i] + ','
            except IndexError:
                print('IndexError3')
                line += ','
            try:
                line += marks[i]+','
            except IndexError:
                print('IndexError4')
                line += ','
            try:
                line += urls[i] + '\n'
            except:
                print('IndexError5')
                line = '\n'

            f.write(line)
    try:
        Next = soup.find('span', class_='next')
        urle = Next.find('link', rel='next')['href']
        url_ = url0 + urle
    except:
        print("NoneUrlError")
        print(url_)
        url_ = None


# %%
