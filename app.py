from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a list to store the guides
guides = []


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/guides')
def guides():
    # Retrieve guides from the database or a file
    guides = [
        {'name': 'Guide 1', 'content': 'Content for Guide 1'},
        {'name': 'Guide 2', 'content': 'Content for Guide 2'},
        {'name': 'Guide 3', 'content': 'Content for Guide 3'}
    ]
    
    return render_template('guides.html', guides=guides)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Perform authentication here
        
        if username == 'admin' and password == 'password':
            # Authentication successful
            return render_template('index.html')  # Redirect to the home page
        else:
            # Authentication failed
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/add_guide', methods=['GET', 'POST'])
def add_guide():
    if request.method == 'POST':
        file = request.files['file']
        file.save('path/to/save/file/' + file.filename)
        return redirect(url_for('home'))
    return render_template('add_guide.html')
if (__name__) == '__main__':

    app.run(debug=True)