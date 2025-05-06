from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('new.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # For now, just print to console (you can store/send later)
        print(f"New contact request:\nName: {name}\nEmail: {email}\nMessage: {message}")
        
        return render_template('contact.html', success=True)
    return render_template('contact.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)
