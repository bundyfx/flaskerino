from flask import Flask, render_template, url_for

app = Flask(__name__)

import json

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', images=fetch_images(), title="Flaskerino")

def fetch_images():
    images = [{
        "name": "DAMN",
        "width": 274,
        "image_path": "../static/images/fulls/01.jpg",
        "thumb_path": "../static/images/thumbs/01.jpg"
    }, {
        "name": "Sexy Flanders",
        "width": 282,
        "image_path": "../static/images/fulls/02.jpg",
        "thumb_path": "../static/images/thumbs/02.jpg"
        },
        {
        "name": "Got Milk?",
        "width": 476,
        "image_path": "../static/images/fulls/03.jpg",
        "thumb_path": "../static/images/thumbs/03.jpg"
        },
        {
        "name": "Adventure",
        "width": 232,
        "image_path": "../static/images/fulls/04.jpg",
        "thumb_path": "../static/images/thumbs/04.jpg"
    }

             ]

    return images

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title="404 Not Found"), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', title="500 Internal Error"), 500

if __name__ == '__main__':
    app.run(debug=True)


