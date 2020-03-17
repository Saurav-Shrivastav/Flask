from flask import Flask, render_template        #importing the Flask class from the flask library

app = Flask(__name__)           #instantiaiting the "app" object of the Flask class where __name__ is a specal variable. The __name__variable is assigned the name __main__ when the script runs.

@app.route('/')                    #Decorator
def home():
    return render_template("home.html")

@app.route('/about/')                    #Decorator
def about():
    return render_template("about.html")

if __name__=="__main__":            #It is true and thus the run statement is executed.
    app.run(debug=True)
