from flask import Flask, request
import os
import my_mail

app = Flask(__name__)

@app.route('/')
def index():
    """
    This function just responds to the browser URL
    """
    return 'Hello, World!'

@app.post('/form_submit')
def form_submit():
    """
    This function obtains post data and sends them to the user
    """
    data = dict(request.form)
    email_address = data.get('target_email')
    if email_address is None:
        return "No target email found, cannot process form.", 404

    del data['target_email']
    message = ""
    for key in data:
        message += key.title() + ": " + data[key] + "\n" + "-"*10 + "\n"

    message += "\n"*5 + "This is an automated message. Please do not reply to this email.\nBy Nalin Angrish <nalin@nalinangrish.me>"
    print("Sending email to", email_address)
    print(message)
    my_mail.send(email_address, message)
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
