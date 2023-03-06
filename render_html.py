from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/government")
def government():
   return render_template("gov.html")

@app.route("/midmarket")
def midmarket():
   return render_template("mm.html")

@app.route("/channelpartners")
def channelpartners():
   return render_template("cp.html")

@app.route("/enterprise")
def enterprise():
   return render_template("enterpise.html")

@app.route("/smallbusiness")
def smallbusiness():
   return render_template("sb.html")

if __name__ == '__main__':
   app.run(debug = True)