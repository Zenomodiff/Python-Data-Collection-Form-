from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Function to generate a text file and append contact information
def generate_text_file(landline, mobile, name, address):
    text_file = "contact_info.txt"
    with open(text_file, "a") as f:
        f.write(f"Landline: {landline}\n")
        f.write(f"Mobile: {mobile}\n")
        f.write(f"Name: {name}\n")
        f.write(f"Address: {address}\n")
        f.write("-" * 20 + "\n")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        landline = request.form['landline']
        mobile = request.form['mobile']
        name = request.form['name']
        address = request.form['address']
        
        # Print the submitted information
        print(f"Landline: {landline}")
        print(f"Mobile: {mobile}")
        print(f"Name: {name}")
        print(f"Address: {address}")
        
        # Save submitted information to a text file
        generate_text_file(landline, mobile, name, address)
        
        return "Form submitted successfully and appended to text file!"

if __name__ == '__main__':
    app.run(debug=True)
