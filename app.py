from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

# Set up the application context
app.app_context().push()

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'URL({self.long_url}, {self.short_url})'

def generate_short_url():
    characters = string.digits + string.ascii_letters
    short_url = ''.join(random.choices(characters, k=6))
    existing_url = URL.query.filter_by(short_url=short_url).first()
    if existing_url:
        return generate_short_url()
    return short_url

@app.route('/', methods=['GET', 'POST'])
def home():
    total_urls = URL.query.count()
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = generate_short_url()
        new_url = URL(long_url=long_url, short_url=short_url)
        db.session.add(new_url)
        db.session.commit()
        return render_template('home.html', short_url=short_url)
    return render_template('home.html',
    total_urls=total_urls)

@app.route('/<short_url>')
def redirect_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first()
    if url:
        return redirect(url.long_url)
    else:
        return render_template('error.html', error='URL not found')

if __name__ == '__main__':
    app.run(debug=True)