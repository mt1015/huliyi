#存放前后置操作
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# @pytest.fixture()
# def test_driver():
#     browser = webdriver.Chrome()
#     browser.get('http://www.baidu.com/')
#
#     return browser
# @pytest.fixture()
# def test_get(test_driver):
#     test_driver.find_element(By.ID, "kw").send_keys('python')
#     test_driver.find_element(By.ID, "su").click


@pytest.fixture()
def test_login():
    browser = webdriver.Chrome()
    # 打开护理易登录页
    browser.get('https://webtest.1-1dr.com/#/login')
    # 登录操作
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/input').send_keys('13888888888')
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div/div/div/input').send_keys('666')
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/button').click()
    print("登录成功")
    return browser





