# NasaApp
My Personal App that helps pull a new space picture daily and provide other interesting daily science articles and tidbits. It is also an oppurtunity to showcase my abilities in Python to potential clients who may be interested in leveraging my skillsets. I wanted to make an app that covered a few different topics (APIs, Web Scraping, GUIs). 

The app at a high level has a a few sections:

"Nasa Events" displays various active nartural event happening currently around the world as well as the GPS coordinates for the most recent location

"Recent Space Articles" is a cliclable list that will take you to articles that are updated regularly at runtime. 

"Background Change" section works to grab the NASA image of the day API, download and set as desktop background. Also has a cooresponding fact if interested.




There are three python files used to generate the GUI with all the data. 

nasa.py : This file is what connects to the APOD endpoint and downloads the current daily imagine of the day. All images are saved in a file and set to desktop background. Also includes function to actually change desktop. **Note this only works on MacOs. Apple script is used to change the desktop background. Windows users will need to edit this a bit. 



articleScrapper.py connects to https://www.sciencenews.org space articles and using the Beautiful Soup web scraping library gets the headers and links to include in the app. 


NasaPortfolio.py Contains the code needed to assemable the actual GUI. It leaverages the Tkinter library to build a simple GUI. 


