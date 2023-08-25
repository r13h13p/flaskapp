import random
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask import Flask, render_template, request, redirect  # Import the redirect function

import socket
socket.getaddrinfo('smtp.gmail.com', 587)

app = Flask(__name__)

# Configure Flask Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Change to your SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'devopsstudyhub@gmail.com'
app.config['MAIL_PASSWORD'] = 'cinigbrxzkyisrti'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# Placeholder for generated OTP
generated_otp = None

# Welcome page route
@app.route('/', methods=['GET'])
def welcome():
    return render_template('index.html')

# Registration page route
@app.route('/register', methods=['GET', 'POST'])
def register():
    global generated_otp

    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']

        # Generate OTP and send it via email
        generated_otp = str(random.randint(1000, 9999))
        msg_to_user = Message('OTP Verification', sender='your_email@gmail.com', recipients=[email])
        msg_to_user.body = f'Your OTP is: {generated_otp}'
        mail.send(msg_to_user)

        # Redirect to the OTP verification page
        return redirect('/verify')  # Redirect to the /verify route

    return render_template('register.html', message="")

# New route for OTP verification page
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        user_otp = request.form['otp']
        if user_otp == generated_otp:
            return "OTP verification successful!"
        else:
            return "Incorrect OTP. Please try again."

    return render_template('verify.html')  # Render the verify.html template




if __name__ == '__main__':
    app.run(debug=True)
