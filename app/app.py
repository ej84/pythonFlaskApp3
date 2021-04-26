from flask import Flask, make_response, request, jsonify, Markup


# Create Flask's `app` object
app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    hello = "Hello World!"
    my_dict = {'key': 'dictionary value'}
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(hello, my_dict, headers), 200, headers)


if __name__ == '__main__':
    app.run(debug=False)