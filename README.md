## Title
### Find Coffee Shops in 24 Populated Citeis in US
--- Visualization Project CUSP

## Team members

Andrew Neil      NetID: adn323

Alex Shannon     NetID: acs882

Baoling Zhou     NetID: bz882

## Visualization Link: 
http://bl.ocks.org/baolingz/527ec140b20ffd5cb5aaa4662f471b5e

- Issues for now: 
1. The histogram is static for now, it's supposed to connected to the input user interface. 
2. The reset buttom doesn's work for now.
3. You need to refresh the page every time before you make new changes in the user interface

- Instruction: 
1. after you get into the page, you can select a city and unchecked boxes to customize the filter
2. Then, you click the update buttom and a updated map will be shown on the right-hand side. 
3. selection function: you can click the square box on the top right and then click the "selection". Doing this will enable the radias circle shown on the map. You can move it around and strech it in different sizes and shows coffee shops within the circle only. (This function will be activated automatically every time when you click the map, but the radias circle will be invisible at that point. you can click the "selection" buttom to make it visible).


## Objectives of the project
#### a brief context of the project, and what tasks you're aiming to solve using visualizations, domain(target user) and task abstraction.
We had built a multifunctional web page which enables users to see all the available coffee shops in 24 cities under several filtering functions, such as price level, coffee shop types and minimum rating.  Our target audience are people who are coffee lovers and looking for coffee shops with certain special servings, like bakeries and ice-cream. It's also a great tool for people who want to explore the coffee shops availability before they move into new neighborhoods.


## Data set involves
Yelp

## Descriptions on your visualization design choices. For example, why you're choosing the types of visualization, representations, and/or interactions in your project.

Visualization Representation:
- Scatterplots on the map shows the location of coffeeshops in 24 cities. The size of the points indicates the number of reviews available in the yelp data for different coffee places. The more reviews there are, the bigger the points will be.

- Histogram section(down for now) on the bottom left contains three parts: all the charts created are based on coffee shops remained after UI filtering. 

1. A stacked chart representing the proportion of different types of coffee
2. A histogram showing distribution of coffee shops by rating.
3. A histogram showing distribution of coffee shops by price.

Interactions:
- selection function: you can click the square box on the top right and then click the "selection". Doing this will enable the radias circle shown on the map. You can move it around and strech it in different sizes and shows coffee shops within the circle only. (This function will be activated automatically every time when you click the map, but the radias circle will be invisible at that point. you can click the "selection" buttom to make it visible)

## Outcome and Evaluation: how did the visualization helps your users to achieve the objectives.



## Visualization Tools Used
React, Javascript, Carto.



