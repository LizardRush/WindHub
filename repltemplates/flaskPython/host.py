from flask import Flask, render_template_string

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template_string('<h1>Welcome to the Website Host</h1>')

if __name__ == '__main__':
    app.run(debug=True)
