from selenium import webdriver
import time
 
driver=webdriver.Chrome()
#driver.get("http://www.spic.com.cn/2018news/zhxx/")


driver.get("https://www.sustech.edu.cn/zh/shizihuancunyemian.html#4")
time.sleep(3)               #留出加载时间
 
links=driver.find_elements_by_xpath("/html/body/div[5]/div[4]/ul/li/a")  #获取到所有a标签，组成一个列表
length=len(links)           #列表的长度，一共有多少个a标签
 
for i in range(0,length):   #遍历列表的循环，使程序可以逐一点击
    links=driver.find_elements_by_xpath("/html/body/div[5]/div[4]/ul/li/a")    #在每次循环内都重新获取a标签，组成列表
    link=links[i]           #逐一将列表里的a标签赋给link
    url=link.get_attribute('href')  #提取a标签内的链接，注意这里提取出来的链接是字符串
    driver.get(url)         #不能用click，因为click点击字符串没用，直接用浏览器打开网址即可
    time.sleep(1)           #留出加载时间
    title=driver.find_element_by_xpath("//div[@class='articleTitle']").text   #.text的意思是指输出这里的纯文本内容
    print(title)
    content=driver.find_element_by_xpath("//div[@class='TRS_Editor']").text
    print(content)
    print("\n")
    driver.back()           #后退，返回原始页面目录页
    time.sleep(1)           #留出加载时间
 
print(length)               #打印列
