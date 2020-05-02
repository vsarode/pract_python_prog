import MySQLdb
from flask import Flask, request, render_template

app = Flask(__name__)

connect = MySQLdb.connect(host='localhost', user='root', password='tiger',
                          db='user')


@app.route('/')
def say_hello():
    return render_template('login.html')


@app.route('/login')
def login():
    data = request.args

    query = 'select * from user where username=%s'

    cur = connect.cursor()
    cur.execute(query, (data['username'],))
    query_result = cur.fetchall()
    cur.close()

    if not query_result:
        return "<h1>Username  is invalid. Please enter valid username and try again !!</h1>"
    elif query_result[0][1] == data['pass']:
        return "<h1> Login successfully for user " + data[
            'username'] + "!!</h1>"
    else:
        return "<h1>Password is invalid. Please entrer valid password and try again !!</h1>"

    if data['username'] == entry[0] and data['pwd'] == 'pass':
        return "<h1> Login successfully for " + data['username'] + " !!</h1>"
    else:
        return "<h1> Login failure for " + data['username'] + " !!</h1>"


if __name__ == '__main__':
    app.run(host='localhost', port=2002, debug=True)
