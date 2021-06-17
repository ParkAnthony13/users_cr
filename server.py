from flask import Flask, render_template, redirect, session, request
from users import User
app = Flask(__name__)
app.secret_key = 'speak friend and enter'

@app.route('/')
def home():
    return redirect('/users')


@app.route('/users')
def users_table():
    users=User.get_all()
    print(users)
    return render_template("users.html", users = users)


@app.route('/users/new_process', methods=['POST'])
def process():
    data = {
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'email':request.form['email']
    }
    User.save(data)
    return redirect('/')


@app.route('/users/new')
def create_user():
    return render_template('/new_user.html')


if __name__ == "__main__":
    app.run(debug=True)