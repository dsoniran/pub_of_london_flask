# Pubs of London
<br/>
A team project for the Introduction to Python Programming course hosted Code First Girls sponsored by Bank of America.<br/>
<br/>
from flask import Flask, render_template <br/>
<br/>
app = Flask('pub_flask') #can be renamed once uploaded online<br/>
<br/>
@app.route('/') def map_of_london_pubs(): return render_template("pubs_of_london.html")<br/>
<br/>
if pub_flask == "main": app.run(debug=False, host = '0.0.0.0')<br/>
