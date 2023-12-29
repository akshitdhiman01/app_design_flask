from flask import Flask,render_template,request,flash,redirect,url_for

app = Flask(__name__)
app.secret_key = "mockup_design"
toggle = True #To toggle between the main and goofy file

@app.route("/clickbait", methods=["POST","GET"])
def index():
    global toggle
    if toggle:
        if request.method == "POST":
            keywords = request.form.get("user_input")
            flash("The keywords are: " + keywords)
            return redirect(url_for("index"))
        else:
            flash("Use Keywords*")
            flash("*Gives better results with keywords")
        return render_template("main.html")
    else:
        return render_template("goofy.html")

@app.route("/toggle", methods=["POST","GET"])
def toggle_template():
    global toggle
    toggle = not toggle
    return redirect(url_for("index"))
    

