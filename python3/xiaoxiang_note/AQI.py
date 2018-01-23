# coding=utf-8

import requests
from bs4 import BeautifulSoup
import csv

def main():
    crawler_all_city()


def crawler_all_city():
    city_dist = get_all_cities()
    with open("aqi.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        have_title = False
        for (name, pingyin) in city_dist.items():
            city_aiq = get_city_aiq("http://pm25.in/" + pingyin)
            if not have_title:
                writer.writerow(["city_name"] + list(city_aiq.keys()))
                have_title = True
            writer.writerow([name] + list(city_aiq.values()))


def get_html_text(url):
    request = requests.get(url=url, timeout=30)
    print(request.status_code)
    if request.status_code == 200:
        return request.text


def get_all_cities():
    html = get_html_text("http://pm25.in")
    soup = BeautifulSoup(html, "lxml")
    div = soup.find_all("div", {"class", "bottom"})
    city_link_list = div[1].find_all("a")
    city_dist = {}
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link["href"][1:]
        city_dist[city_name] = city_pinyin
    return city_dist


def get_city_aiq(url):
    html = get_html_text(url)
    soup = BeautifulSoup(html, "lxml")
    divs = soup.find_all("div", {"class": "span1"})
    city_api = {}
    for div in divs:
        try:
            caption = div.find("div", {"class": "caption"}).text.strip()
            value = div.find("div", {"class": "value"}).text.strip()
            city_api[caption] = value
        except:
            print("解析异常", div)
    return city_api


if __name__ == '__main__':
    main()
