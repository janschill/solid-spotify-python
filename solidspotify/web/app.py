from flask import Flask, render_template

from solidspotify.modules.solid.client import client
print(client)
# from models.track import Track

# track = Track()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='Index')
