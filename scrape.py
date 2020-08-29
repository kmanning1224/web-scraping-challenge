import requests as req
import time
from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver
import requests
from pymongo import MongoClient



client = MongoClient(
        'localhost',
        27017
    )
db = client['mars_db']
collection = db['mars_info']

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape(collection, data):
    browser = init_browser()
    webinfo = {}

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    webinfo["title"] = soup.find("div", class_='content_title').find('a').get_text()
    webinfo["body"]= soup.find("div",class_='rollover_description_inner').get_text()

    

    return webinfo.insert_one(data)

def img_scrape():
    browser = img_scrape()
    featured_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    main_url = 'https://www.jpl.nasa.gov'
    browser.visit(featured_image)

    image = browser.html
    soup = BeautifulSoup(image, "html.parser")

    image_url = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    image_url = main_url + image_url

    return image_url

def fact_scrape():

    browser = fact_scrape()
    facts_url = 'https://space-facts.com/mars/'
    driver = webdriver.Chrome()
    driver.get(facts_url)
    html = driver.page_source

    tables = pd.read_html(facts_url)
    facts = tables[0]
    facts.columns = ['Planet', 'Profile']

    return facts

def astro_images():
    astro_image_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(astro_image_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    images = []
    list_link = soup.find("div", class_="result-list")
    img_url = list_link.find_all("div", {"class":"item"})
    download = soup.find("div", class_="downloads")

    for img_url in img_url:
        title= img_url.find("h3").text
        img_link = img_url.find("a")["href"]
        img_link_full = "https://astrogeology.usgs.gov/" + img_link
        browser.visit(img_link_full)
        html_url = browser.html
        soup = BeautifulSoup(html_url, "html.parser")
        downloads = soup.find("div", class_="downloads")
        img_full = downloads.find("a")["href"]
        images.append({"title": title, "img_link": img_full})

    return images