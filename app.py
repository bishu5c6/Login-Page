from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
databases = {'bishu':'123','sam':'1234','sai':'12345','nikhil':'123456'}

@app.route('/form_login',methods=['GET','POST'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']

    if name1 not in databases:
        return render_template('index.html', info = 'Invalid_user')
    else:
        if databases[name1]!= pwd:
            return render_template('index.html', info = 'Invalid_password')
        else:
            return render_template('results.html', name=name1)


if __name__ == '__main__':
    app.run(debug=True)



































































'''
        input[type=text] {
                padding : 12px;
                border: 1px solid black;
                border-radius: 4px;
                background-color: beige;
                color: black;
                font-weight: bold;
            }
'''