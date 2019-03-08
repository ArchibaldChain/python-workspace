import random
import time
import requests
from bs4 import BeautifulSoup

s = requests.session()
r = s.get('https://cas.sustc.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.sustc.edu.cn%2Fjsxsd%2F')

CAS_soup = BeautifulSoup(r.content, 'html.parser')
execution = CAS_soup.find("input", attrs={"name": "execution"})["value"]

r = s.post('https://cas.sustc.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.sustc.edu.cn%2Fjsxsd%2F',
           data={"username": "11712317",
                 "password": "",
                 "execution": execution,
                 "_eventId": "submit",
                 "geolocation": " "})

r = s.get("http://jwxt.sustc.edu.cn/jsxsd/xsxk/xklc_list?Ves632DSdyV=NEW_XSD_PYGL")

r = s.get("http://jwxt.sustc.edu.cn/jsxsd/xsxk/xklc_view?jx0502zbid=D102885918754CD79C2E3F167A288A11")

r = s.get("http://jwxt.sustc.edu.cn/jsxsd/xsxk/xsxk_index?jx0502zbid=D102885918754CD79C2E3F167A288A11")

pro_class_id = [

				"201820191000721", "数据结构与算法分析[英文-实验3班（选择计算机专业的学生修读）]",
				"201820191000727", "数字逻辑[英文-实验3班]",
				"201820191000712", "形势与政策[中文6班]"]
				

#sch_class_id = ["201820191001077", "PE"]
while True:
# for i in range(0, len(sch_class_id) - 1):
#      if i % 2 == 0:
#         res = s.get(
#            "http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/bxqjhxkOper?" + "jx0404id=" + sch_class_id[i] + "&xkzy=&trjf=")
#        print(sch_class_id[i + 1], res.json()["message"])
#       time.sleep(1*random.random())
    for i in range(0, len(pro_class_id) - 1):
        if i % 2 == 0:
            res = s.get(
                "http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/fawxkOper?" + "jx0404id=" + pro_class_id[i] + "&xkzy=&trjf=")
            print(pro_class_id[i + 1], res.json()["message"])
            time.sleep(1*random.random())
