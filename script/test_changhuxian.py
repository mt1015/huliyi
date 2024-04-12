# 1.模块名必须以test_开头或者_test结尾
# 2测试类必须以Test开头，并且不能有init方法
# 3.测试方法必须以test开头
import pytest
from selenium.webdriver.common.by import By
import time

def test_changhuxian(test_login):
    time.sleep(2)
    # 点击长护险管理
    test_login.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/ul/li[12]/div').click()
    time.sleep(2)
    # 点击长护险定价管理
    test_login.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/ul/li[12]/ul/a[6]').click()
    time.sleep(4)
    # 最大化窗口
    test_login.maximize_window()
    # 点击所属项目点筛选框，打开下拉筛选框
    test_login.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/div[1]').click()
    time.sleep(1)
    # 点击“可乐-长护险三22”
    test_login.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[3]/div/div[2]/ul[2]/li[60]').click()
    #点击查询
    test_login.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[8]/button').click()
    #断言
    text=test_login.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[7]/div/div').text
    assert "后定价" in text
    # 截屏,保存在picture文件夹下
    test_login.save_screenshot('picture/success.png')

if __name__ == '__main__':
    pytest.main(['-vs'])