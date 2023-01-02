''' print("Page ", page+1, link)
    for item in range(items_per_page):
        items = (item + 1+page * items_per_page)

        print(items)'''


'''tags = soup.find_all(
        "ul", class_="undefined list__09f24__ynIEd")
    for n in range(len(tags)):
        tag = tags[n].find_all("span", class_="raw__09f24__T4Ezm").text
        print(tag).text'''
import sys
import time
from bs4 import BeautifulSoup
import requests
import os
import subprocess
import openpyxl
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "hotels detail yelp"
# print(excel.sheetnames)
sheet.append(["page number", "sr#", "name of resturant", "people visited",
             "catagories are", "description ", "page link", "image link"])
try:
    items_per_page = 10
    num_pages = 24
    base_link = "https://www.yelp.com/search?cflt=restaurants&find_loc=San+Francisco%2C+CA&start="
    for page in range(num_pages):
        #print("Page ", page+1)
        link_url_concatinate = (page*10)
        link_url_concatinate = str(link_url_concatinate)
        link = base_link+link_url_concatinate
        source = requests.get(link)
        # print(source)
        source.raise_for_status()

        soup = BeautifulSoup(source.text, 'html.parser')
        # print(soup)
        heading_list = soup.find_all("span", class_='css-1egxyvc')
        # function to get names of resturants

        def get_names(lis):
            names_list = []
            for a in range(len(lis)):
                name = lis[a].a.text
                names_list.append(name)
            return names_list
        resNames = get_names(heading_list)

        # function for people visited
        peopleVisited = soup.find_all("span", class_="css-chan6m")

        def people_visited(lis):
            people_vis = []
            for b in range(0, 20, 2):
                people = lis[b].text
                people_vis.append(people)
            return people_vis
        people_Visited_List = people_visited(peopleVisited)
        # to find the list of catagory
        category_index = soup.find_all(
            "span", class_="css-epvm6 display--inline__09f24__c6N_k border-color--default__09f24__NPAKY")

        def catagory(lis):
            cat = []
            for d in range(len(category_index)):
                catagory_fetch = category_index[d].text
                cat.append(catagory_fetch)
            return cat

    # calling category function
        final_category_list = catagory(category_index)

        description_list = soup.find_all("p", class_="css-16lklrv")

        def des(lis):
            descriptionList = []
            for f in range(len(lis)):
                description_variable = lis[f].text
                descriptionList.append(description_variable)
            return descriptionList

        finaldescription = des(description_list)

    # to find pages lnks

        pgf = soup.find_all("span", class_="css-1wayfxy")

        def pg_link(li):
            st = []
            lkr = "https://www.yelp.com"
            for h in range(len(li)):
                pageslink = li[h].a.get("href")
                st.append(lkr+pageslink)
            return st
        print__pagelink = pg_link(pgf)

    # images link function
        img = soup.find_all("img", class_="css-xlzvdl")

        def iamges(li):
            img_ii = []
            for o in range(len(li)):
                lp = li[o]["src"]
                img_ii.append(lp)
            return img_ii
        images_link_var = iamges(img)

    #resNames, people_Visited_List, final_category_list, finaldescription, print__pagelink, images_link_var
        sheet.append(page+1)
        for data in range(len(resNames)):

            #print(f"{data+1}.[Name of resturant is]    {resNames[data]}.\n [People visied are]     {people_Visited_List[data]}.\n[categories are]      {final_category_list[data]}\n [Description is]    [Page link of this resturant is]     {print__pagelink[data]}\n [Image link is]      {images_link_var[data]}\n\n")
            sheet.append([data+1, resNames[data], people_Visited_List[data], final_category_list[data],
                          finaldescription[data], print__pagelink[data], images_link_var[data]])

except Exception as e:
    print(e)
excel.save("yelp data.xlsx")
