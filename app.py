from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>سلام! این سایت mass هست 😎</h1>'

@app.route('/about')
def about():
    return '<p>درباره‌ی ما: این یه سایت ساده با Flask و Render هست.</p>'

if __name__ == '__main__':
    app.run()
