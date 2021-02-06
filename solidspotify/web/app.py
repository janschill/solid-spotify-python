from flask import Flask, render_template
from solidspotify.util.enums.http import HTTPMethod

from solidspotify.modules.solid.client import client
response = client.fetch('http://localhost:3000')
print(response)

put_response = client.fetch('http://localhost:3000/test/test.ttl',
                            method=HTTPMethod.PUT, body='<ex:s> <ex:p> <ex:o>.')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='Index')
