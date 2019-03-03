    #!/usr/bin/env python
    # coding: utf-8

    # In[1]:


    # Dependencies
        from bs4 import BeautifulSoup as bs
        import os
        import pandas as pd
        import time
        from splinter import Browser
        import requests
        import shutil

def Mars_browser():
        executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
        return Browser("chrome", **executable_path, headless = False)

def scrape():
        browser = Mars_browser()
        Mars_data = {}
        url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
        response = requests.get(url)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        Mars_data['title'] = title
        Mars_data['body'] = body

    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
        get_ipython().system('which chromedriver')
        executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)


        url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url)


        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        image = soup.find("img", class_="thumb")["src"]
        img_url = "https://jpl.nasa.gov"+image
        featured_image_url = img_url





        response = requests.get(img_url, stream=True)
        with open('img.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

        # Display the image with IPython.display
        from IPython.display import Image
        Image(url='img.jpg')


    # # Mars Weather

    # In[14]:


        url_tw = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(url_tw)
        soup = BeautifulSoup(browser.html, 'html.parser')


        # In[15]:


        soup.body.find_all('p')[2].text


        # In[16]:


        mars_weather= soup.body.find_all('p')[2].text
        mars_weather


        # # Mars Facts

        # In[17]:


        # Mars facts  page
        url_facts = "https://space-facts.com/mars/"
        browser.visit(url_facts)


        # In[27]:


        import pandas as pd
        # place data into a dataframe
        facts_list = pd.read_html(url_facts)
        facts_df = facts_list[0]

        facts_table = facts_df.to_html(header=False, index=False)
        print(facts_table)


        # # Mars Hemispheres

        # In[19]:


           url_hem= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


        # In[28]:


           browser.visit(url_hem)
           soup = BeautifulSoup(html, 'html.parser')
           mars_hemis=[]


        # In[32]:


        #let's loop through it
        import time
        for i in range (4):
            time.sleep(5)
            images = browser.find_by_tag('h3')
            images[i].click()

            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')

            Hemis = soup.find("img", class_="wide-image")["src"]
            img_title = soup.find("h2",class_="title").text
            img_url = 'https://astrogeology.usgs.gov'+ Hemis

            dictionary={"title":img_title,"img_url":img_url}

            mars_hemis.append(dictionary)
            browser.back()
            print(mars_hemis)
return Mars_data
