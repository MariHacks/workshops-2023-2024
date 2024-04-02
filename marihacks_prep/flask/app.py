"""
Building a simple website that asks for the user's name and greets them
"""

# Import necessary modules from Flask
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the root URL, which handles the form where users can input their name


@app.route('/', methods=['GET'])
def ask_name():
    # When a GET request is made to the root URL, render and return the ask_name.html template
    # This template contains the form asking for the user's name
    return render_template('ask_name.html')

# Define a route for '/greet', which will handle the form submission


@app.route('/greet', methods=['POST'])
def greet():
    # Extract the 'name' value from the submitted form data
    name = request.form['name']
    # Render the greet.html template, passing the submitted 'name' to be used within the template
    # This template is responsible for displaying the personalized greeting message
    return render_template('greet.html', name=name)


# Check if the script is executed as the main program and not imported as a module in another script
if __name__ == '__main__':
    # Run the Flask application in debug mode, which provides useful error messages and auto-reloads the app on code changes
    app.run(debug=True)
