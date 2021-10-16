from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/ADMIN/pro127/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrap():
    headers = ["name","Distance","planet_mass","mass", "radius"]
    Star_data = []
    for i in range(0,426):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","name"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            Star_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/tbody/tr[1]/td[1]/span[1]').click()
    with open("scrapper.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(Star_data)

scrap()