from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_word():
    return render_template('home.html')

# @app.route('/')
# def hello_word():
#     return render_template('index.html', content='Long', hlong=['long1','long2','long3'])

# @app.route('/admin')
# def hello_admin():
#     return f"<h1>Hello admin </h1>"

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    return f"<h1>Hello {name} </h1>"

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        if name: 
            return redirect(url_for('hello_user', name=name))
    return render_template('login.html')

# @app.route('/blog/<int:blog_id>')
# def blog(blog_id):
#     return f"<h1>Blog {blog_id} </h1>"

if __name__=='__main__':
    app.run(debug=True)