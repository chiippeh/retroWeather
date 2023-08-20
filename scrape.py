# import requests
# from bs4 import BeautifulSoup

# url = "https://www.dws.gov.za/Hydrology/Weekly/SumProvince.aspx"
# page = requests.get(url)

# soup = BeautifulSoup(page.content, "html.parser");
# soup = soup.prettify()

# dam_data = soup.find('table')
# print(dam_data)

from bs4 import BeautifulSoup
import requests
import json

html_text_1 = requests.get('https://www.dws.gov.za/Hydrology/Weekly/SumProvince.aspx').text #get actual dam levels
html_text_2 = requests.get('https://www.dws.gov.za/drought/weeklystatus.aspx').text #get last updated dam of dam levels
soup = BeautifulSoup(html_text_1, 'lxml')
soup_2 = BeautifulSoup(html_text_2, 'lxml')

#find last update date
last_updated = soup_2.find('td', class_='tableColumnContents')
date = last_updated.find('h2').find('b').text

#find dam level data
dam_data = soup.find('table', align='Center', border='4')
provinces = dam_data.find_all('tr')


del provinces[0]
del provinces[-1]
del provinces[-2] #get rid of swaziland

f = open("damData.csv", "w") #create new file

data = []

for province in provinces:
    province_info = province.find_all('td', align = 'Center')
    province_name = province_info[0].text
    province_percent_capacity = province_info[2].text 
    data.append({
            'province_name': province_name,
            'province_percent_capacity': province_percent_capacity
        })

# Write data to a JSON file
with open('damData.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data exported to damData.json")
    


# for province in provinces:
#     province_info = province.find_all('td', align = 'Center')
#     province_name = province_info[0].text
#     province_percent_capacity = province_info[2].text 
#     if (province_name != "Western Cape"):
#         f.write(province_name + ' ' + province_percent_capacity + '\n')
#     else:
#         f.write(province_name + ' ' + province_percent_capacity)
    

f.close()




# for province in provinces:
#     province_info = province.find_all('td', align = 'Center')

#     province_name = province_info[0].text
#     province_percent_capacity = province_info[2].text
    
#     print(f'''Province: {province_name}\nCapacity: {province_percent_capacity}% \n''')
#     # print(province_name + ' dams are ' + province_percent_capacity + '% full')
# print(f'''~~~ Data last updated : {date} ~~~''')

