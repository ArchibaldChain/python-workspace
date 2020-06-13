import urllib.request
import urllib.error
from bs4 import BeautifulSoup

def get_title(url):
    try:
        req=urllib.request.Request(url)
        response=urllib.request.urlopen(req)
    except (urllib.error.HTTPError,urllib.error.URLError) as e:
        #网页在服务器不存在，或者服务器不存在
        print(e)
        return None
    try:
        html = response.read().decode("utf-7")
        soup = BeautifulSoup(html, "html.parser")
        title=soup.body.h1
        urf = soup.find_all()
        print("****")
        print(type(urf))
        
        for each in urf:
            print("each = ",each)
            print("@@@@@@@@@@@")
            print(type(each))
    except AttributeError as e:
        #标签不存在
        return None
    return title

if __name__=="__main__":
    url="http://www.pythonscraping.com/exercises/exercise1.html"
    title=get_title(url)
    if title == None:
        print("Title could not be found")
    else:
        print(title)
