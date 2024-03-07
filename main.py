from flask_cors import CORS
from flask import Flask,render_template, request




app = Flask(__name__)
CORS(app)  # Enable CORS for all routes



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/urlpredict', methods=['POST'])
def urlpredict():

    return render_template('index.html' , url_result = 'Pass')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
