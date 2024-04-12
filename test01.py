
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
#打开护理易登录页
browser.get('https://webtest.1-1dr.com/#/login')
#登录操作
browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/input').send_keys('13888888888')
browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div/input').send_keys('666')
browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/button').click()
print("登录成功")
#等待两秒
time.sleep(2)

#断言
# test_text=browser.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div/div[2]').text
# assert "首页" in test_text

#点击长护险管理
browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/ul/li[12]/div').click()
time.sleep(2)
#点击长护险定价管理
browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/ul/li[12]/ul/a[6]').click()
time.sleep(4)
#最大化窗口
browser.maximize_window()
#点击所属项目点筛选框，打开下拉筛选框
browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/div[1]').click()
time.sleep(1)
#点击“可乐-长护险三22”
browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[2]/li[60]').click()
#截屏,保存在picture文件夹下
browser.save_screenshot('picture/success.png')

