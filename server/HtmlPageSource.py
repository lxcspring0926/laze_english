from selenium import webdriver
from bs4 import BeautifulSoup
import time

class HtmlSourceClass:
  # コンストラクタ
  def __init__(self):
    self.htmlSource = ""
    self.url = ""
 
  # デストラクタ
  def __del__(self):
    self.htmlSource = ""
    self.url = ""
 
  def getInfo(self):
    return self.htmlSource
 
  def setInfo(self, url):
    self.url = url

  def editHtmlPageSource(self):
     driver = webdriver.PhantomJS()
     url = self.url 
     driver.get(url)
     time.sleep(3)
     self.htmlSource = driver.page_source
     html = driver.page_source

     soup = BeautifulSoup(html, "lxml")

     print(soup.select('div[class="gt-cc-l"]'))
