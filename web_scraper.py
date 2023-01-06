import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By #needed for declaration of css selector method By.{METHOD}
from webdriver_manager.chrome import ChromeDriverManager #needed for webdriver.Chrome service arg DEPRECATED
from selenium.webdriver.chrome.service import Service #needed for webdriver.Chrome service arg DEPRECATED

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
results = []
author_names = []
dates_list = []
links_list = []
with webdriver.Chrome() as driver: #CLOSES AUOMATICALLY W/O HAVING TO  driver.close()
    #executable_path = "/Users/yuliia.hlamazdenko/Downloads/chromedriver" is DEPRICATED
#wait = WebDriverWait(driver, 10)
    driver.get("https://oxylabs.io/blog")
    time.sleep(10)
    content = driver.find_element(By.CSS_SELECTOR, "div.css-1kfmdo4.emlf3670")
    title = content.find_elements(By.TAG_NAME, "h5")
    feat_title = driver.find_element(By.TAG_NAME, 'h4')
    results.append(feat_title.text)
    authors = driver.find_elements(By.CLASS_NAME, "css-19fxrd0")
    dates = driver.find_elements(By.CLASS_NAME, "css-1uydhl8")
    feat_link = driver.find_element(By.CLASS_NAME, 'css-1gklcwp').get_attribute('href')
    links = driver.find_elements(By.CLASS_NAME, 'css-g65o95')
    for el in links:
        #print(el.get_attribute('href'))
        links_list.append(str(el.get_attribute('href')))

    for el in dates:
        date = el.text
        dates_list.append(date)
    for el in authors:
        author_name = el.text
        author_names.append(author_name)
    for el in title:
        title = el.text
        if title not in results:
            results.append(title)
links_list = links_list[2:]
links_list = [feat_link]+links_list
data_file = pd.DataFrame({'Names':results, 'Dates':dates_list, 'Author':author_names, 'Reference link':links_list})
data_file.to_csv("names.csv", index=False, encoding="utf-8")

# results = []
# content = driver.page_source
# soup = BeautifulSoup(content, features="html.parser")
#
# for el in soup.find_all("div",{"class": "css-19brrzf"}):
#     print(el.get('a'))
