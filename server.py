from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    
    return render_template("waylo_sop.html")

if __name__ == "__main__":
  #host = '192.168.0.5'
  #app.run(host=host, debug=True, use_reloader=False)
  app.run(debug=True, use_reloader=False)