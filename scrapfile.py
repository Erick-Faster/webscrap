import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

def scrape_site(SAMPLE_URL):
    SAMPLE_URL = 'https://webscraper.io/test-sites/tables/'
    
    print(f"Begin extraction of {SAMPLE_URL}")
    options = webdriver.ChromeOptions()
    options.headless = True

    options.add_argument("window-size=1920x1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')

    # options.add_argument('--disable-dev-shm-usage') # Not used 

    driver = webdriver.Chrome(options=options)
    driver.get(SAMPLE_URL)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
        
    tables = soup.find_all("table", {"class": "table-bordered"})
    tables = tables[:2]
    
    ids = []
    first_names = []
    last_names = []
    twitters = []
    
    for table in tables:
        rows = table.find_all("tr") # get all of the rows in the table
        for row in rows:  
            columns = row.find_all("td")
            if len(columns) == 0:
                continue
            
            ids.append(columns[0].text)
            first_names.append(columns[1].text)
            last_names.append(columns[2].text)
            twitters.append(columns[3].text)
            
    driver.close()

    print(f"End extraction of {SAMPLE_URL}")
    
    data = {'id': ids,
            'first_name': first_names,
            'last_name': last_names,
            'twitter': twitters}
            
    df = pd.DataFrame(data)
    return df.to_csv(index=False)