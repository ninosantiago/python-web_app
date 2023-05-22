# create web server using flask
import flask

# create a new web app
app = flask.Flask(__name__)

# define a function to be run when the root URL is requested
@app.route("/")
def hello():
    return "Hello World!"

# create POST endpoint for /echo
@app.route("/echo", methods=["POST"])
def echo():
    # parse payload
    payload = flask.request.json
    # parse val1 and val2 if they exist
    val1 = payload.get("val1", None)
    val2 = payload.get("val2", None)

    # define hasVal1 and hasVal2
    hasVal1 = val1 is not None
    hasVal2 = val2 is not None

    # compose json output
    output = {"postedPayload": payload, "hasVal1": hasVal1, "hasVal2": hasVal2}

    return flask.jsonify(output)

# create api error if route is not found
@app.errorhandler(404)
def page_not_found(e):
    return "404 - Page not found", 404

# create api error if method is not allowed
@app.errorhandler(405)
def method_not_allowed(e):
    return "405 - Method not allowed", 405

# create api error if forbidden
@app.errorhandler(403)
def forbidden(e):
    return "403 - Forbidden", 403

# run the app
app.run(debug=True)

