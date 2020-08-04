import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def getHTMLText(url):
    try:
        header = {"user-agent": 
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
        r = requests.get(url, timeout = 20, headers = header)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        with open('web.html', 'w') as f:
            f.write(r.text)
            f.close
        return r.text

    except:
        print("Failed on fetch: " + url)
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)): 
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])

    except:
        print("failed to parse")  
    
def parsePage_soup(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find('div', class_ = "m-itemlist")
    item_list = items.find_all('div', class_ = "item")

    price_list = []
    name_list = []
    url_list  = []
    for item in item_list:

        p = item.find('div', class_ = "price g_price g_price-highlight")
        price = p.strong.string.replace('\n', '')
        price = price.replace(' ', '')

        price_list.append(p.span.string + price)
        text_temp = item.find('div', class_ = 'ctx-box J_MouseEneterLeave J_IconMoreNew')

        u = text_temp.find('a', class_ = "J_ClickStat")
        url_list.append(u['href'])
        name = ""
        for str in u.strings:
            name = name + str
        name = name.replace('\n', '')
        name = name.replace(' ', '')
        name_list.append(name)

    ilt = {'price': price_list, 
            'name': name_list, 
            'url' : url_list}

    return ilt

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格￥", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
    
def saveGoodsList(ilt):
    df = pd.DataFrame(ilt)
    df.to_csv("dress_Price_comparsion.csv")


def main():
    goods = '裙子'
    depth = 2   # pages to be scratch
    start_url = 'https://s.taobao.com/search?q='+goods
    infoList = []
    # for i in range(depth):
    #     try:
    #         url = start_url + "&s=" + str(44*i)
    #         html = getHTMLText(url)
    #         parsePage_soup(infoList, html)
    #     except:
    #         print('Failed, url: ' + start_url + "&s=" + str(44*i))
    #         continue

    with open("裙子_淘宝搜索.html", 'r') as f:
        html = f.read()
        f.close()
    info = parsePage_soup(html)
    saveGoodsList(info)

    parsePage(infoList, html)
    printGoodsList(infoList)

if __name__ == "__main__":
    main()
