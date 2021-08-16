#!/usr/bin/env python
# coding: utf-8

# In[4]:


#dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver

import requests
import time


# In[11]:


def scrape():
    # # Mars News
    #url and get page with requests
    url = 'https://redplanetscience.com/'
    browser = Browser('chrome')
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    soup
    
    #get soup (object)
    content_title = soup.find('div', class_ = 'content_title')
    news_title = content_title.text.strip()
    article_teaser_body = soup.find('div', class_ = 'article_teaser_body')
    news_p = article_teaser_body.text.strip()
    print("Title: ",news_title)
    print("Paragraph: ",news_p)


    # # JPL Mars Space Images - Featured Image


    #visit the URL
    url = "https://spaceimages-mars.com"
    browser.visit(url)


    #pause 2 seconds to let it load
    time.sleep(2)


    #scrape browser into soup and find full resolution image of Mars
    html = browser.html
    image_soup = bs(html, "lxml")
    img_url = image_soup.find('img', class_ = 'headerimage fade-in')['src']



    #append the url snippet to the full url of the image 
    featured_img_url = "https://spaceimages-mars.com/" + img_url
    featured_img_url


    # # Mars Facts


    url = 'https://galaxyfacts-mars.com'


    tables = pd.read_html(url)
    tables


    facts_df = tables[1]
    facts_df.columns = ['Fact', 'Value']
    facts_df['Fact'] = facts_df['Fact'].str.replace(':', '')
    print(facts_df)
    facts_html = facts_df.to_html()

    print(facts_html)


    # # Mars Hemispheres

    url = 'https://marshemispheres.com/'


    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    items = soup.find_all('div', class_='item')



    urls = []
    titles = []
    for item in items:
        urls.append(url + item.find('a')['href'])
        titles.append(item.find('h3').text.strip())
    print(urls)
    titles


    browser.visit(urls[0])
    html = browser.html
    soup = bs(html, 'html.parser')
    oneurl = url+soup.find('img',class_='wide-image')['src']
    oneurl


    img_urls = []
    for oneurl in urls:
        browser.visit(oneurl)
        html = browser.html
        soup = bs(html, 'html.parser')
        oneurl = url+soup.find('img',class_='wide-image')['src']
        img_urls.append(oneurl)

    img_urls


    hemisphere_image_urls = []

    for i in range(len(titles)):
        hemisphere_image_urls.append({'title':titles[i],'img_url':img_urls[i]})

    hemisphere_image_urls

    # Assigning scraped data to a page
    
    marspage = {}
    marspage["news_title"] = news_title
    marspage["news_p"] = news_p
    marspage["featured_img_url"] = featured_img_url
    marspage["marsfacts_html"] = facts_html
    marspage["hemisphere_image_urls"] = hemisphere_image_urls

    return marspage


# In[ ]:




