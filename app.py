from flask import Flask, render_template, redirect, request, url_for
from pymongo import MongoClient
#from data import Articles

client = MongoClient()
db = client.Comments
comments = db.comments

app = Flask(__name__)

#Arts = Articles()

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
    comment = comments.find()
    return render_template('home.html',comment=comment)

# @app.route('/articles')
# def articles():
#     return render_template('articles.html', articles = Arts)

# @app.route('/article/string:id>/')
# def articles(id):
#     return render_template('articles.html', id=id)

@app.route('/comments/all')
def comments_all():
    """Create a new comment."""
    # TODO fetch all comments and pass to template
    return render_template('comments_all.html')

@app.route('/comments/<comment_id>')
def comments_show(comment_id):
    """ Show comment"""
    comment = comments.find()
    return render_template('comments_show.html', comment=comment, comments=comments)


@app.route('/home/comments', methods=['POST'])
def comments_new():
    """Submit a new comment"""
    comment={
        'content': request.form.get('content'),
        # 'comment_id': ObjectId(request.form.get('_id'))
    }
    print(comment)
    comments.insert_one(comment).inserted_id

    return redirect(url_for('index', _id=request.form.get('_id')))

if __name__ == '__main__':
    app.run(debug=True)
