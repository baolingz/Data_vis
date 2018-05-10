## Title
### Find Coffee Shops in 25 Populated Cities in US
--- Visualization Project CUSP

## Team members

Andrew Neil      NetID: adn323

Alex Shannon     NetID: acs882

Baoling Zhou     NetID: bz882

## Visualization Link: 
http://bl.ocks.org/baolingz/527ec140b20ffd5cb5aaa4662f471b5e


![alt text](https://raw.githubusercontent.com/baolingz/Data_vis/master/coffee.png)

- Issues for now: 
1. The histogram is static for now, it's supposed to be connected with the user interface. 
2. The reset buttom doesn's work for now.
3. You need to refresh the page every time before you make new changes in the input section.
4. The "dark" buttom doesn't work appropriately. If you accidently click it, you can refesh the page and redo the selection to make the map work again. Sorry about all of these inconvenience, we still tweaking it :(

- Instruction: 
1. After you get into the page, you can select a city and unchecked boxes to customize the filter
2. Then, you click the "update" buttom and a map with plots be shown on the right-hand side. 
3. Selection function: you can click the square box on the top right and then click the "selection". Doing this will enable the radias circle shown on the map. You can move it around and strech it in different sizes and shows coffee shops within the circle only. (This function will be activated automatically every time when you click the map, but the radias circle will be invisible at that point. you can click the "selection" buttom to make it visible).


## Objectives of the project
#### A brief context of the project, and what tasks you're aiming to solve using visualizations, domain(target user) and task abstraction.
We had built a multifunctional web page which enables users to see all the available coffee shops in 25 cities under several filtering functions, such as price level, coffee shop types and minimum rating.  Our target audience are people who are coffee lovers and looking for coffee shops with certain special servings, like bakeries and ice-cream. It's also a great tool for people who want to explore the coffee shops availability before they move into new neighborhoods.


## Data set involves
Our project deals with data from coffee shops in 25 major American cities. This data did not exist in a clean format, so we wrote a script to interface with Yelp and Zillow APIs. These pulled data is then aggregated with a spatial joins and concatenations to produce our final dataset. To perform initial exploratory analysis and to gain a better understanding of the 'coffee-shop-footprint' of different cities, we graphed location and plot data, as can be seen in our iPython Notebook. We used this analysis to inform our choice of relevant categories and to better anticipate what users may want to find on our web-visualization. 

## Descriptions on your visualization design choices. For example, why you're choosing the types of visualization, representations, and/or interactions in your project.

Visualization Representation:
- Scatterplots on the map shows the location of coffeeshops in 25 cities. The size of the points indicates the number of reviews available in the yelp data for different coffee places. The more reviews there are, the bigger the points will be.

- Histogram section(down for now) on the bottom left contains three parts: all the charts created are based on coffee shops remained after UI filtering. 

1. A stacked chart representing the proportion of different types of coffee
2. A histogram showing distribution of coffee shops by rating.
3. A histogram showing distribution of coffee shops by price.

Interactions:
- selection function: you can click the square box on the top right and then click the "selection". Doing this will enable the radias circle shown on the map. You can move it around and strech it in different sizes and shows coffee shops within the circle only. (This function will be activated automatically every time when you click the map, but the radias circle will be invisible at that point. you can click the "selection" buttom to make it visible)

## Outcome and Evaluation: how did the visualization helps your users to achieve the objectives.



## Visualization Tools Used
React, Javascript, Carto.



