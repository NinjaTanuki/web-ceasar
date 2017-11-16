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
                background-color: #eeeeee;
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
            <input name="rotate" type="text" value="0"></input>
        </label>
        <textarea name="message" type="text">{0}</textarea>
        <input type="submit"></input>
       </form> 
        
    </body>
</html>
"""

@app.route('/', methods=['POST'])
def encryption():
    rot = int(request.form['rotate'])
    text = request.form['message']


    return form.format(encrypt(text,rot))

@app.route('/')
def index(): 
    return form.format("")

app.run() 
