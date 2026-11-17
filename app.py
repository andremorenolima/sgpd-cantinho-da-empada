from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cantinho-da-empada-secret-key-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sgpd.db'
db = SQLAlchemy(app)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password_hash = db.Column(db.String(200), nullable=False)


class Order(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  client_name = db.Column(db.String(100), nullable=False)
  phone = db.Column(db.String(20), nullable=False)
  items = db.Column(db.Text, nullable=False)
  pickup_time = db.Column(db.String(50), nullable=False)
  dietary_restrictions = db.Column(db.String(200), nullable=True)
  status = db.Column(
      db.String(20), default='Pendente'
  )  # Pendente, Em Produção, Finalizado
  created_at = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
  db.create_all()
  # Cria usuário gerente padrão se não existir
  if not User.query.filter_by(username='gerente.cantinho').first():
    hashed_pw = generate_password_hash('senha123')
    admin = User(username='gerente.cantinho', password_hash=hashed_pw)
    db.session.add(admin)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
      return redirect(url_for('balcao'))
    flash('Credenciais inválidas. Tente novamente.', 'danger')
  return render_template('login.html')


@app.route('/balcao', methods=['GET', 'POST'])
def balcao():
  if request.method == 'POST':
    client_name = request.form.get('client_name')
    phone = request.form.get('phone')
    items = request.form.get('items')
    pickup_time = request.form.get('pickup_time')
    dietary_restrictions = request.form.get('dietary_restrictions')

    if not client_name or not phone or not items or not pickup_time:
      flash('Preencha todos os campos obrigatórios.', 'danger')
      return redirect(url_for('balcao'))

    new_order = Order(
        client_name=client_name,
        phone=phone,
        items=items,
        pickup_time=pickup_time,
        dietary_restrictions=dietary_restrictions,
        status='Pendente',
    )
    db.session.add(new_order)
    db.session.commit()
    flash('Encomenda cadastrada com sucesso!', 'success')
    return redirect(url_for('cozinha'))
  return render_template('balcao.html')


@app.route('/cozinha')
def cozinha():
  pending_orders = Order.query.filter_by(status='Pendente').all()
  in_production = Order.query.filter_by(status='Em Produção').all()
  finished_orders = Order.query.filter_by(status='Finalizado').all()
  return render_template(
      'cozinha.html',
      pending=pending_orders,
      production=in_production,
      finished=finished_orders,
  )


@app.route('/update_status/<int:order_id>/<string:new_status>')
def update_status(order_id, new_status):
  order = Order.query.get_or_404(order_id)
  if new_status in ['Pendente', 'Em Produção', 'Finalizado']:
    order.status = new_status
    db.session.commit()
  return redirect(url_for('cozinha'))


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
