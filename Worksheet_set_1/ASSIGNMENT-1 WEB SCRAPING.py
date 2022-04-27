#!/usr/bin/env python
# coding: utf-8
                                              ASSIGNMENT-1 
                                              WEB SCRAPING
# In[ ]:





# In[9]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# Q1. Write a python program to display all the header tags from wikipedia.org.

# In[78]:


from bs4 import BeautifulSoup
import requests


# In[ ]:


page = requests.get("https://www.wikipedia.org/")


# In[ ]:


soup = BeautifulSoup(page.content, 'html.parser')


# In[ ]:


soup


# In[ ]:





# Q2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame.

# In[264]:


from bs4 import BeautifulSoup
import requests


# In[265]:


page = requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc')
page


# In[269]:


soup = BeautifulSoup(page.content)
soup


# Scraping first name

# In[270]:


first_title = soup.find('h3',class_="lister-item-header")
first_title


# In[271]:


first_title.text


# scraping first rating

# In[202]:


first_rating = soup.find('div',class_="ratings-bar")
first_rating.text


# Scraping year of release

# In[204]:


yor = soup.find('span',class_="lister-item-year text-muted unbold")
yor.text


# Scraping multiple titles

# In[205]:


titles = []
for i in soup.find_all('h3',class_="lister-item-header"):
    titles.append(i.text)
    
titles


# Scraping multiple ratings

# In[272]:


ratings = []
for i in soup.find_all('div',class_="ratings-bar"):
    ratings.append(i.text)
ratings


# scraping multiple year of release 

# In[210]:


yor = []
for i in soup.find_all('span',class_="lister-item-year text-muted unbold"):
    yor.append(i.text)
    
yor


# Print Length

# In[211]:


print(len(titles),len(ratings),len(yor))


# In[215]:


import pandas as pd
df = pd.DataFrame({'Titles':titles,'Ratings':ratings,'Year Of Release':yor})


# In[217]:


df


# In[ ]:





# Q3. Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.

# In[397]:


from bs4 import BeautifulSoup
import requests


# In[398]:


page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
page


# In[399]:


soup = BeautifulSoup(page.content)
soup


# scraping first title

# In[400]:


first_title = soup.find('td',class_="titleColumn")
first_title.text


# scraping rating

# In[401]:


rating = soup.find('td',class_="ratingColumn imdbRating")
rating.text


# scraping year of release

# In[402]:


yor = soup.find('span',class_="secondaryInfo")
yor.text


# scraping multiple titles

# In[403]:


titles = []
for i in soup.find_all('td',class_="titleColumn"):
    titles.append(i.text)

titles[0:100]


# scraping multiple ratings

# In[404]:


ratings = []
for i in soup.find_all('td',class_="ratingColumn imdbRating"):
    ratings.append(i.text)
    
ratings[0:100]
    


# scraping multiple year of release

# In[405]:


yor = []
for i in soup.find_all('span',class_="secondaryInfo"):
    yor.append(i.text)
    
yor[0:100]


# In[407]:


print(len(titles[0:100]),len(ratings[0:100]),len(yor[0:100]))


# In[409]:


import pandas as pd
df = pd.DataFrame({'Titles':titles[0:100],'Ratings':ratings[0:100],'Year Of Release':yor[0:100]})
df


# In[ ]:





# Q4. Write a python program to scrape product name, price and discounts from https://meesho.com/bags-ladies/pl/p7vbp

# In[279]:


from bs4 import BeautifulSoup
import requests


# In[280]:


page = requests.get("https://meesho.com/bags-ladies/pl/p7vbp")
page


# In[281]:


soup = BeautifulSoup(page.content)
soup


# scraping first product name

# In[282]:


pname = soup.find("p",class_="Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS")
pname.text


# scraping first product price

# In[283]:


price = soup.find("h5",class_="Text__StyledText-sc-oo0kvp-0 hiHdyy")
price.text


# scraping discount

# In[284]:


discount = soup.find("span",class_="Text__StyledText-sc-oo0kvp-0 lnonyH")
discount.text


# scraping multiple products name

# In[289]:


pname = []
for i in soup.find_all("p",class_="Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS"):
    pname.append(i.text)
    
pname


# scraping multiple products price

# In[290]:


price = []
for i in soup.find_all("h5",class_="Text__StyledText-sc-oo0kvp-0 hiHdyy"):
    price.append(i.text)
price


# In[ ]:


scraping multiple products discount


# In[292]:


discount = []
for i in soup.find_all("span",class_="Text__StyledText-sc-oo0kvp-0 lnonyH"):
    discount.append(i.text)
discount


# In[295]:


print(len(pname),len(price),len(discount))


# creating dataframe

# In[297]:


import pandas as pd
df = pd.DataFrame({'Products name':pname,'Price':price,'Discount':discount})
df


# In[ ]:





# Q5. Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
#    
#    a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
#    
#    b) Top 10 ODI Batsmen along with the records of their team and rating.
#   
#    c) Top 10 ODI bowlers along with the records of their team and rating.

# In[ ]:





# In[298]:


from bs4 import BeautifulSoup
import requests


# In[300]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page


# In[310]:


soup = BeautifulSoup(page.content)
soup


# ans a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

# In[369]:


names = []
for i in soup.find_all('span',class_="u-hide-phablet"):
    names.append(i.text)
names[0:10]


# In[370]:


matches = []
for i in soup.find_all("td",class_="table-body__cell u-center-text"):
    matches.append(i.text)
    
matches[0:10]


# In[371]:


ratings = []
for i in soup.find_all("td",class_="table-body__cell u-text-right rating"):
    ratings.append(i.text)
ratings[0:10]


# ans b) Top 10 ODI Batsmen along with the records of their team and rating.

# In[374]:


from bs4 import BeautifulSoup
import requests


# In[375]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")
page


# In[377]:


soup = BeautifulSoup(page.content)
soup


# In[381]:


names = []
for i in soup.find_all("td",class_="table-body__cell name"):
    names.append(i.text)
names[0:9]


# In[384]:


team = []
for i in soup.find_all("span",class_="table-body__logo-text"):
    team.append(i.text)
    
team[0:9]


# In[385]:


ratings = []
for i in soup.find_all("td",class_="table-body__cell u-text-right rating"):
    ratings.append(i.text)
ratings[0:9]


#  ans c) Top 10 ODI bowlers along with the records of their team and rating.

# In[393]:


names = []
for i in soup.find_all("td",class_="table-body__cell name"):
    names.append(i.text)
names[9:18]


# In[394]:


team = []
for i in soup.find_all("span",class_="table-body__logo-text"):
    team.append(i.text)
    
team[9:18]


# In[395]:


ratings = []
for i in soup.find_all("td",class_="table-body__cell u-text-right rating"):
    ratings.append(i.text)
ratings[9:18]


# In[ ]:





# Q6. Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# 
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# 
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# 
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[410]:


from bs4 import BeautifulSoup
import requests


# In[411]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page


# In[412]:


soup = BeautifulSoup(page.content)
soup


# ans a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# 

# In[414]:


names = []
for i in soup.find_all("span",class_="u-hide-phablet"):
    names.append(i.text)
    
names[0:10]


# In[417]:


matches = []
for i in soup.find_all("td",class_="table-body__cell u-center-text"):
    matches.append(i.text)
    
matches[0:10]


# In[419]:


ratings = []
for i in soup.find_all("td",class_="table-body__cell u-text-right rating"):
    ratings.append(i.text)
    
ratings[0:10]


# ans b) Top 10 women’s ODI Batting players along with the records of their team and rating.

# In[421]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
page


# In[422]:


soup = BeautifulSoup(page.content)
soup


# In[425]:


names = []
for i in soup.find_all("td",class_="table-body__cell name"):
    names.append(i.text)
    
names[0:9]


# In[429]:


teams = []
for i in soup.find_all("td",class_="table-body__cell nationality-logo"):
    teams.append(i.text)
    
teams[0:9]


# In[431]:


ratings = []
for i in soup.find_all("td",class_="table-body__cell u-text-right rating"):
    ratings.append(i.text)
    
ratings[0:9]


# ans c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[435]:


names = []
for i in soup.find_all("td",class_="table-body__cell name"):
    names.append(i.text)
    
names[18:28]


# In[437]:


teams = []
for i in soup.find_all("span",class_="table-body__logo-text"):
    teams.append(i.text)
    
teams[18:28]


# In[438]:


ratings = []
for i in soup.find_all("td",class_="table-body__cell u-text-right rating"):
    ratings.append(i.text)

ratings[18:28]


# In[ ]:





# Q7. Write a python program to scrape details of all the posts from coreyms.com. Scrape the heading, date, content
# and the code for the video from the link for the youtube video from the post.

# In[439]:


from bs4 import BeautifulSoup
import requests


# In[441]:


page = requests.get("https://coreyms.com/")
page


# In[442]:


soup = BeautifulSoup(page.content)
soup


# scraping heading

# In[445]:


heading = soup.find("h2",class_="entry-title")
heading.text


# scraping date

# In[448]:


date = soup.find("time",class_="entry-time",datetime="2019-11-19T13:02:37-05:00")
date.text


# scraping content

# In[451]:


content = soup.find("article",class_="post-1670 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-gzip tag-shutil tag-zip tag-zipfile entry")
content.text


# scraping video code

# In[ ]:





# In[679]:


page = requests.get("https://youtu.be/z0gguhEmWiY")
page


# In[681]:


soup = BeautifulSoup(page.content)
soup


# In[683]:


video = soup.find("https://youtu.be/z0gguhEmWiY")
video.split


# In[ ]:





# Q8. Write a python program to scrape house details from mentioned URL. It should include house title, location, area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar, Rajaji Nagar.

# In[468]:


from bs4 import BeautifulSoup
import requests


# In[491]:


page = requests.get("https://www.nobroker.in/property/sale/hyderabad/Indira%20Nagar?searchParam=W3sibGF0IjoxNy40NDc0NDc1LCJsb24iOjc4LjM1NjkyNzUsInBsYWNlSWQiOiJDaElKZzVwcF9KU1R5enNSaHBYNzU2M2VkX2ciLCJwbGFjZU5hbWUiOiJJbmRpcmEgTmFnYXIifV0=&radius=2.0&city=hyderabad&locality=Indira%20Nagar")
page


# In[492]:


soup = BeautifulSoup(page.content)
soup


# scraping data for Indira Nagar

# In[494]:


housetitle = soup.find("span",class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full")
housetitle.text


# scraping house location

# In[497]:


location = soup.find("div",class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95")
location.text


# scraping house area

# In[524]:


area = soup.find("div",class_="font-semi-bold heading-6")
area.text


# scraping house EMI

# In[525]:


EMI = soup.find("div",class_="flex flex-col w-33pe items-center border-r border-r-solid border-card-overview-border-color tp:w-half po:w-full last:border-r-1")
EMI.text


# scraping houe price

# In[519]:


price = soup.find("div",class_="flex flex-col w-33pe items-center bo tp:w-half po:w-full border-r-0")
price.text


# scraping data for JAYA NAGAR

# In[528]:


page = requests.get("https://www.nobroker.in/property/sale/hyderabad/Jaya%20Nagar?searchParam=W3sibGF0IjoxNy40OTk3NzE1LCJsb24iOjc4LjQwNjI2MjMsInBsYWNlSWQiOiJDaElKUDRreWRlcVJ5enNSOFgwU2hxd2hBM1UiLCJwbGFjZU5hbWUiOiJKYXlhIE5hZ2FyIn1d&radius=2.0&city=hyderabad&locality=Jaya%20Nagar")
page


# In[529]:


soup = BeautifulSoup(page.content)
soup


# scraping housetitle

# In[537]:


housetitle = soup.find("span",class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full")
housetitle.text


# scraping house location

# In[538]:


location = soup.find("div",class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95")
location.text


# scraping house area

# In[541]:


area = soup.find("div",class_="flex flex-col w-33pe items-center border-r border-r-solid border-card-overview-border-color tp:w-half po:w-full last:border-r-1")
area.text


# scraping house EMI

# In[544]:


EMI = soup.find("div",class_="font-semi-bold heading-6")
EMI.text


# scraping house price

# In[545]:


price = soup.find("div",class_="flex flex-col w-33pe items-center bo tp:w-half po:w-full border-r-0")
price.text


# Scraping data for Rajaji Nagar

# In[546]:


page = requests.get("https://www.nobroker.in/property/sale/bangalore/Rajajinagar?searchParam=W3sibGF0IjoxMi45OTgxNzMyLCJsb24iOjc3LjU1MzA0NDU5OTk5OTk5LCJwbGFjZUlkIjoiQ2hJSnhmVzREUE05cmpzUktzTlRHLTVwX1FRIiwicGxhY2VOYW1lIjoiUmFqYWppbmFnYXIifV0=&radius=2.0&city=bangalore&locality=Rajajinagar")
page


# In[547]:


soup = BeautifulSoup(page.content)
soup


# scraping house name

# In[549]:


housename = soup.find("span",class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full")
housename.text


# Scraping house location

# In[550]:


location = soup.find("div",class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95")
location.text

scraping house area
# In[552]:


area = soup.find("div",class_="font-semi-bold heading-6")
area.text


# scraping house EMI

# In[553]:


EMI = soup.find("div",class_="flex flex-col w-33pe items-center border-r border-r-solid border-card-overview-border-color tp:w-half po:w-full last:border-r-1")
EMI.text


# Scraping house price

# In[554]:


price = soup.find("div",class_="flex flex-col w-33pe items-center bo tp:w-half po:w-full border-r-0")
price.text


# In[ ]:





#  Q9. Write a python program to scrape mentioned details from dineout.co.in :
#     i) Restaurant name
#    ii) Cuisine
#   iii) Location
#    iv) Ratings
#     v) Image URL

# In[555]:


from bs4 import BeautifulSoup
import requests


# In[645]:


page = requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
page


# In[646]:


soup = BeautifulSoup(page.content)
soup


# scraping restaurant name

# In[647]:


name = soup.find("div",class_="restnt-info cursor")
name.text


# scraping location

# In[648]:


location = soup.find("div",class_="restnt-loc ellipsis")
location.text


# scraping price and cuisine

# In[649]:


cuisine = soup.find("span",class_="double-line-ellipsis")
cuisine.text


# scraping ratings

# In[650]:


ratings = soup.find("div",class_="restnt-rating rating-4")
ratings.text


# scraping image url

# In[651]:


imageurl = soup.find("div",class_="img cursor")
imageurl


# In[ ]:





# Q10. Write a python program to scrape first 10 product details which include product name , price , Image URL from https://www.bewakoof.com/women-tshirts?ga_q=tshirts .

# In[637]:


from bs4 import BeautifulSoup
import requests


# In[638]:


page = requests.get("https://www.bewakoof.com/women-t-shirts")
page


# In[639]:


soup = BeautifulSoup(page.content)
soup


# scraping products name

# In[643]:


name = []
for i in soup.find_all("div",class_="productCardDetail"):
    name.append(i.text)
name[0:10]


# scraping product price

# In[621]:


price = []
for i in soup.find_all("span",class_="discountedPriceText"):
    price.append(i.text)
price[0:10]


# scraping product image url

# In[616]:


imageurl = []
for i  in soup.find_all("div",class_="productImg"):
    imageurl.append(i)
imageurl[0:10]


# In[ ]:




