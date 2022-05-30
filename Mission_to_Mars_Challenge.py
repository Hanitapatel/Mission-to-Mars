#!/usr/bin/env python
# coding: utf-8

# In[1]:


##10.3.3  

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[21]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[22]:


#set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[23]:


slide_elem.find('div', class_='content_title')


# In[24]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[25]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# #   ##10.3.4

# ### Featured Images

# In[26]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[27]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[28]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[29]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[30]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### 10.3.5

# In[3]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[4]:


df.to_html()


# In[7]:


browser.quit()


# In[3]:


#Challenge D-1

# 1. Use browser to visit the URL
url = 'https://marshemispheres.com'
browser.visit(url)


# In[4]:


# Parse the resulting html with soup
html = browser.html
html_soup = soup(html, 'html.parser')

# 2. Create a list to hold the images and titles.\n",
hemisphere_image_urls = []


# In[5]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
items = html_soup.find_all('div', class_='item')
for item in items:
    item_href = item.find('a', class_='itemLink product-item').get('href')
    browser.visit(url+"/"+item_href)
    # Parse the resulting html with soup
    html = browser.html
    hem_img_soup = soup(html, 'html.parser') 
    downloads = hem_img_soup.find('div', class_='downloads')
    href = hem_img_soup.find('a', string='Sample').get('href')
    full_url = url+"/"+href
    text = hem_img_soup.find('h2', class_='title').text
    hem_info = {'img_url' : full_url, 'title': text}
    hemisphere_image_urls.append(hem_info)
    browser.back()
    
print(hemisphere_image_urls)    
browser.quit()



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


### emispheres"
  ]
 },
 {
  "cell_type": "code",
  "execution_count": 16,
  "metadata": {},
  "outputs": [],
  "source": [
   "# 1. Use browser to visit the URL \n",
   "url = 'https://marshemispheres.com/'\n",
   "\n",
   "browser.visit(url)"
  ]
 },
 {
  "cell_type": "code",
  "execution_count": 17,
  "metadata": {},
  "outputs": [],
  "source": [
   "# 2. Create a list to hold the images and titles.\n",
   "hemisphere_image_urls = []\n",
   "\n",
   "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n"
  ]
 },
 {
  "cell_type": "code",
  "execution_count": 18,
  "metadata": {},
  "outputs": [
   {
    "data": {
     "text/plain": [
      "[{'img_url': 'https://marshemispheres.com/images/full.jpg',\n",
      "  'title': 'Cerberus Hemisphere Enhanced'},\n",
      " {'img_url': 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg',\n",
      "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
      " {'img_url': 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg',\n",
      "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
      " {'img_url': 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg',\n",
      "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
     ]
    },
    "execution_count": 18,
    "metadata": {},
    "output_type": "execute_result"
   }
  ],
  "source": [
   "# 4. Print the list that holds the dictionary of each image url and title.\n",
   "hemisphere_image_urls"
  ]
 },
 {
  "cell_type": "code",
  "execution_count": 19,
  "metadata": {},
  "outputs": [],
  "source": [
   "# 5. Quit the browser\n",
   "browser.quit()"
  ]
 },
 {
  "cell_type": "code",
  "execution_count": null,
  "metadata": {},
  "outputs": [],
  "source": []
 }
],
"metadata": {
 "kernelspec": {
  "display_name": "Python 3",
  "language": "python",
  "name": "python3"
 },
 "language_info": {
  "codemirror_mode": {
   "name": "ipython",
   "version": 3
  },
  "file_extension": ".py",
  "mimetype": "text/x-python",
  "name": "python",
  "nbconvert_exporter": "python",
  "pygments_lexer": "ipython3",
  "version": "3.7.9"
 },
 "nteract": {
  "version": "0.15.0"
 }
},
"nbformat": 4,
"nbformat_minor": 4
}

