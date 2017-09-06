import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'



#this is specific to c9, do not change
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
