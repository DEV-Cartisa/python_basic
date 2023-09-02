from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():#coding the pages - the home page [ will be functions ]
    return "This is the main page"

@app.route("/<name>") # within <>, it will pass , whatever name , into function ,pass as parameter mor dynm
def user(name):
    return f"Hello {name}"
    #Hello home , when /home

#redirect , when access level not met , by user 
@app.route("/admin")
def admin():
    return redirect(url_for("home"))#where to redirect , not /home. at object

if __name__ == "__main__":
    app.run()

















