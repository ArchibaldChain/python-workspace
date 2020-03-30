# %% [markdown]
# Four step of spider
# - Request
# - Response
# - site anslysis
# > re BeautifulSoup, pyquery, lxml
# - save data
# %%
import driver
from selenium import webdriver
import requests
# %%
url = 'https://www.baidu.com'

# urllib,requests
response = requests.get(url)
response.encoding = 'utf8'
print(response.text)
print(response.status_code)

# %%
print(response.headers)
# %% [Markdown]
# > what kind of file can we get?

# %%
url0 = 'https://img4.goodfon.com/original/2400x1380/1/b1/wlop-ghostblade-art-devushka.jpg'
url = 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1906469856,4113625838&fm=26&gp=0.jpg'
res = requests.get(url)
with open('strwberry.jpg', 'wb') as f:
    f.write(res.content)
print(res.status_code)

# %% [markdown]
# > selenium
# > webdriver chrome
# used for dynamic website
# https://www.jianshu.com/p/dd848e40c7ad
# http://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.16/

# %%
driver = webdriver.Chrome

# %%
driver.get('https://www.toutiao.com/')
print(driver.status_code)

# %%
file = open(
    r'I:\Programming\Python\python-workspace\Workspace for Python\studying file\Spider\toutiao.html', 'w')
file.write(driver.page_source)
