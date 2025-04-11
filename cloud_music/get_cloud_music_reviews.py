import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.get('https://music.163.com/#/song?id=2097486090') # 这里粘贴歌曲评论区网址
# 切换到嵌套网页中
driver.switch_to.frame(0)

# 要抓几页就循环几次
for page in range(903):
    time.sleep(3)
    # 下拉页面到页面底部
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
    driver.execute_script(js)
    # css选择器，根据标签属性提取内容
    list = driver.find_elements(By.CSS_SELECTOR, '.itm')
    for li in list:
        content = li.find_element(By.CSS_SELECTOR, '.cnt').text
        new_content = re.findall('：(.*)', content)[0]
        print(new_content)
        with open('reviews.txt', mode='a', encoding='utf-8-sig') as f: # 文件保存路径
            f.write(new_content)
            f.write('\n')
    driver.find_element(By.CSS_SELECTOR, '.znxt').click()