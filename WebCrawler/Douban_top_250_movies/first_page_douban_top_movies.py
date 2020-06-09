# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import requests
from bs4 import BeautifulSoup

# %%
url = 'https://movie.douban.com/top250'
response = requests.get(url)
print(response)

# %% [markdown]
#  there are anti-spider method
#   to solve this, adding user-agent

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
file = open('I:\Programming\Python\python-workspace\Workspace for Python\studying file\Spider\douban_top_250_movies.html', 'r', encoding='utf-8')

html = file.read()
file.close

# %%
soup = BeautifulSoup(html, 'html.parser')


# %%
# attrs = ['class': 'grid_view']
movie_list = soup.find('ol', class_='grid_view')
print(movie_list)

# %% [markdown]
#  ### Find information for each movie

# %%
movies = movie_list.find_all('li')
print(type(movie_list))

# %%
for movie in movies:
    info = movie.find('p')
    info_text = (info.get_text()).split('\n')
    print('1')
    print(info_text[0])
    print('\n2')
    print(info_text[1])
    print('\n3')
    print(info_text[2])
    print('\n')

# %%
names = []

for movie in movies:
    name = movie.find('span', class_='title').get_text()
    names.append(name)

print(names)


# %%
e_names = []
c_names = []

for movie in movies:
    name = movie.find_all('span', class_='title')
    for n in name:
        print(n.get_text)

    e_names.append(name[0].get_text())
    e_names.append(name[1].get_text())

print(e_names)
print(c_names)


# %%
e_names = []
c_names = []

for movie in movies:
    name = movie.find_all('span', class_='title')

    print(name[0].get_text())
    c_names.append(name[0].get_text())
    if len(name) > 1:
        e_names.append(name[1].get_text())
    else:
        e_names.append('')

print(e_names)
print(c_names)


# %%
urls = []
for movie in movies:
    url = movie.find('a')['href']
    urls.append(url)

print(urls)

# %% [markdown]
# ### Save the file

# %%
with open('movies.csv', 'w', encoding='utf-8')as f:
    for i in range(len(urls)):
        f.write(c_names[i]+','+e_names[i]+','+urls[i]+'\n')
