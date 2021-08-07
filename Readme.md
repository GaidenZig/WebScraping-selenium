# Web Scrapping with selenium project

Is a program that can navigate throught a web page and extract data, then create a csv file with it.
Written in order to learn selenium and webscraping techniques with python by following this site tutorial [go and try it for yourself!, there is no waste.](https://www.byperth.com/2018/04/25/guide-web-scraping-101-what-you-need-to-know-and-how-to-scrape-with-python-selenium-webdriver/)

currently it just take information from a gihub projects compilation page due to licenses and ethical limits of this practice and for future improvements i'll try to add paralelization functions, executable archive, pc GUI program, etc...

## Usage
For now the only way to use this is by python interpreter (i recommend 3.8 or advance) and execute:

`$ python src/main.py [path/to/the/chromedriver.exe]`

## Dependencies
- Chromedriver
- Selenium webdriver `$ pip install selenium`
- Pandas `$ pip install pandas`