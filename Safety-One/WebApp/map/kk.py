from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '<Your mail address>'
app.config['MAIL_PASSWORD'] = '<Your password>'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


def maill(recp_list,final_msg):
	msg = Message('From safety-one', sender ='<Your mail address>' , recipients = recp_list)
	msg.body = final_msg
	mail.send(msg)
	return "Sent"
