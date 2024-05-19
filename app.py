from flask import Flask, render_template, request, redirect, url_for
import os

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
        {'guide_name': 'Как играть в бравл старс', 'author_name': 'John Doe', 'game_name': 'Бравл старс', 'description': 'Описание гайда для игры Бравл Старс'},
        {'guide_name': 'Как играть в майнкрафт', 'author_name': 'Jane Smith', 'game_name': 'Майнкрафт', 'description': 'Описание гайда для игры Майнкрафт'},
        {'guide_name': 'Как играть в роблокс', 'author_name': 'Alex Johnson', 'game_name': 'Роблокс', 'description': 'Описание гайда для игры Роблокс'}
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
        guide_title = request.form.get('guide_title')
        game_name = request.form.get('game_name')
        author_name = request.form.get('author_name')
        description = request.form.get('description')
        
        if guide_title and game_name and author_name and description:
            guide_file_name = f"{guide_title}.txt"
            file_path = os.path.join('Save_guides', guide_file_name)
            
            with open(file_path, 'w') as file:
                file.write(f"Game Name: {game_name}\n")
                file.write(f"Author Name: {author_name}\n")
                file.write(f"Description: {description}\n")
                file.write("Guide Content:\n")
                file.write(guide_content)
            
            return redirect(url_for('home'))
    
    return render_template('add_guide.html')

if (__name__) == '__main__':

    app.run(debug=True)