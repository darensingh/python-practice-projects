from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

logins = {'darren':{'email':'darren@gmail.com', 'password':'1234'},
          'jash':{'email':'jash@gmail.com', 'password':'1234'},
           'rubi':{'email':'rubi@gmail.com', 'password':'1234'}
           }


@app.route('/login', methods=['POST'])
def login():
    form_data = request.form
    user_details = {}

    try:
        user_details = logins[form_data['username']]
    except:
        message = '⚠️ Incorrect username, email, password. Try again'
        return render_template('fail.html', message=message)

    if form_data['email'] == user_details['email'] and form_data['password'] == user_details['password']:
        message = '✅ You\'re logged in'
        return render_template('success.html', message=message, username = form_data['username']).capitalize()
    else:
        message = '⚠️ Incorrect username, email, password. Try again'
        return render_template('fail.html', message=message)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)