from flask import Flask, flash, redirect, render_template, \
     request, url_for, redirect
from models.config import session
from sqlalchemy import *
import models.config as models
import datetime
import json
from flask_login import LoginManager, login_required, logout_user, current_user, login_user

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
user_id = 3
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/')
def index():
   data_lq = session.query(models.Nicks).filter(models.Nicks.status == 'Đang bán', models.Nicks.game_name == 'Liên Quân').limit(6).all()
   data_nr = session.query(models.Nicks).filter(models.Nicks.status == 'Đang bán', models.Nicks.game_name == 'Ngọc Rồng').limit(8).all()
   return render_template(
      'web/index.html',
      data_lq=data_lq,
      data_nr=data_nr,
      user=current_user
   )

@app.route('/list-nick')
def list_nick():
   game_name = request.args.get("game", None)
   price = request.args.get("price", None)
   code = request.args.get("find", None)
   page_size = 12
   
   if game_name:
      data = session.query(models.Nicks).filter(models.Nicks.game_name == game_name, models.Nicks.status == 'Đang bán')
   else:
      data = session.query(models.Nicks).filter(models.Nicks.status == 'Đang bán')
   
   if code:
      data = data.filter(models.Nicks.code == code)

   if price:
      price_cv = list(price.split(","))
      price1 = None
      price2 = None
      if len(price_cv) > 1:
         price1 = int(price_cv[0])
         price2 = int(price_cv[1])
         data = data.filter(models.Nicks.price > price1)
         data = data.filter(models.Nicks.price <= price2)
      elif int(price) == 1000000:
         data = data.filter(models.Nicks.price > int(price))
      else:
         data = data.filter(models.Nicks.price <= int(price))
   data = data.limit(page_size)
   data = data.all()
   return render_template(
      'web/list.html',
      data=data,
      game_name=game_name,
      price=price,
      code=code
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
   data_qr = session.query(models.History).filter(models.History.user_id == user_id).all()
   data = []
   for d in data_qr:
      rd = {
         "id": d.id,
         "card": d.card,
         "buy": d.buy,
         "info": json.loads(d.info),
      }
      data.append(rd)
   return render_template(
      'web/profile.html',
      data=data
   )

# ================= Login ================= #

@app.route('/sign_up')
def sign_up():
   return render_template('web/sign_up.html')

@app.route('/sign_up', methods=['POST'])
def sign_up_process():
   try:
      name = request.form.get("name")
      account = request.form.get("account")
      password = request.form.get("password")
      confirm_password = request.form.get("confirm_password")
      user = session.query(models.Users).filter(
         models.Users.account_tk == account).first()
      if user:
         flash('Tên tài khoản đã tồn tại')
         return redirect("/sign_up")
      user = models.Users()
      user.name = name
      user.account_tk = account
      user.super = False
      user.ctv = False
      user.enduser = True
      user.create_at = str(datetime.datetime.now())
      user.password = password
      user.money = 0
      session.add(user)
      session.commit()
      session.close()
      flash('Tạo tài khoản "'+ name +'" thành công!')
   except Exception as e:
      flash('Hệ thống lỗi, nhờ báo cáo sự cố với bộ phận kỹ thuật.')
      return redirect("/sign_up")
   return redirect("/login")

@app.route('/login')
def login():
   return render_template('web/login.html')

@login_manager.user_loader
def load_user(user_id):
   return session.query(models.Users).filter(
      models.Users.id == user_id).first()

@app.route('/login', methods=['POST'])
def login_process():
   try:
      username = request.form.get("username")
      password = request.form.get("password")
      user = session.query(models.Users).filter(
         models.Users.account_tk == username,
         models.Users.password == password).first()
      if user:
         login_user(user)
      else:
         flash('Mật khẩu không chính xác')
         return redirect("/login")
   except Exception as e:
      flash('Hệ thống lỗi, nhờ báo cáo sự cố với bộ phận kỹ thuật.')
      return redirect("/login")
   return redirect("/")

@app.route("/logout")
def logout():
   logout_user()
   return redirect('/')

# ================= Web admin ================= #
def checkPermisson():
   if current_user.super:
      return 'admin'
   elif current_user.ctv:
      return 'ctv'
   else:
      return False

@app.route('/login-admin')
def login_admin():
   return render_template('admin/login.html')

@app.route('/login-admin', methods=['POST'])
def login_admin_process():
   try:
      username = request.form.get("username")
      password = request.form.get("password")
      user = session.query(models.Users).filter(
         models.Users.account_tk == username,
         models.Users.password == password).first()
      if user:
         login_user(user)
         per = checkPermisson()
         if not per:
            logout_user()
            return redirect("/")
      else:
         flash('Mật khẩu không chính xác')
         return redirect("/login-admin")
   except Exception as e:
      flash('Hệ thống lỗi, nhờ báo cáo sự cố với bộ phận kỹ thuật.')
      return redirect("/login-admin")
   return redirect("/admin")

@app.route('/admin')
@login_required
def admin():
   per = checkPermisson()
   if per == 'admin':
      nicks_qr = session.query(models.Nicks).all()

      # Get info nicks
      sold = []
      on_sale = []
      nicks = []
      for nick in nicks_qr:
         if nick.status == 'Đang bán':
            on_sale.append(nick)
         if nick.status == 'Đã bán':
            sold.append(nick)

         # Convert nicks data
         user = session.query(models.Users).filter(models.Users.id == nick.user_id).first()
         data = {
            "id": nick.id,
            "code": nick.code,
            "name": nick.name,
            "game_name": nick.game_name,
            "price": nick.price,
            "user": { "name": user.name, "id": user.id },
            "status": nick.status
         }
         nicks.append(data)

      # Get info users
      ctv = []
      enduser = []
      users = []
      users_qr = session.query(models.Users).filter(models.Users.super == False).all()
      for user in users_qr:
         if user.ctv:
            ctv.append(user)
         elif user.enduser:
            enduser.append(user)
         
         # Convert users data
         # list_request = session.query(models.History).filter(
         #    models.History.user_id == user.id, models.History.status == "Confirm").all()
         # list_nick = session.query(models.Nicks).filter(models.Nicks.user_id == user.id).all()
         # data = {
         #    "id": user.id,
         #    "name": user.name,
         #    "ctv": user.ctv,
         #    "nick_sale": len(list_nick),
         #    "money": user.money,
         #    "request": len(list_request)
         # }
      
      return render_template(
         'admin/admin.html',
         nicks=nicks,
         sold=sold,
         on_sale=on_sale,
         ctv=ctv,
         enduser=enduser)
   elif per == 'ctv':
      nicks_qr = session.query(models.Nicks).filter(models.Nicks.user_id == current_user.id).all()
      # Get info nicks
      sold = []
      on_sale = []
      nicks = []
      for nick in nicks_qr:
         if nick.status == 'Đang bán':
            on_sale.append(nick)
         if nick.status == 'Đã bán':
            sold.append(nick)

         # Convert nicks data
         user = session.query(models.Users).filter(models.Users.id == nick.user_id).first()
         data = {
            "id": nick.id,
            "code": nick.code,
            "name": nick.name,
            "game_name": nick.game_name,
            "price": nick.price,
            "user": { "name": user.name, "id": user.id },
            "status": nick.status
         }
         nicks.append(data)
      return render_template(
         'admin/admin.html',
         nicks=nicks,
         sold=sold,
         on_sale=on_sale)
   else:
      return redirect("/")

@app.route('/add-nick', methods=['POST'])
def add_nick():
   try:
      name = request.form.get('name')
      price = request.form.get('price')
      game_type = request.form.get('gameType')
      images = request.files['files']
      if game_type=='LQ':
         game_name = 'Liên Quân'
         data = {
            "rank": request.form.get('rank'),
            "tuong": request.form.get('slTuong'),
            "skin": request.form.get('Skin'),
            "ngoc": request.form.get('ngoc'),
            "da_quy": request.form.get('daQuy')
         }
      else:
         game_name = 'Ngọc Rồng'
         data = {
            "nickType": request.form.get('nickType'),
            "server": request.form.get('server'),
            "hanhTinh": request.form.get('hanhTinh'),
            "bongTai": request.form.get('bongTai'),
            "deTu": request.form.get('deTu')
         }
      nick = models.Nicks()
      nick.name = name
      nick.price = price
      nick.status = 'Đang bán'
      nick.game_name = game_name
      nick.game_info = json.dumps(data)
      nick.code = 'LQ-' + str(int(datetime.datetime.utcnow().timestamp()))
      nick.create_at = str(datetime.datetime.now())
      nick.images = ''
      nick.user_id = user_id
      session.add(nick)
      session.commit()
      session.close()

      flash('Đăng ký bán nick thành công!')  
   except Exception as e:
      flash(e)
      flash('Hệ thống lỗi, nhờ báo cáo sự cố với bộ phận kỹ thuật.')
   return redirect("/admin")

@app.route('/admin-ctv')
def admin_ctv():
   # Get info nicks
   nicks_qr = session.query(models.Nicks).all()
   sold = []
   on_sale = []
   nicks = []
   for nick in nicks_qr:
      if nick.status == 'Đang bán':
         on_sale.append(nick)
      if nick.status == 'Đã bán':
         sold.append(nick)

      # Convert nicks data
      user = session.query(models.Users).filter(models.Users.id == nick.user_id).first()
      data = {
         "id": nick.id,
         "code": nick.code,
         "name": nick.name,
         "game_name": nick.game_name,
         "price": nick.price,
         "user": { "name": user.name, "id": user.id },
         "status": nick.status
      }
      nicks.append(data)

   # Get info users
   ctv = []
   enduser = []
   users = []
   users_qr = session.query(models.Users).filter(models.Users.super == False).all()
   for user in users_qr:
      if user.ctv:
         ctv.append(user)
      elif user.enduser:
         enduser.append(user)
   return render_template('admin/ctv.html', nicks=nicks, sold=sold, on_sale=on_sale, ctv=ctv, enduser=enduser)

@app.route('/add-ctv', methods=['POST'])
def add_ctv():
   try:
      name = request.form.get('name')
      account_tk = request.form.get('account_tk')
      password = request.form.get('password')
      
      user = models.Users()
      user.name = name
      user.account_tk = account_tk
      user.ctv = True
      user.super = False
      user.enduser = False
      user.password = password
      user.create_at = str(datetime.datetime.now())
      session.add(user)

      session.commit()
      session.close()

      flash('Tạo ctv thành công!')
   except Exception as e:
      flash(e)
      flash('Hệ thống lỗi, nhờ báo cáo sự cố với bộ phận kỹ thuật.')
   return redirect("/admin-ctv")

@app.route('/admin-history')
def admin_history():
   # Get info nicks
   nicks_qr = session.query(models.Nicks).all()
   sold = []
   on_sale = []
   nicks = []
   for nick in nicks_qr:
      if nick.status == 'Đang bán':
         on_sale.append(nick)
      if nick.status == 'Đã bán':
         sold.append(nick)

      # Convert nicks data
      user = session.query(models.Users).filter(models.Users.id == nick.user_id).first()
      data = {
         "id": nick.id,
         "code": nick.code,
         "name": nick.name,
         "game_name": nick.game_name,
         "price": nick.price,
         "user": { "name": user.name, "id": user.id },
         "status": nick.status
      }
      nicks.append(data)

   # Get info users
   ctv = []
   enduser = []
   users = []
   users_qr = session.query(models.Users).filter(models.Users.super == False).all()
   for user in users_qr:
      if user.ctv:
         ctv.append(user)
      elif user.enduser:
         enduser.append(user)
   return render_template('admin/ctv.html', nicks=nicks, sold=sold, on_sale=on_sale, ctv=ctv, enduser=enduser)

if __name__ == '__main__':
   app.run(debug = True)