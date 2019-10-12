import urllib.request
import urllib.error
import re
from bs4 import BeautifulSoup

def get_href(url):
    try:
        req=urllib.request.Request(url)
        response=urllib.request.urlopen(req)
    except (urllib.error.HTTPError,urllib.error.URLError) as e:
        #网页在服务器不存在，或者服务器不存在
        print(e)
        print("*")
        return None
    try:
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        title=soup.body.h1
        href_ = soup.find_all(name='a')
        herf = []
        for each in href_:
            if str(each.get('href'))[:30]=='https://www.sustech.edu.cn/zh/':
                herf.append(each.get('href'))
        print('end')
        
    except AttributeError as e:
        #标签不存在
        return None
    return herf

def find(url):
    try:
        req=urllib.request.Request(url)
        response=urllib.request.urlopen(req)
    except (urllib.error.HTTPError,urllib.error.URLError) as e:
        #网页在服务器不存在，或者服务器不存在
        print(e)
        return None
    try:
        html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        title=soup.body.h1
        regex = ["德国图宾根大学", "德国蒂宾根大学","University of Tubingen", "Eberhard Karls Universität Tübingen"]
        
        contents = soup.find_all('span')
        for content in contents:
            print(content.span.get_text())
            for each in regex:

                if re.search(each, content.span.get_text()) is not None:
                    print(url)
                    return(url)

        #content = soup.find (id='introduce').h1.get_text()
    except AttributeError as e:
        #标签不存在
        return None
    return None

if __name__=="__main__":
    url="https://www.sustech.edu.cn/zh/shizihuancunyemian.html#4"

    
    href = get_href(url)
    print(href)
    # link = []
    # for each in href:
    #     link.append(find(each))
    
    # print("******************************")
    # print(link)