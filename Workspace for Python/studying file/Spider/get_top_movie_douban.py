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
soup = BeautifulSoup(html, ' html.parser')
# %%
movie_list = soup.find('ol', class_='grid_view')
print(movie_list)
