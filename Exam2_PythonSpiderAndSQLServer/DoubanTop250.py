import csv
import os
import time

import requests
from bs4 import BeautifulSoup

import pymssql


def GetHtmlText(Url):
    try:
        REQ_HEADER = {
            'Host': 'movie.douban.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Referer': 'https://movie.douban.com/explore',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
        }
        req = requests.get(Url, headers=REQ_HEADER)
        req.raise_for_status()
        req.encoding = req.apparent_encoding
        return(req.text)
    except:
        print('Something Wrong Occured, Please try again.')


def GetMovieInfo(Html):
    soup = BeautifulSoup(Html, 'html.parser')
    Lis = soup.select("ol li")
    for Li in Lis:
        # index
        Index = Li.find("em").text
        # title
        Title = Li.find("span", class_="title").text
        # comment, and replace the unleagel string
        Comment = Li.find("span", class_="inq").text
        Comment = Comment.replace("\u22ef", "")
        # rating num
        RatingNum = Li.find("span", class_="rating_num").text
        SvaeToFile(Index, Title, Comment, RatingNum)


def CheckFileExists():
    if not os.path.exists("D:\\PythonData"):
        os.mkdir("D:\\PythonData")
    else:
        os.removedirs("D:\\PythonData")


def SvaeToFile(index, title, comment, ratingNum):
    with open('D:\\PythonData\\douban.csv', 'a') as f:
        f.write(f'{index}, {title}, {comment}, {ratingNum}\n')


def MSSQL_Insert(sql):
    with pymssql.connect(host='127.0.0.1', user='', password='', database='PySpiderData') as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()


def MSSQL_PrintAll():
    with pymssql.connect(host='127.0.0.1', user='', password='', database='PySpiderData') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM MoviesTop250')
        print(cursor.fetchall())


# judge if the file exist and run the main function
CheckFileExists()
for i in range(1):
    Url = "http://movie.douban.com/top250?start=" + str(0)
    print("***正在爬取第" + str(i + 1) + "页***")
    content = GetHtmlText(Url)
    vSoup = GetMovieInfo(content)
    time.sleep(2)
print("*****爬取完毕*****")

with open("D:\\PythonData\\douban.csv") as f:
    reader = csv.reader(f)
    for col in reader:
        col = list(map(lambda x: x.strip(), col))
        rank, name, introduction, grade = int(
            col[0]), col[1], col[2], float(col[3])
        seq = "INSERT INTO MoviesTop250 VALUES (%d, '%s', '%s', %.1f)" % (
            rank, name, introduction, grade)
        MSSQL_Insert(seq)
