from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>
<html>
    <head>
        <title>Web Caesar - Marco Torrente</title>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }

        </style>
    </head>
    <body>
        <form action="/caesar" method="POST">
            <div>
                <label for="rot">Rotate by: <input type="text" name="rot" value="0"></label>
            </div>    
            <textarea class="text" name="text"></textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>

"""

encrypted_text = """
<!DOCTYPE html>
<html>
    <head>
        <title>Web Caesar - Marco Torrente</title>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}

        </style>
    </head>
    <body>
        <form action="/caesar" method="POST">
            <div>
                <label for="rot">Rotate by: <input type="text" name="rot" value="0"></label>
            </div>    
            <textarea class="text" name="text">{text1:s}</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>

"""

answer = """
<!DOCTYPE html>
<html>
    <head>
        <title>
        </title>
    </head>
    <body>
        <h1>Code {text1:s}</h1>
    </body>
</html>

"""

@app.route("/")
def index():
    return form

@app.route("/caesar", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = int(request.form['rot'])
    text1 = rotate_string(text,rot)
    return encrypted_text.format(text1=text1)

app.run()