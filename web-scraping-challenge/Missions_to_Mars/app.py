from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrap_mars_data

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/web_scrapping_challenge_db")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    # @TODO: YOUR CODE HERE!
    hemisphere = mongo.db.mars_hemisphere.find_one()
    img_link = mongo.db.mars_link_img.find_one()
    mars_title= mongo.db.mars_title.find_one()
    mars_data= mongo.db.mars_data.find_one()
    #return render_template("index.html", listings=listings)
    # Return template and data
    return render_template("index.html", vacation=hemisphere, imgLink=img_link, marsTitle=mars_title, marsData=mars_data)

# Route to rendehemisphere r index.html template using data from Mongo
@app.route("/hemisphere")
def hemisphere():

    # Find one record of data from the mongo database
    # @TODO: YOUR CODE HERE!
    hemisphere = mongo.db.mars_hemisphere.find()
    img_link = mongo.db.mars_link_img.find_one()
    mars_title= mongo.db.mars_title.find_one()
    mars_data= mongo.db.mars_data.find_one()
    #return render_template("index.html", listings=listings)
    # Return template and data
    return render_template("hemisphere.html", hemisImg=hemisphere, imgLink=img_link, marsTitle=mars_title, marsData=mars_data)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function and save the results to a variable
    # @TODO: YOUR CODE HERE!

    # Update the Mongo database using update and upsert=True
    # @TODO: YOUR CODE HERE!

  
    # This is process the hemisphere image from mars website
    marshemisphere = mongo.db.mars_hemisphere
    marshemisphere_data = scrap_mars_data.scrape_mars_hemisphere_data()
    for data_hemis in marshemisphere_data:
        marshemisphere.update({}, data_hemis, upsert=True)

    # This is mars data processing to get equatorial and other data
    marsdata = mongo.db.mars_data
    marsdata_data = scrap_mars_data.scrape_mars_data()
    marsdata.update({}, marsdata_data, upsert=True)

    # This is to get the mars image link for the main page
    marsimg = mongo.db.mars_link_img
    marsimg_data = scrap_mars_data.scrape_mars_imglink_data()
    marsimg.update({}, marsimg_data, upsert=True)

    # This is get the latest title, news and its description
    marstitle = mongo.db.mars_title
    marstitle_data = scrap_mars_data.scrape_mars_title_para()
    for data_title in marstitle_data:
        marstitle.update({}, data_title, upsert=True)
    

    # Redirect back to home page
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)
