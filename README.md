## Find Coffee Shops in 25 Populated Cities in US
CUSP Data Visualization Final Project

## Team members

Andrew Neil      NetID: adn323

Alex Shannon     NetID: acs882

Baoling Zhou     NetID: bz882

## Visualization Link: 
http://ando9.pythonanywhere.com/


![alt text](https://github.com/baolingz/Data_vis/blob/master/coffee_app_image.PNG)

- Instruction: 
1. After you get into the page, you can select a city and unchecked boxes to customize the filter. (All checkboxes are checked as a default setting for testing purpose, since all coffee shops will be displayed at first sight. In real world practices, we will make our default setting as all things unchecked).
2. Then, you click the "update" buttom and a map with plots be shown on the right-hand side. Besides, three histograms will be shown on the left bottom section.
3. Selection function: you can click the square box on the top right and then click the "selection" buttom. Doing this will enable the radius circle shown on the map. You can move the circle around and strech it in different sizes which displays coffee shops within the circle only. (This function will be activated automatically every time when you click the map).

## Objectives of the project
We built a multifunctional web page which enables users to see all the available coffee shops in 25 cities around the United States under several filtering functions, such as price level, coffee shop types (as defined by us) and minimum rating.  Our target audience are coffee lovers and people looking for coffee shops with specific features, like bakeries and ice-cream. It's also a great tool for people who want to explore the coffee shop availability when deciding what area to move to, work in etc.


## Data set involves
Our project deals with data from coffee shops in 25 major American cities. This data did not exist in a clean format, so we wrote a script to interface with Yelp and Zillow APIs. The pulled data is then aggregated with a spatial join and concatenated to produce our final dataset. To perform initial exploratory analysis and to gain a better understanding of the 'coffee-shop-footprint' of different cities, we graphed location and plot data, as can be seen in our iPython Notebook (coffee_shop_final_notebook(1).ipynb). We used this analysis to inform our choice of relevant categories and to better anticipate what users may want to find on our web-visualization. 

## Instructions on Reproducing the web Page
- Download the following three files and upload them to the pythonanywhere/mysite (An account and virtual environment need to be created, and Altair need to be installed first).
1. Index.html: our front-end webpage design
2. app.py: connecting front-end with the back-end.
3. createChart.py: histogram creating functions
4. final_coffee.csv: final clean yelp dataset

- Create a web page served on virtual env you created and connect it to app.py.
- Access 'username'/pythonanywhere.com, which will be identical to our web page.

## Descriptions on your visualization design choices. 

Visualization Representation:
- Dot points indicating coffee shops on the map show the location of coffeeshops in 25 cities. The color of the points represents the type of coffee shop corresponding to the legend of the charts. The size of the points indicates the number of reviews available in the yelp data for different coffee places. The more reviews there are, the bigger the points will be. This provides an easy way to identify coffee shops in a neigjbpurhood that meets specific criteria of the user. One major shortcoming is the exclusion of tooltips which would make the visualization much more effective for a user who could see what specific coffee shop they are looking at.

- Graphical section on the bottom left contains three parts: all the charts were created based on coffee shops remained after UI filtering. This provides a quick and easy way of visualizing the distribution of coffee shops under the UI selection criteria. 

1. A bar chart representing the proportion of different types of coffee meeting selection criteria
2. A histogram showing distribution of coffee shops by rating.
3. A histogram showing distribution of coffee shops by price. 

Interactions:
- User Interface lets you select coffee shops based on city, type of coffee shop, cost and rating according to yelp, the results will be relected on charts and map. The user can also make modification and click the 'update' button to make charts and map update. 
- Selection function: you can click the square box on the top right and then click the "selection" buttom. Doing this will enable the radius circle shown on the map. You can move the circle around and strech it in different sizes which displays coffee shops within the circle only. (This function will be activated automatically every time when you click the map).

## Outcome and Evaluation: how did the visualization helps your users to achieve the objectives.
The visualization provides the user with a quick and easy tool which allows them to know a neighborhood/city regarding coffee shop availablity by different types, costs and ratings. With this tool, people can easily assess choices between different areas to live, work or meet someone. 

- Shortcoming
1. The visualization has no tooltip that would make it easier for the user to identify the name of coffee shops. 
2. the chart does not updated based on selection circle or zoom of map, which means the user cannot understand the specific characteristics of a specific neighbourhood. 

These two features should be improved. 


## Visualization Tools Used
React, Javascript, Carto, Python, PythonAnywhere.
