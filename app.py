from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'suryashivakumar005@gmail.com'
app.config['MAIL_PASSWORD'] = '12345'  

mail = Mail(app)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(f"New contact from {name}",
                      sender=email,
                      recipients=['suryashivakumar005@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        mail.send(msg)

        return f"Thanks {name}, your message has been sent!"
    return render_template("contact.html")

@app.route('/about/')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
