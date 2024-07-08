# 1.模块名必须以test_开头或者_test结尾
# 2测试类必须以Test开头，并且不能有init方法
# 3.测试方法必须以test开头
#创建住院陪护订单
import pytest
from selenium.webdriver.common.by import By
import time
import random

def test_zhuyuanpeihu(test_login):
    test_login.maximize_window()
    time.sleep(2)
    #点击住院陪护管理
    test_login.find_element(By.XPATH, '// *[@id="app"]/div/div/div[1]/div[1]/div[2]/ul/li[20]/div').click()
    time.sleep(2)
    # 点击住院陪护订单
    test_login.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div[2]/ul/li[20]/ul/a[8]').click()
    time.sleep(4)
    # 最大化窗口
    #test_login.maximize_window()
    # 点击新建订单按钮
    test_login.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/button[2]').click()
    #定位到第一个窗口
    #test_login.switch_to.window(test_login.window_handles[0])
    time.sleep(2)
    #填入下单账号
    numbers=random.randint(100,999)
    test_login.find_element(By.XPATH,'//div[text()="账号信息"]/following-sibling::div/div/div[text()="下单账号"]/following-sibling::div/div//input[@type="text"]').send_keys('13828943'+str(numbers))
    time.sleep(1)
    # 填入姓名
    test_login.find_element(By.XPATH,'//div[text()="预约信息"]/following-sibling::div/div/div[text()="姓名"]/following-sibling::div/div/input[@type="text"]').click()
    time.sleep(1)
    test_login.find_element(By.XPATH,'//div[text()="预约信息"]/following-sibling::div/div/div[text()="姓名"]/following-sibling::div/div/input[@type="text"]').send_keys('可乐'+str(random.randint(0,100)))
    time.sleep(1)
    #填入年龄
    test_login.find_element(By.XPATH,'//div[text()="预约信息"]/following-sibling::div/div/div[text()="年龄"]/following-sibling::div/div/input[@type="text"]').send_keys('88')
    #选择科室
    test_login.find_element(By.XPATH,'//div[text()="预约信息"]/following-sibling::div/div/div[text()="科室"]/following-sibling::div/div/div/span').click()
    time.sleep(2)
    test_login.find_element(By.XPATH,'//div[text()="预约信息"]/following-sibling::div/div/div[text()="科室"]/following-sibling::div/div[2]/ul[2]/li[2]').click()
    time.sleep(1)
    #点击服务项
    test_login.find_element(By.XPATH,'//div[text()="协助清洁面部口腔头发手部脚部"]/parent::div/preceding-sibling::label/span').click()
    time.sleep(1)
    #点击立即预约
    test_login.find_element(By.XPATH,'//div[text()=" 预付款押金合计： "]/following-sibling::button[2]').click()
    time.sleep(1)
    # 截屏,保存在picture文件夹下
    temp=int(time.time())  #拿到当前时间戳
    test_login.save_screenshot('F:/PycharmProjects/huliyi/picture/zhuyuan_success'+str(temp)+'.png')

if __name__ == '__main__':
    pytest.main(['-vs','test_zhuyuanpeihu.py'])