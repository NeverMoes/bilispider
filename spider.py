import requests
from selenium import webdriver

path = r'/usr/bin/phantomjs'


hidden_test_url = 'http://www.bilibili.com/video/av6536710/'

normal_test_url = 'http://www.bilibili.com/video/av7629588/'

driver = webdriver.PhantomJS(executable_path=path)

driver.get(normal_test_url)

with open('/home/nemos/down/test.html', 'w') as f:
    f.write(driver.page_source)

