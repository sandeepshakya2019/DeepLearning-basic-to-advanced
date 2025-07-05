from flask import Flask, render_template, request

app = Flask(__name__)

# GET route for home page
@app.route("/", methods=["GET", "POST"])
def index():
    print(request)
    return render_template("index.html", email="Sandeep")

# GET route for /ml-model
@app.route("/ml-model", methods=["GET", "POST"])
def ml_model():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        # data = dict(request.form)
        email = request.form.get("email")
        password = request.form.get("password")
        return f"email : {email} and password is : {password}"
    return

if __name__ == "__main__":
    app.run(debug=True)
