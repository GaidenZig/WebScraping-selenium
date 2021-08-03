from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
from concurrent.futures import ProcessPoolExecutor
import concurrent.futures
import subprocess
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Scraping the name and url of a github page')
parser.add_argument('chromedriverPath', metavar='dir', type=str, help='Path to the chromedriver exe')
args = parser.parse_args()
cmd = args.chromedriverPath
process = subprocess.Popen([cmd])
process.wait(5)

driver_option = webdriver.ChromeOptions()
driver_option.add_argument("- incognito")
chromedriver_path = args.chromedriverPath

def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path, options=driver_option)

# Open the website
browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")

# extract all projects
projects = browser.find_elements_by_xpath("//h1[@class='h3 lh-condensed']")

# Extract information for each project
project_list = {}
for proj in projects:
    proj_name = proj.text
    proj_url = proj.find_elements_by_xpath("a")[0].get_attribute('href')
    project_list[proj_name] = proj_url

# Extracting data
project_df= pd.DataFrame.from_dict(project_list, orient='index')

# Manipulate the table
project_df['project_name'] = project_df.index
project_df.columns = ['project_url', 'project_name']
project_df = project_df.reset_index(drop = True)

# Export project dataFrame to CSV
project_df.to_csv('project_list.csv')

# Closing connection
browser.close()

