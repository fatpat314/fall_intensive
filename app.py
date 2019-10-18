from flask import Flask, render_template, redirect, request, url_for
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

#from data import Articles

#client = MongoClient(os.environ['MONGODB_URI'])
if 'MONGODB_URI' in os.environ.keys():
    client = MongoClient(os.environ['MONGODB_URI'])
else:
    client = MongoClient()

# db = client['void']

comments = db.comments

# client = MongoClient()
# db = client.Comments
# comments = db.comments

app = Flask(__name__)



@app.route('/')
def index():
    """Show all playlists."""
    comment = comments.find().sort([('_id', pymongo.DESCENDING)]) # possible issue with pymongo when opening heroku

    return render_template('home.html', comment=comment)
#show comments

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

#post comments
@app.route('/home/comments', methods=['POST'])
def comments_new():
    """Submit a new comment"""
    comment={
        'content': request.form.get('content'),

    }
    # print(comment)
    comments.insert_one(comment).inserted_id

    return redirect(url_for('index'))
# Edit link
@app.route('/comments/<comment_id>/edit')
def comments_edit(comment_id):
    """Show the edit form"""
    comment = comments.find_one({'_id': ObjectId(comment_id)})
    return render_template('comments_edit.html', comment=comment)

#Delete link
@app.route('/home/<comment_id>/delete', methods=['POST'])
def comments_delete(comment_id):
    """ Delete one comment"""
    comments.delete_one({'_id': ObjectId(comment_id)})
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
