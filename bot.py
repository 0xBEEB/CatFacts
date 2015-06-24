from flask import Flask, request, redirect
from models import Message, User, db
from twilio.rest import TwilioRestClient
import twilio.twiml

SID = "SECRED_ID_FROM_TWILIO"
AUTH_TOKEN = "AUTH_TOKEN_FROM_TWILLIO"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://heroku_mysql_instance"

db.init_app(app)

client = TwilioRestClient(SID, AUTH_TOKEN)

def send_sms(msg, to):
    """Sends sms messages to a given number."""
    message = client.messages.create(body=msg,
                                     from_=TWILIO_NUMBER,
                                     to=to)

def send_all(msg):
    """Sends an sms message to all registered users"""
    for user in User.query.all():
        send_sms(msg, user.phone_number)

@app.route("/", methods=['GET', 'POST'])
def message_recieved():
    """Handle a new message recieved."""

    msg = Message(request.values)
    command = None
    message = ""

    if msg is None or msg.from_number is None:
        resp = twilio.twiml.Response()
        resp.message("We couldn't read your phone number.")

        return str(resp)

    user = User.query.filter_by(phone_number=msg.from_number).first()

    if msg.body is not None:
        command = msg.body.split(" ")[0]
    if command is not None and command.lower() == 'stop':
        if user is not None:
            db.session.delete(user)
            db.session.commit()
            message = "You will no longer receive updates from Cat Facts. To restart updates please text us back."
    if command is not None and command.lower() == 'secretmeow':
        cat_message = msg.body.split(" ", 1)[1]
        send_all(cat_message)
        message = "Your message has been sent >:D"
    else:
        if user is None:
            user = User(msg.from_number)
            db.session.add(user)
            db.session.commit()
        message = "Welcome to Cat Facts! SMS rates may apply. Text 'STOP' to no longer receive updates."

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
