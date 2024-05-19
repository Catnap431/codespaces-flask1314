from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a list to store the guides
guides = []


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/guides', methods=['GET', 'POST'])
def guides():
    if request.method == 'POST':
        # Get the form data
        guide_name = request.form['guide_name']
        guide_content = request.form['guide_content']
        
        # Save the guide to the list or database
        guides.append({'name': guide_name, 'content': guide_content})
        
        # Redirect back to the guides page
        return redirect(url_for('guides'))
    else:
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