# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import time


class NaverNews:
    def __init__(self):
        self.browser = self.setup_browser()
        self.table = self.get_table()
        self.write_to_text(self.table)
        self.browser.quit()

    @staticmethod
    def setup_browser():
        options = Options()
        options.add_argument("--headless")
        path = "C:/Users/jhunyeom/Desktop/coding/webdrivers/chromedriver.exe"
        browser = webdriver.Chrome(options=options, executable_path=path)
        return browser

    def get_table(self):
        table = []
        for i in range(6):
            table.append(self.scrape((i+1)*10))
        return table

    def scrape(self, age):
        url = "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=age&subType="
        self.browser.get(url+str(age))
        sources = self.browser.find_elements_by_class_name("ranking_office")
        source_list = []
        for i in sources:
            source_list.append(i.text)
        return source_list

    @staticmethod
    def write_to_text(table):
        for i in range(6):
            age_data = table[i]
            filename = "result/" + str((i+1)*10) + ".txt"
            with open(filename, 'a') as textfile:
                for source in age_data:
                    textfile.write(source.encode('utf-8') + "\n")


scrape_count = 0
while scrape_count < 10:
    now = datetime.datetime.now()
    if now.minute == 57:
        print "[" + str(scrape_count+1) + "] scraping at " + str(now)
        NaverNews()
        print "finished scrape"
        scrape_count += 1
        time.sleep(120)
