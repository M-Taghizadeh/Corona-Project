from flask import Flask, render_template

app = Flask(__name__, static_folder="statics")

@app.route("/")
def crawl_info():
    # Step 1: Runing Spider

    # Step 2 : Read Info 

    # Step 3 : Get Plot Image
    return render_template("index.html")

