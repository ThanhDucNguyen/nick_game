from flask import Flask, flash, redirect, render_template, \
     request, url_for, redirect
from models.config import session
from sqlalchemy import *
import models.config as models
import datetime
import json
from flask_login import LoginManager, login_required, logout_user, current_user, login_user
import common
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

PATH_DEFAULT = 'C:/Users/OS/Desktop/Data/0.Work/nickgame/nick_game/30.App/'
UPLOAD_FOLDER = 'static/nicks/'
app.config['UPLOAD_FOLDER'] = PATH_DEFAULT + UPLOAD_FOLDER

@app.route('/')
def index():
   data_lq = session.query(models.Nicks).filter(models.Nicks.status == 'Đang bán', models.Nicks.game_name == 'Liên Quân').order_by(desc(models.Nicks.id)).limit(6).all()
   data_nr = session.query(models.Nicks).filter(models.Nicks.status == 'Đang bán', models.Nicks.game_name == 'Ngọc Rồng').order_by(desc(models.Nicks.id)).limit(8).all()
   for lq in data_lq:
      if lq.images:
         list_image = lq.images.split(",")
         lq.images = list_image[0]
   for nr in data_nr:
      if nr.images:
         list_image = nr.images.split(",")
         nr.images = list_image[0]
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
      data = session.query(models.Nicks).filter(models.Nicks.game_name == game_name, models.Nicks.status == 'Đang bán').order_by(desc(models.Nicks.id))
   else:
      data = session.query(models.Nicks).filter(models.Nicks.status == 'Đang bán').order_by(desc(models.Nicks.id))
   
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
   for d in data:
      if d.images:
         list_image = d.images.split(",")
         d.images = list_image[0]
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
   list_image = data.images.split(",")
   return render_template(
      'web/detail-nick.html',
      list_image=list_image,
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
   data_qr = session.query(models.History).filter(models.History.user_id == user_id).order_by(desc(models.History.id)).all()
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

@app.route('/error')
@login_required
def error():
   return render_template('admin/404.html')  

@app.route('/admin')
@login_required
def admin():
   per = checkPermisson()
   if per == 'admin':
      nicks_qr = session.query(models.Nicks).order_by(desc(models.Nicks.id)).all()

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
            "status": nick.status,
            "game_info": json.loads(nick.game_info),
            "images": nick.images.split(",")
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
      
      return render_template(
         'admin/admin.html',
         nicks=nicks,
         sold=sold,
         on_sale=on_sale,
         ctv=ctv,
         enduser=enduser)
   elif per == 'ctv':
      nicks_qr = session.query(models.Nicks).filter(models.Nicks.user_id == current_user.id).order_by(desc(models.Nicks.id)).all()
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
         data = {
            "id": nick.id,
            "code": nick.code,
            "name": nick.name,
            "game_name": nick.game_name,
            "price": nick.price,
            "status": nick.status,
            "game_info": json.loads(nick.game_info)
         }
         nicks.append(data)
      return render_template(
         'admin/ctv-nick.html',
         nicks=nicks,
         sold=sold,
         on_sale=on_sale)
   else:
      return redirect("/404")

@app.route('/add-nick', methods=['POST'])
def add_nick():
   try:
      name = request.form.get('name')
      price = request.form.get('price')
      game_type = request.form.get('gameType')

      code = ''
      # Game Info
      if game_type=='LQ':
         code  = 'LQ-' + str(int(datetime.datetime.utcnow().timestamp()))
         game_name = 'Liên Quân'
         data = {
            "account": request.form.get('account'),
            "password": request.form.get('password'),
            "rank": request.form.get('rank'),
            "tuong": request.form.get('slTuong'),
            "skin": request.form.get('Skin'),
            "ngoc": request.form.get('ngoc'),
            "da_quy": request.form.get('daQuy')
         }
      else:
         code  = 'NR-' + str(int(datetime.datetime.utcnow().timestamp()))
         game_name = 'Ngọc Rồng'
         data = {
            "nickType": request.form.get('nickType'),
            "server": request.form.get('server'),
            "hanhTinh": request.form.get('hanhTinh'),
            "bongTai": True if request.form.get('bongTai') == 'on' else False,
            "deTu": True if request.form.get('deTu') == 'on' else False
         }

      path = app.config['UPLOAD_FOLDER'] + code
      os.mkdir(path)

      # Image
      if 'files' not in request.files:
         flash('No file part')
         return redirect("/admin")
      images = request.files.getlist('files')
      # if user does not select file, browser also
      # submit an empty part without filename
      list_image = []
      if images:
         for image in images:
            if image.filename == '':
               flash('No selected file')
               return redirect("/admin")
            file_name = common.upload_file(image, path)
            list_image.append(os.path.join(UPLOAD_FOLDER + code, image.filename))

      nick = models.Nicks()
      nick.name = name
      nick.price = price
      nick.status = 'Xác nhận'
      nick.game_name = game_name
      nick.game_info = json.dumps(data)
      nick.code = code
      nick.create_at = str(datetime.datetime.now())
      nick.images = ','.join(list_image)
      nick.user_id = current_user.id
      session.add(nick)
      session.commit()
      session.close()

      flash('Đăng ký bán nick '+ code + ' thành công!')
   except Exception as e:
      flash(e)
      flash('Hệ thống lỗi, nhờ báo cáo sự cố với bộ phận kỹ thuật.')
      redirect("/admin")
   return redirect("/admin")

@app.route('/edit-nick', methods=['POST'])
def edit_nick():
   try:
      id = request.form.get('id')
      nick = session.query(models.Nicks).filter(models.Nicks.id == id).first()
      name = request.form.get('name')
      nick.name = name
      price = request.form.get('price')
      nick.price = price
      game_type = request.form.get('gameType')

      code = ''
      # Game Info
      if game_type=='LQ':
         code  = 'LQ-' + str(int(datetime.datetime.utcnow().timestamp()))
         game_name = 'Liên Quân'
         data = {
            "account": request.form.get('account'),
            "password": request.form.get('password'),
            "rank": request.form.get('rank'),
            "tuong": request.form.get('slTuong'),
            "skin": request.form.get('Skin'),
            "ngoc": request.form.get('ngoc'),
            "da_quy": request.form.get('daQuy')
         }
      else:
         code  = 'NR-' + str(int(datetime.datetime.utcnow().timestamp()))
         game_name = 'Ngọc Rồng'
         data = {
            "nickType": request.form.get('nickType'),
            "server": request.form.get('server'),
            "hanhTinh": request.form.get('hanhTinh'),
            "bongTai": True if request.form.get('bongTai') == 'on' else False,
            "deTu": True if request.form.get('deTu') == 'on' else False
         }

      # Image
      if 'files' not in request.files:
         nick.images = nick.images
      else:
         images = request.files.getlist('files')
         # if user does not select file, browser also
         # submit an empty part without filename
         list_image = []
         if images:
            for image in images:
               if image.filename == '':
                  nick.images = nick.images
               else:
                  path = app.config['UPLOAD_FOLDER'] + code
                  os.mkdir(path)
                  file_name = common.upload_file(image, path)
                  list_image.append(os.path.join(UPLOAD_FOLDER + code, image.filename))
                  nick.images = ','.join(list_image)

      nick.status = request.form.get('status')
      nick.game_name = game_name
      nick.game_info = json.dumps(data)
      nick.code = code
      nick.create_at = str(datetime.datetime.now())
      nick.user_id = current_user.id
      session.merge(nick)
      session.commit()
      session.close()

      flash('Update thông tin nick thành công!')
   except Exception as e:
      flash(e)
      flash('Hệ thống lỗi, nhờ báo cáo sự cố với bộ phận kỹ thuật.')
      redirect("/admin")
   return redirect("/admin")

@app.route('/delete-nick-<id>')
@login_required
def delete_nick(id):
   try:
      session.query(models.Nicks).filter(models.Nicks.id == int(id)).delete()
      flash('Xóa thông tin bán nick thành công!')
   except Exception as e:
      flash('Hệ thống lỗi, nhờ báo cáo sự cố với bộ phận kỹ thuật.')
   return redirect("/admin")

@app.route('/admin-ctv')
def admin_ctv():
   per = checkPermisson()
   if per == 'admin':
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
         historys = session.query(models.History).filter(models.History.user_id == nick.user_id).all()
         data = {
            "id": nick.id,
            "code": nick.code,
            "name": nick.name,
            "sale": len(historys),
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
   else:
      return redirect("/error")

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

      flash('Tạo ctv '+ account_tk +' thành công!')
   except Exception as e:
      flash(e)
      flash('Hệ thống lỗi, nhờ báo cáo sự cố với bộ phận kỹ thuật.')
   return redirect("/admin-ctv")

@app.route('/edit-user', methods=['POST'])
def edit_user():
   per = checkPermisson()
   if per == 'admin':
      try:
         id = request.form.get('id')
         name = request.form.get('name')
         account_tk = request.form.get('account_tk')
         password = request.form.get('password')
         money = request.form.get('money')
         
         user = session.query(models.Users).filter(models.Users.id == int(id)).first()
         user.name = name
         user.account_tk = account_tk
         user.password = password
         user.money = money
         user.create_at = str(datetime.datetime.now())

         session.merge(user)
         session.commit()
         session.close()

         flash('Update user '+ account_tk +' thành công!')
      except Exception as e:
         flash(e)
         flash('Hệ thống lỗi, nhờ báo cáo sự cố với bộ phận kỹ thuật.')
      return redirect("/admin-ctv")
   else:
      return redirect("/error")

@app.route('/admin-history')
def admin_history():
   per = checkPermisson()
   if per == 'admin':
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
      
      historys = session.query(models.History).all()
      data = []
      for his in historys:
         # Convert nicks data
         user = session.query(models.Users).filter(models.Users.id == his.user_id).first()
         history = {
            "id": his.id,
            "card": his.card,
            "buy": his.buy,
            "info": json.loads(his.info),
            "create_at": his.create_at,
            "user": { "name": user.name, "id": user.id },
            "status": his.status
         }
         data.append(history)

      return render_template('admin/history.html', data=data, nicks=nicks, sold=sold, on_sale=on_sale, ctv=ctv, enduser=enduser)
   elif per == 'ctv':
      # Get info nicks
      nicks = session.query(models.Nicks).filter(models.Nicks.user_id == current_user.id).order_by(desc(models.Nicks.id)).all()
      sold = []
      on_sale = []
      for nick in nicks:
         if nick.status == 'Đang bán':
            on_sale.append(nick)
         if nick.status == 'Đã bán':
            sold.append(nick)
      
      historys = session.query(models.History).filter(
         models.History.user_id == current_user.id,
         models.History.card == False,
         models.History.buy == False).all()
      data = []
      for his in historys:
         # Convert nicks data
         user = session.query(models.Users).filter(models.Users.id == his.user_id).first()
         history = {
            "id": his.id,
            "card": his.card,
            "buy": his.buy,
            "info": json.loads(his.info),
            "create_at": his.create_at,
            "status": his.status
         }
         data.append(history)
      return render_template(
         'admin/ctv-request.html',
         historys=data,
         sold=sold,
         on_sale=on_sale)
   else:
      return redirect("/error")

@app.route('/admin-user')
def admin_user():
   per = checkPermisson()
   if per == 'admin':
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
      return render_template('admin/user.html', nicks=nicks, sold=sold, on_sale=on_sale, ctv=ctv, enduser=enduser)
   else:
      return redirect("/error")

@app.route('/request', methods=['POST'])
def request():
   # try:
   price = request.form.get('price')
   description = request.form.get('description')
   
   history = models.History()
   history.create_at = str(datetime.datetime.now())
   history.card = False
   history.buy = False
   history.user_id = current_user.id
   history.status = 'Confirm'
   data = {
      "price": price,
      "description": description
   }
   history.info = json.dumps(data)

   session.add(history)
   session.commit()
   session.close()

   flash('Request rút tiền thành công!')
   # except Exception as e:
   #    flash(e)
   #    flash('Hệ thống lỗi, nhờ báo cáo sự cố với bộ phận kỹ thuật.')
   return redirect("/admin-ctv")

if __name__ == '__main__':
   app.run(debug = True)