from flask import Flask, Response
from createChart import LoadData, createChart

app = Flask(__name__, static_url_path='', static_folder='.')
app.add_url_rule('/', 'root', lambda: app.send_static_file('Index.html'))

@app.route('/vis/<city>/<int:rating>/<lowcost>/<medcost>/<hicost>/<hihicost>/<strictly_coffee>/<chain>/<bakeries>/<breakfast_and_brunch>/<diner>/<deli>/<icecream>/<juice>/<other>')
def visualize(city, rating, lowcost, medcost, hicost, hihicost, strictly_coffee, chain, bakeries, breakfast_and_brunch, diner, deli, icecream, juice, other):

    response = ''



    data = LoadData(city, rating, lowcost, medcost, hicost, hihicost, strictly_coffee, chain, bakeries, breakfast_and_brunch, diner, deli, icecream, juice, other)

    if data is not None:
         response = createChart(data).to_json()

    return Response(response,
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )

if __name__ == '__main__':
    app.run(port=8002)