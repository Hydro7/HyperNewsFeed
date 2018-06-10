
# Hyper News Feed

## General
The Hyper New Feed is a news crawler made for providing an unbiased view on the things happening around you. It can be upgraded to include more locations given a bigger data set of websites to go from. However currently there is no way to set your location such that you get local news and you would as such just get the most recent news as the crawler finds it. Furthermore the app currently saves the articles it finds along with the title and publishing company, if it is a company. It then saves these in a database explained [here](https://github.com/Mikmist/HyperNewsFeed/blob/master/source/backend/database/readme.md). For the web app we made a Vue web app that can pull the articles from the database and display them in a good looking way. Alternatively the user can also search through the posts and find the articles that they wish to see.

## Usage
### Frontend
Usage of the web app is pretty straight forward, when visiting the page the user will be presented with a single page displaying the current news. The user can search through our database for articles that they might be intereseted in.
### Backend
For backend usage we currently have not much customization.  However the ```dataset.csv``` file could swapped out to make the crawler run over other websites. Besides this in the future we might add functionality to further support customization on how long the crawler might have to run and other tools to for example make it run on more threads.


## Deployment.
The web app can currently be run run using Node.js and Vue. Starting the app is currently done by using the command ```npm run dev```. While still in development this will be the way it is run. The web app is dependent on the flask server for sending REST requests. This will be run by the host that is maintaining the server. The server should preferebly be run on a linux server. When this is the case it can be run by executing the shell file ```run_me.sh```. If you wanna run the server on another operation system, you can simply start the files ```app.py``` and ```start_up.py``` with the python interperter after running ```pip install -r reqruiments.txt```.




