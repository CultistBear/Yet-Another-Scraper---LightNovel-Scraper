from bs4 import BeautifulSoup
import cloudscraper
import os
from __main__ import NovelLinks,NovelTitles,ChapterLinks

os.system("color")

Scraper = cloudscraper.create_scraper()

def Search(Series_Name):
  headers = {
      "accept": "*/*",
      "x-requested-with": "XMLHttpRequest",
      "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4549.3 Safari/537.36",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "origin": "https://www.readlightnovel.org",
      "referer": "https://www.readlightnovel.org/",
  }

  data = {
    "q": Series_Name
  }

  response=Scraper.post("https://www.readlightnovel.org/search/autocomplete", headers=headers, data=data)
  Soup=BeautifulSoup(response.content, "html.parser").find_all("li")
  for i in Soup:
    NovelLinks.append(i.a["href"])
    NovelTitles.append(i.find("span",class_="title").string)

def ChapterRange(ChosenNovelLink):
  response=Scraper.get(ChosenNovelLink)
  Soup=BeautifulSoup(response.content,"html.parser").find("div",id="accordion",class_="panel-group")
  for i in Soup.find_all("ul",class_="chapter-chs"):
    for j in i.find_all("a",href=True,string=True):
      ChapterLinks.append(j["href"])

def Download(ToDownloadChapterLink,FinalPath):
  try:
    ChapterContent=[]
    response=""
    response=Scraper.get(ToDownloadChapterLink)
    Soup=BeautifulSoup(response.content,"html.parser")
    for i in Soup.find("div",class_="hidden",id="chapterhidden").find_all("p"):
      ChapterContent.append(i.text.strip().replace("\n", "")+"\n\n")
    ChapterTitle=str(Soup.find("div",class_="block-title").a.string+Soup.find("div",class_="block-title").a.next_sibling)
    CompleteName = os.path.join(FinalPath,ChapterTitle+".txt" )
    f=open(CompleteName, "w+", encoding="utf-8")
    for i in ChapterContent:
        f.write(i)
    print("\033[0;36m",ChapterTitle," Completed!\033[0;37m")
  except FileNotFoundError:
    pass
