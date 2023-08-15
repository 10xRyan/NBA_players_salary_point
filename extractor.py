import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrap(url):
    page=requests.get(url)

    soup=BeautifulSoup(page.text,"html")
    table = soup.find('table')

    #Columns name
    index=table.find_all('th')
    index_name=[i.text for i in index]
    index_name.pop()
    index_name.pop()
    index_name.remove(index_name[0])

    #row data
    entries=table.find_all('tr')
    row_data_list=[]
    for row in entries:
        row_data = row.find_all('td')
        row_data_list.append([data.text for data in row_data])

    row_data_list.remove(row_data_list[0])

    player_name=[]
    salary=[]
    for i in row_data_list:
        salary.append(i[2])
        lines = i[1].split('\n')
        name = next(line.strip() for line in lines if line.strip())
        player_name.append(name)

    #Creating the data frame
    df = pd.DataFrame(columns=index_name)
    df['Player']=player_name
    df['EarningsTotal']=salary

    return df