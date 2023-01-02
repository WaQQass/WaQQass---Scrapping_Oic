import sys
import time
from bs4 import BeautifulSoup
import requests
import openpyxl
import os
import subprocess

try:
    source = requests.get("https://www.oic-oci.org/home/?lan=en")
    # print(source)
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')
    # print(soup)
    # for headings and headlines
    main_para = soup.find_all("div", class_="row")
    first_para = main_para[3]
    mainheading = (main_para[3].a.text)  # Hot news headline
    mainpara = ((main_para[3].p.text))  # hotnews Paragraph
    print("main heading and paragraph is listed below\n")
    print("[Main Heading]\n", mainheading, "\n")
    print("[Main heading paragraph]\n", mainpara, "\n")
    print("other news are listed below\n")
    for inner_news in range(4, 8):
        headings = (main_para[inner_news].a.text)

        paragraphs = (main_para[inner_news].p.text)

        paragraphs = paragraphs.replace("... more", "   ")
        print(
            f"{inner_news-3}. [Main heading] \n {headings} \n [Paragraph]\n {paragraphs}")
    # For calender meetings
    all_meeings_box = soup.find_all("div", class_="media")
    print("calender events are listed below\n")
    for cal_meeting in range(1, 4):
        calender_meeting = all_meeings_box[cal_meeting].text
        print(
            f"{cal_meeting}.[calender event]\n{calender_meeting}\n")
    # for getting departments heading
    departments_heading_fetch = soup.find_all("div", class_="panel-heading")
    department_heading = ((departments_heading_fetch[1]).text)
    print("departments are listed below \n",
          department_heading)  # dparments heading get
    # for getting departments list and URL's
    dp_list_block = soup.find_all(
        "div", class_="panel-body")
    departmnts_list = dp_list_block[1].find_all("li")
    concatinate = "https://www.oic-oci.org"
    for i in range(len(departmnts_list)):
        show_list = departmnts_list[i].a.text
        show_link = departmnts_list[i].a.attrs["href"]
        show_link = show_link.replace("..", "")
        link = concatinate+show_link
        # dpt list
        print(
            f"{i+1}.[heading] {show_list}\n[link]{link}\n")


except Exception as e:
    print(e)
