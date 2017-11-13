from flask import Flask, redirect, request
from Caesar import encrypt
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
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
      <form method='POST'>
        <label>Rotate by:
            <input name="rotate" type="text" />
        </label>
        <textarea id="text"name="message" type="text">{0}</textarea>
        <input type="submit"/>
       </form> 
        
    </body>
</html>
"""


@app.route('/')
def index(): 

    return form.format()

@app.route('/', methods=['POST'])
def encryption():
    rot = int(request.form['rotate'])
    text = request.form['message']

    return '<h1>' + encrypt(text,rot) + '</h1>'

app.run() 
