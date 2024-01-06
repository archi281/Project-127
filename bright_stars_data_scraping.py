import requests
from bs4 import BeautifulSoup
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

stars_data = []
headers = ['Star_name','Distance','Mass','Radius']  

def scrape():
        page = requests.get(START_URL)
   
        soup = BeautifulSoup(browser.page_source, "html.parser")

        bright_star_table = soup.find("table", attrs={"class", "wikitable"})

        table_body = bright_star_table.find('tbody')

        table_rows = table_body.find_all('tr')

        for row in table_rows:
            table_cols = row.find_all('td')
            temp_list = []
            for col_data in table_cols:
                data = col_data.text.strip()
                temp_list.append(data)
            stars_data.append(temp_list)
  
scrape()

for i in range(0,len(stars_data)):
    
    Star_names =stars_data [i][1]
    Distance = stars_data[i][3]
    Mass = stars_data[i][5]
    Radius = stars_data[i][6]

    
    stars_data.append(required_data)

print(stars_data)


star_df_1 = pd.DataFrame(stars_data, columns=headers)
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
