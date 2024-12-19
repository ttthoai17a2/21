import requests
from xml.dom.minidom import parseString
import csv


url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"


response = requests.get(url)
with open("rss_feed.xml", "wb") as file:
    file.write(response.content)


with open("rss_feed.xml", "r", encoding="utf-8") as file:
    xml_content = file.read()


doc = parseString(xml_content)
items = doc.getElementsByTagName("item")


news_items = []
for item in items:
    title = item.getElementsByTagName("title")[0].firstChild.data
    link = item.getElementsByTagName("link")[0].firstChild.data
    description = item.getElementsByTagName("description")[0].firstChild.data
    pub_date = item.getElementsByTagName("pubDate")[0].firstChild.data

    news_items.append({
        "Title": title,
        "Link": link,
        "Description": description,
        "Publication Date": pub_date
    })


with open("news_items.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Title", "Link", "Description", "Publication Date"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(news_items)

print("Tin tức đã được lưu vào tệp news_items.csv")
