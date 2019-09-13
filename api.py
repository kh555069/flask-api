from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def template():
    html_string = """
    <center>
      </br>
      <h1>Hellooooo World ~!</h1>
      </br>
      <form method="POST">
        <input name="name" placeholder="your name">
        </br>
        </br>
        <input type="submit">
      </form>
    </center>
    """
    return render_template_string(html_string)

@app.route('/', methods=['POST'])
def tmp_post():
    name = request.form.get('name')
    curl_get  = "curl -X GET http://localhost:5000/api?name=" + name
    curl_post = "curl -X POST -d '{\"name\":\"" + name + "\"}' http://localhost:5000/api"
    tmp_string = """
    <center>
      <h1>Hey, {name} </h1>
      </br>
      <div>
        <h3>Using cURL</h3>
        <p>{curl_get}<p>
        <p>{curl_post}<p>
      </div>
    </center>
    """.format( name=name , curl_get=curl_get , curl_post=curl_post )
    return render_template_string(tmp_string)

@app.route('/api', methods=['GET','POST'])
def tmp_api():
    if request.method == "GET":
        name = request.args.get("name")
        tmp_json = { "text": "Hey, {name}".format(name=name) }
        return tmp_json
    if request.method == "POST":
        name = request.get_json(force=True).get('name')
        tmp_json = { "text": "Hey, {name}".format(name=name) }
        return tmp_json

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
