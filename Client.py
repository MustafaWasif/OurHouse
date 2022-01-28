
from flask import Flask, redirect, request, url_for, render_template
app = Flask(__name__)

#Purpose: To Redirect to the Signup page
@app.route("/")
def redirect_to_signup():
    return redirect(url_for("signup"))

#Purpose: To collect user input and redirect users to Signup Successful page
@app.route("/signup", methods = ["GET", "POST"])
def signup():
    user_location = "ab"
    if (request.method == "POST"):
        try:
            user_location = request.form["location"]
            print(user_location)
            return redirect(url_for("success", house = user_location))
        except:
            error_msg = "Please input valid address"
    #else:
    #    user_location = request.args.get("location")  
    #    return redirect(url_for("success", house = user_location))
    
    return render_template("Signup.html")

#Purpose: To inform users about email reminders.
@app.route("/success/<house>")
def success(house):
    return "Signup Successful! We will send email reminder before your next Collection Pickup."
    #return "Garbage Pickup for %s is on: *Date here*" %house


if __name__ == "__main__":
    app.run(debug=True)