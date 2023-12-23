from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage (rendering index.html)
@app.route('/')
def home():
    return render_template('index.html')

# Route to serve static files (such as CSS, JS, images)
@app.route('/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(debug=True)
