from flask import Flask, render_template


app = Flask('pub_flask') #can be renamed once uploaded online

#---Dashboard

@app.route('/')
def dashboard():
    return render_template("dashboard.html")

#---Map Page

@app.route('/map')
def map_of_london_pubs():
    return render_template("map.html")

#---Bar Chart Page

@app.route('/bar-chart')
def pubchart():
    return render_template("bar_chart.html")

#--- Pie Chart Page

@app.route('/pie-chart')
def pie_chart():
   return render_template("pie_chart.html")

#Pie Chart Page

app.run(debug=True)
