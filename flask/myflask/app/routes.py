from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Post, User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@main.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = request.form['user_id']  # Предполагаем, что ID пользователя передается
        post = Post(title=title, content=content, user_id=user_id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_post.html')


@main.route('/deletepost/<int:post_id>', methods=['POST'])
def deletepost(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.index'))
