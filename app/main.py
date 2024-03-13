import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv() # load the data form env file
app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1> Hello Home </h1>'

# commet added

@app.route('/<random_string>')
def reversed_random_string(random_string):
    return ''.join(reversed(random_string))

@app.route('/get-env')
def get_env():
    return os.environ.get("MODE")

if __name__ == '__main__':
    app.run(debug=True, port=4040)
