# %%
from bs4 import BeautifulSoup
import requests

# %%
url = 'https://movie.douban.com/top250'
response = requests.get(url)
print(response)

# %% [markdown]
# there are anti-spider method
#  to solve this, adding user-agent

# %%
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.369'
}
response = requests.get(url, headers=header)
print(response.status_code)
# %%
print(response.text)
# %%
file = open('I:\Programming\Python\python-workspace\Workspace for Python\studying file\Spider\douban_top_250_movies.html', 'w', encoding='utf-8')
file.write(response.text)
file.close
html = response.text

# %%
file = open(r'I:\Programming\Python\python-workspace\Workspace for Python\studying file\Spider\douban_top_250_movies.html', 'r', encoding='utf-8')
html = file.read()
file.close

# %%

# %%
soup = BeautifulSoup(html, 'html.parser')
# %% [markdown]
# ### Find information for each movie
# %%
# attrs = ['class': 'grid_view']
movie_list = soup.find('ol', class_='grid_view')
print(movie_list)


# %%
movies = movie_list.find_all('li')
print(type(movie_list))
movies[0]

# %%
names = []
for movie in movies:
    name = movie.find('span', class_='title').get_text()

print(names)
# %%
for movie in movies:
    urls = movie.find('a', ['href']).get_text()
    print(urls)
# %%
movies

# %%

# %%
# All the pages
url = 'https://movie.douban.com/top250'
while url is not null:
    header = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.369'
    }
    response = requests(url, head=header)
    print(response)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    movie_list = soup.find('ol', class_='gridview')
    movies = movie_list.find_all('li')

    cnames = []
    enames = []
    info = []
    marks = []
    urls = []

    for movie in moives
     names = movie.find_all('span', class_='title')
      cnames.append(names[0].get_text())
       if len(names) > 1:
            enames.append(names[1].get_text())
        else:
            enames.append([])

        inf = movie.find('p').find('pr').get_text()
        info.append(inf)
        url = movie.find('a')['href']
        urls.append(url)
        mark = movie.find('span', class_='rating_num').get_text()
        marks.append(mark)

    with open()


# %%
