"""
title：将中医药的原始txt转换为excel
author：superdong
original url：https://github.com/xiaopangxia/TCM-Ancient-Books
date：2023-2-8
"""

# 导入相关的库
import os
import re
import glob
import pandas as pd

# 文件夹的路径
folder_path = r"C:\Users\Superdong\Downloads\TCM-Ancient-Books-master\TCM-Ancient-Books-master"

# 文件夹中所有txt文本的获取
total_data = []
for filename in glob.glob(os.path.join(folder_path, "*.txt")):
    print(filename)
    try:
        with open(filename, "r", encoding="ANSI") as file:
            contents = file.readlines()
            total_data.append(contents)
    except:
        print("这个文件:", "\n",
              filename, "\n",
              "异常")

# 设定抽取内容
titles = []
authors = []
dynasties = []
years = []
contents = []

i = 1
j = 0

for i in range(0, 700):
    # 使用re进行匹配书名，生成列表，提取出来
    each_titles = []
    try:
        for item in total_data[j]:
            title = re.findall(r"<篇名>(.*)", item, re.DOTALL)
            each_titles.append(title)
        each_titles = list(filter(None, each_titles))[0]
        each_titles = each_titles[0].strip()
    except IndexError:
        each_titles = total_data[j][0]

    # 使用re进行匹配作者，生成列表，提取出来
    each_authors = []
    try:
        for item in total_data[j]:
            author = re.findall(r"作者：(.*)", item, re.DOTALL)
            each_authors.append(author)
        each_authors = list(filter(None, each_authors))[0]
        each_authors = each_authors[0].strip()
    except IndexError:
        each_authors = total_data[j][4]

    # 使用re进行匹配朝代，生成列表，提取出来
    each_dynasties = []
    try:
        for item in total_data[j]:
            dynasty = re.findall(r"朝代：(.*)", item, re.DOTALL)
            each_dynasties.append(dynasty)
        each_dynasties = list(filter(None, each_dynasties))[0]
        each_dynasties = each_dynasties[0].strip()
    except IndexError:
        each_dynasties = "NA"

    # 朝代提取
    dynasty = total_data[j][3][3:].rstrip()

    # 年份提取
    year = total_data[j][4][3:].rstrip()

    # 将内容按照整体进行读取
    content = total_data[j][5:]
    # 去掉列表中的左右空行
    content = [x.strip() for x in content]
    # 删除列表中的None元素
    content = list(filter(None, content))
    # 将list转为str
    content = "".join(content)

    # 添加进去总的提取内容
    titles.append(each_titles)
    authors.append(each_authors)
    dynasties.append(each_dynasties)
    years.append(year)
    contents.append(content)
    j = j + 1

# 将抽取到的内容变为字典
TCM_books = \
    {"书名": titles,
     "作者": authors,
     "朝代": dynasties,
     "年份": years,
     "内容": contents}

# 将字典内容转换为数据框
TCM_books = pd.DataFrame(TCM_books)

# 也可将数据框内容存到excel
TCM_books.to_excel(r"D:\Desktop\TCM_books.xlsx")