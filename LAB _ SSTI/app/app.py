from flask import Flask, request, render_template, render_template_string,redirect, url_for, session
import subprocess

app = Flask(__name__)
app.secret_key = 'My@supersecret263636!'  

# Simple user database for demonstration
users = {
    'admin@app.com': 'mot2pass'
}

# Initialize a list to store messages
messages = []

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if users.get(username) == password:
            session['username'] = username  # Set the session
            return redirect(url_for('dashboard'))
        else:
            return render_template('index.html', message='Invalid credentials!')
    
    return render_template('index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('index'))  # Redirect to login if not authenticated

    if request.method == 'POST':
        new_message = request.form.get('message')
        if new_message and  not ('bash' in new_message or 'sh' in new_message):
            messages.append(new_message)
        return redirect(url_for('dashboard'))

    return render_template('dashboard.html', messages=messages, render_template_string=render_template_string)

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the user from session
    return redirect(url_for('index'))


@app.route('/thingstodo')
def thingstodo():
    return '''
        <html>
        <head><title>Things To Do</title></head>
        <body>
            <h1>Things To Do</h1>
            <ul>
                <li>Add a rate limit</li>
                <li>Add a documentation</li>
                <li>...</li>
            </ul>
        </body>
        </html>
    '''

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
