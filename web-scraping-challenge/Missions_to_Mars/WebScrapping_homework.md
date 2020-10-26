Mars Nasa Web Scrapping Report
Introduction:
The web scrapping document provides details of the data that is web scrapped from Nasas website, there are Nasa Gov website, JPL website and other Nasa websites are used to gather the data.
The initial analysis phase on understanding the Nasas website, JPL website to get the data, developer tool used to get the tags that data is available to web scrap and store in Mongo DB.
The Local MongoDb is used to store the json data.
News and Description of Mars:
The major websites used to download the data
https://mars.nasa.gov/news/ To get the latest Nasas News and its description, so this website is scrapped to get the latest news as title and para as description, the parsed data is stored on the DB instance.
 

JPL Img file:
The JPL website https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars is used to get the high resolution image that used to build our website., it is parsed and data is retrieved and stored in the DB instance.
 

The Mars Hemisphere Img link
The Mars hemisphere image also required for the project, it is scrapped from https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars  and stored in the local mongo DB
 
Mars Data:
The Mars data is retrieved from https://space-facts.com/mars/  and stored in the mongo DB, its attributes data like equatorial_diameter,.. are captured from this website
 
MongoDB:
The data stored in mongo DB
 
 ..

 All the above data are stored in mongo db and used to build the website.  The word document has more details of the implementation.

 The file scrap_mars_display.py implements method for each transaction.

 i. To get Mars Data for equotorial.. 
 ii. To get hemisphere image data
 iii. To get the image from JPL website
 iv. To get the latest mars news and descriptions

