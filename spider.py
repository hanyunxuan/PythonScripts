from selenium import webdriver
import time
from bs4 import BeautifulSoup


driver=webdriver.Chrome("D:/ChromeDriver/chromedriver.exe")                #用chrome浏览器打开
driver.get("http://www.zhihu.com")       #打开知乎我们要登录
time.sleep(2)                            #让操作稍微停一下
driver.find_element_by_link_text('登录').click() #找到‘登录’按钮并点击
time.sleep(2)
#找到输入账号的框，并自动输入账号 这里要替换为你的登录账号
driver.find_element_by_name('account').send_keys('18761686550')
time.sleep(2)
#密码，这里要替换为你的密码
driver.find_element_by_name('password').send_keys('qianxin954')
time.sleep(2)
#输入浏览器中显示的验证码，这里如果知乎让你找烦人的倒立汉字，手动登录一下，再停止程序，退出#浏览器，然后重新启动程序，直到让你输入验证码
yanzhengma=input('验证码:')
driver.find_element_by_name('captcha').send_keys(yanzhengma)
#找到登录按钮，并点击
driver.find_element_by_css_selector('div.button-wrapper.command > button').click()