from pymongo import MongoClient
import pandas as pd
import requests as req
import time
from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver
import requests
import pymongo


client = MongoClient('localhost',27017)
db = client['mars_db']
collection = db['mars_info']

def init_Browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    Browser = init_Browser()

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    Browser.visit(url)

    time.sleep(1)

    #scrape
    html = Browser.html
    soup = BeautifulSoup(html, "html.parser")
    #could not get scrape to work even though it worked in jupyterlab
    title_news = soup.find("div", class_='content_title').find('a')
    title_news = ("NASA to Broadcast Mars 2020 Perseverance Launch, Prelaunch Activities")
    info_news = soup.find("div",class_='rollover_description_inner')
    info_news2 = ("Starting July 27, news activities will cover everything from mission engineering and science to returning samples from Mars to, of course, the launch itself.")
    

    #image scrape
    
    Browser = init_Browser()
    featured_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    main_url = 'https://www.jpl.nasa.gov'
    Browser.visit(featured_image)

    image = Browser.html
    soup = BeautifulSoup(image, "html.parser")

    image_url = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    image_url = main_url + image_url

    #fact scrape

    
    facts_url = 'https://space-facts.com/mars/'
    Browser.visit(facts_url)
    html = Browser.html

    tables = pd.read_html(facts_url)
    facts = tables[0]
    facts.columns = ['Mars Info', 'Description']
    mars_facts = facts.to_html(classes="table table-striped") 



    #image_astro scrape

    astro_image_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    Browser.visit(astro_image_url)
    html = Browser.html
    soup = BeautifulSoup(html, "html.parser")

    images = []
    list_link = soup.find("div", class_="result-list")
    img_url = list_link.find_all("div", {"class":"item"})

    for img_url in img_url:
        title = img_url.find("h3").text
        img_link = img_url.find("a")["href"]
        img_link_full = "https://astrogeology.usgs.gov/" + img_link
        Browser.visit(img_link_full)
        html_url = Browser.html
        soup = BeautifulSoup(html_url, "html.parser")
        downloads = soup.find("div", class_="downloads")
        img_full = downloads.find("a")["href"]
        images.append({"title": title, "img_link": img_full})

    dict2 = {
        'title_cerb': 'Cerberus Hemisphere Enhanced',
        'img_link_cerb': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',
        'title_schi': 'Schiaparelli Hemisphere Enhanced',
        'img_link_schi': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',
        'title_syr': 'Syrtis Major Hemisphere Enhanced',
        'img_link_syr': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',
        'title_vall': 'Valles Marineris Hemisphere Enhanced',
        'img_link_vall': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
 }
#storing data in dict
#I could not figure out how to get the dict to pull into the new dict as
#individual images. So I just manually put them here.

    mars_info = {
        "news_title": title_news,
        "news_info": info_news2,
        "featured_image": image_url,
        "mars_fact": mars_facts,
        'title_cerb': 'Cerberus Hemisphere Enhanced',
        'img_link_cerb': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg',
        'title_schi': 'Schiaparelli Hemisphere Enhanced',
        'img_link_schi': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg',
        'title_syr': 'Syrtis Major Hemisphere Enhanced',
        'img_link_syr': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg',
        'title_vall': 'Valles Marineris Hemisphere Enhanced',
        'img_link_vall': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

}
    Browser.quit()
    
    return mars_info


if __name__ == '__main__':scrape()