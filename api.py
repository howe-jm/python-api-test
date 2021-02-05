import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return "<h1>Test test test</h1><p>This is only a test</p>"


app.run()