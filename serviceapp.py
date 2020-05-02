from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello welcome to flask !!"


@app.route('/bye')
def bye():
    return "Bye !!"

#192.168.0.124:2002/hello


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2002, debug=True)
