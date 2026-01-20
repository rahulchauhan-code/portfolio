from flask import Flask, render_template, request, jsonify
from data.resume_data import resume
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Email configuration (update with your details)
EMAIL_ADDRESS = "rahulchauhan5004@gmail.com"
EMAIL_PASSWORD = "gcfq pwjh jwhj bjnx"  # Create at: https://myaccount.google.com/apppasswords
RECIPIENT_EMAIL = resume.get("email", "rahulchauhan5004@gmail.com")

def send_email(name, email, subject, message):
    try:
        # Email to portfolio owner
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Reply-To'] = email  # User can reply to the sender
        msg['Subject'] = f"Portfolio Contact: {subject}"
        
        body = f"""New message from your portfolio contact form:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}"""
        
        msg.attach(MIMEText(body, 'plain'))
        
        # For Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        
        # Send confirmation email to user
        user_msg = MIMEMultipart()
        user_msg['From'] = EMAIL_ADDRESS
        user_msg['To'] = email
        user_msg['Subject'] = f"Re: {subject} - Thank you for contacting me"
        
        user_body = f"""Hi {name},

Thank you for reaching out through my portfolio! I have received your message and will get back to you soon.

Your message:
"{message}"

Best regards,
{resume.get('name', 'Rahul Chauhan')}"""
        
        user_msg.attach(MIMEText(user_body, 'plain'))
        server.send_message(user_msg)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route("/")
def home():
    return render_template("home.html", resume=resume)

@app.route("/about")
def about():
    return render_template("about.html", resume=resume)

@app.route("/skills")
def skills():
    return render_template("skills.html", resume=resume)

@app.route("/projects")
def projects():
    return render_template("projects.html", resume=resume)

@app.route("/education")
def education():
    return render_template("education.html", resume=resume)

@app.route("/contact")
def contact():
    return render_template("contact.html", resume=resume)

@app.route("/send-message", methods=['POST'])
def send_message():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')
    
    if not all([name, email, subject, message]):
        return jsonify({"success": False, "message": "All fields are required"}), 400
    
    if send_email(name, email, subject, message):
        return jsonify({"success": True, "message": "Message sent successfully!"})
    else:
        return jsonify({"success": False, "message": "Failed to send message. Try again."}), 500

if __name__ == "__main__":
    app.run(debug=True)
