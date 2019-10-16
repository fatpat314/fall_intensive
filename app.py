from flask import Flask, render_template
from pymongo import MongoClient
from data import Articles

#client = MongoClient()
#db = client.Playlister
#playlists = db.playlists

app = Flask(__name__)

Arts = Articles()

# @app.route('/')
# def index():
#     """Return homepage"""
#     return render_template('playlists_index.html', playlists=playlists.find)

# playlists = [
#     { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
#     { 'title': '80\'s Music', 'description': 'Don\'t stop beleving'}
# ]

@app.route('/')
def index():
    """Show all playlists."""
    return render_template('home.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Arts)

if __name__ == '__main__':
    app.run(debug=True)
