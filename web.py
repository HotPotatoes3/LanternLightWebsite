from flask import Flask, request, render_template, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # `index.html` exists in the templates folder

'''
@app.before_request
def force_host():
    # Allowed hosts: Add any additional domains or subdomains here
    allowed_hosts

'''

if __name__ == '__main__':
    # Bind to 0.0.0.0 to make the server accessible on all network interfaces
    app.run(host="0.0.0.0", port=5000)
