from flask import Flask, flash, redirect, render_template, \
     request, url_for, redirect
from models.config import session
from sqlalchemy import *
import models.config as models
import datetime
import json

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
user_id = 873246

@app.route('/')
def index():
   data_lq = session.query(models.Nicks).filter(models.Nicks.status == 'Đang bán', models.Nicks.game_name == 'Liên Quân').limit(6).all()
   data_nr = session.query(models.Nicks).filter(models.Nicks.status == 'Đang bán', models.Nicks.game_name == 'Ngọc Rồng').limit(8).all()
   return render_template(
      'web/index.html',
      data_lq=data_lq,
      data_nr=data_nr
   )

@app.route('/list-nick')
def list_nick():
   game_name = request.args.get("game", None)
   page_size = 12
   if game_name:
      data = session.query(models.Nicks).filter(models.Nicks.game_name == game_name, models.Nicks.status == 'Đang bán').limit(page_size).all()
   else:
      data = session.query(models.Nicks).filter(models.Nicks.status == 'Đang bán').limit(page_size).all()
   return render_template(
      'web/list.html',
      data=data
   )

@app.route('/nick-detail')
def nick_detail():
   code = request.args.get("code")
   id = request.args.get("id")
   data = session.query(models.Nicks).filter(models.Nicks.code == code, models.Nicks.id == id).first()
   return render_template(
      'web/detail-nick.html',
      data=data
   )

@app.route('/recharge-card')
def recharge_card():
   return render_template('web/nap-the.html')

@app.route('/support')
def support():
   return render_template('web/support.html')

@app.route('/profile')
def profile():
   page_size = 12
   data = session.query(models.Nicks).filter(models.Nicks.user_id == user_id).all()
   return render_template(
      'web/profile.html',
      data=data
   )

@app.route('/login')
def login():
   return render_template('web/login.html')

@app.route('/login_fb')
def login_fb():
   return render_template('web/login_fb.html')

# ================= Web admin ================= #

@app.route('/add-nick', methods=['POST'])
def add_nick():
   # try:
   name = request.form.get('name')
   price = request.form.get('price')
   game_type = request.form.get('gameType')
   images = request.files['files']
   # if game_type=='LQ':
   game_name = 'Liên Quân'
   game_id = 1
   data = {
      "rank": request.form.get('rank'),
      "tuong": request.form.get('slTuong'),
      "ngoc": request.form.get('ngoc'),
      "da_quy": request.form.get('daQuy')
   }
   nick = models.Nicks()
   nick.name = name
   nick.price = price
   nick.status = 'Confirm'
   nick.game_name = game_name
   nick.game_info = json.dumps(data)
   nick.code = 'LQ-098754'
   nick.create_at = str(datetime.datetime.now())
   nick.images = ''
   nick.game_id = game_id
   nick.user_id = user_id
   session.add(nick)
   session.commit()
   session.close()

   flash('Đăng ký bán nick thành công!')  
   # except Exception as e:
   #    flash(e)
   #    flash('Hệ thống lỗi, nhờ báo cáo sự cố với bộ phận kỹ thuật.')
   return redirect("/profile")

if __name__ == '__main__':
   app.run(debug = True)