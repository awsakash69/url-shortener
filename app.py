from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

urls = {}

def generate_short():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_code = generate_short()
        urls[short_code] = long_url
        short_url = request.host_url + short_code
    return render_template('index.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_url(short_code):
    long_url = urls.get(short_code)
    if long_url:
        return redirect(long_url)
    return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)
