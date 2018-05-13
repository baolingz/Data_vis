import altair as alt
import pandas as pd
import json
import numpy as np

def LoadData(city, rating, lowcost, medcost, hicost, hihicost,strictly_coffee,
             chain, bakeries, breakfast_and_brunch, diner, deli, icecream, juice, other):
    """
        Function to load data and ensure it can be filtered by the UI inputs
    """
    import os

    directory = os.path.dirname(__file__)

    # data = pd.read_json(os.path.join(directory,"COFFEE_data.json"))
    data = pd.read_csv(os.path.join(directory,"final_coffee.csv"))



    # Filter data by city
    df = data[data.City == city]

    # Filter by minimum rating
    df = df[df.Rating >= rating]

    # Create Cost Arr
    costarr = []

    # Input COst Array Variables
    if lowcost == "true":
        costarr.append('$')
    else:
        costarr.append('null')
    if medcost == "true":
        costarr.append('$$')
    else:
        costarr.append('null')
    if hicost == "true":
        costarr.append('$$$')
    else:
        costarr.append('null')
    if hihicost == "true":
        costarr.append('$$$$')
    else:
        costarr.append('null')

    # Filter by costs
    # df2 = df[df.Price.str.contains("|".join(costarr))]
    df2 = df[(df.Price == (costarr[0])) | (df.Price == (costarr[1])) | (df.Price == (costarr[2])) | (df.Price == (costarr[3]))]

    # Create Cost Arr
    coffeearr = []

    if strictly_coffee == "true":
        coffeearr.append('strictly_coffee')
    else:
        coffeearr.append('null')
    if chain == "true":
        coffeearr.append('chain')
    else:
        coffeearr.append('null')
    if bakeries == "true":
        coffeearr.append('bakeries')
    else:
        coffeearr.append('null')
    if breakfast_and_brunch == "true":
        coffeearr.append('breakfast_and_brunch')
    else:
        coffeearr.append('null')
    if diner == "true":
        coffeearr.append('diner')
    else:
        coffeearr.append('null')
    if deli == "true":
        coffeearr.append('deli')
    else:
        coffeearr.append('null')
    if icecream == "true":
        coffeearr.append('ice_cream_and_froyo')
    else:
        coffeearr.append('null')
    if juice == "true":
        coffeearr.append('juice_and_smoothie')
    else:
        coffeearr.append('null')
    if other == "true":
        coffeearr.append('other')
    else:
        coffeearr.append('null')

    # Filter by
    df3 = df2[df2.primary_category.str.lower().str.contains("|".join(coffeearr))]

    df3 = df3[['Store_Name', 'Price', 'Rating','primary_category']]

    return df3



def createChart(data):
    """
        Function to create chart using data set loaded previously into set Altair/Vega-Lite Format
    """

    barType = alt.Chart(data) \
                    .mark_bar(stroke="Black") \
                    .encode(
                        alt.Y("primary_category:N",
                              sort=alt.SortField(field='primary_category', op='count', order='descending'),
                              axis=alt.Axis(title="Coffee Shop Type")
                             ),

                        alt.Color('primary_category:N',
                            legend=alt.Legend(title='Coffee Shops'),
                            scale=alt.Scale(
                                domain=list(['strictly_coffee', 'chain', 'bakeries', 'breakfast_and_brunch','diner',
                                             'deli','ice_cream_and_froyo','juice_and_smoothie','other']),
                                scheme='tableau10'
                            ),
                        ),

                        alt.X("count()", axis=alt.Axis(title="Number of Coffee Shops"),
                                     ),
                ).properties(
                    height=450,
                    width=200
                )


    barRatings = alt.Chart(data) \
                        .mark_bar(stroke="Black", fill="silver") \
                        .encode(
                            alt.X('Rating:O',
                                axis=alt.Axis(title='Rating'),
                                scale=alt.Scale(type='band', domain=list(np.arange(0,5.5,0.5))),
                            ),
                            alt.Y("count()", axis=alt.Axis(title="Number of Coffee Shops per Rating"),
                                     ),
                    ).properties(
                        width = 200,
                        height=200,
                    )


    barCost = alt.Chart(data) \
                        .mark_bar(stroke="Black", fill="Silver") \
                        .encode(
                            alt.X('Price:N',
                                axis=alt.Axis(title='Price'),
                                scale=alt.Scale(type='band', domain=['$','$$','$$$','$$$$'])
                            ),
                            alt.Y("count()", axis=alt.Axis(title="Number of Coffee Shops per Price"),
                                     ),
                    ).properties(
                        width = 200,
                        height=200,
                    )

    rightside = alt.vconcat(barRatings, barCost)



    return alt.hconcat(barType, rightside,
        data=data
    )
