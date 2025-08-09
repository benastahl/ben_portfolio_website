from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/links')
def links():
    return render_template('links.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')


if __name__ == '__main__':
    app.run(debug=True, port=8888)
