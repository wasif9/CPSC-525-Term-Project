from flask import Flask, request, render_template, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Mock database
users = ['admin', 'user1', 'user2']

@app.route('/')
def index():
    if 'username' in session:
        return f"Welcome, {session['username']}! <a href='/logout'>Logout</a>"
    return "You are not logged in. <a href='/login'>Login</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('admin'))
    return render_template('login.html')

@app.route('/admin')
def admin():
    if 'username' in session:
        return render_template('admin.html', users=users)
    return redirect(url_for('login'))

@app.route('/delete_user', methods=['POST'])
def delete_user():
    if 'username' in session and session['username'] == 'admin':
        user_to_delete = request.form['user']
        users.remove(user_to_delete)
        return f"User {user_to_delete} deleted."
    return "Unauthorized", 403

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
