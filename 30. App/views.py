from flask import Flask, flash, redirect, render_template, \
     request, url_for, redirect
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('web/index.html')

@app.route('/list-nick')
def list_nick():
   return render_template('web/list.html')

@app.route('/nick-detail')
def nick_detail():
   return render_template('web/detail-nick.html')

@app.route('/recharge-card')
def recharge_card():
   return render_template('web/nap-the.html')

@app.route('/support')
def support():
   return render_template('web/support.html')

@app.route('/profile')
def profile():
   return render_template('web/profile.html')

if __name__ == '__main__':
   app.run(debug = True)