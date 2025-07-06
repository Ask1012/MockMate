from flask import Flask, render_template, request, redirect, url_for
from models import db, InterviewRequest , Contact
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        domain = request.form['domain']
        language = request.form['language']
        time = request.form['time']
        new_entry = InterviewRequest(name=name, email=email, domain=domain , time=time, language=language)
        db.session.add(new_entry)
        db.session.commit()
        return render_template('index.html', message='Interview Scheduled Successfully!  We will contact you soon.')
    return render_template('index.html')

@app.route('/admin')
def admin():
    entries = InterviewRequest.query.all()
    return render_template('admin.html', entries=entries)

@app.route('/contact' , methods=['GET','POST'])
def contact():

    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        msg = request.form["msg"]

        if name and email and msg :
            contact = Contact(name=name, email=email, msg=msg)
            db.session.add(contact)
            db.session.commit()
            db.session.rollback()
            return render_template('contact.html', message='Done !')
    return render_template('contact.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
      # Render provides PORT env variable
    port = int(os.environ.get("PORT", 5000))  # ✅ Correct way to get PORT from env
    app.run(debug=True, host="0.0.0.0", port=port)
