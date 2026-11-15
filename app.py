import sqlite3
import csv
import io
from flask import Flask, render_template, request, redirect, url_for, session, flash, Response

app = Flask(__name__)
app.secret_key = 'clave_secreta_super_segura'
DB_NAME = 'gastos.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            monto REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    if 'usuario' in session:
        return redirect(url_for('dashboard'))
        
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        clave = request.form.get('clave')
        
        if usuario == 'admin' and clave == '123':
            session['usuario'] = usuario
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales incorrectas. Intenta de nuevo.')
            
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('login'))
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    if request.method == 'POST':
        fecha = request.form.get('fecha')
        descripcion = request.form.get('descripcion')
        monto = float(request.form.get('monto'))
        
        cursor.execute('INSERT INTO gastos (fecha, descripcion, monto) VALUES (?, ?, ?)',
                       (fecha, descripcion, monto))
        conn.commit()
        return redirect(url_for('dashboard'))
        
    cursor.execute('SELECT id, fecha, descripcion, monto FROM gastos ORDER BY fecha DESC')
    gastos = cursor.fetchall()
    
    cursor.execute('SELECT SUM(monto) FROM gastos')
    resultado = cursor.fetchone()
    total = resultado[0] if resultado and resultado[0] is not None else 0.0
    conn.close()
    
    return render_template('index.html', gastos=gastos, total=total)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM gastos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/reporte')
def reporte():
    if 'usuario' not in session:
        return redirect(url_for('login'))
        
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT id, fecha, descripcion, monto FROM gastos ORDER BY fecha DESC')
    gastos = cursor.fetchall()
    conn.close()
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Fecha', 'Descripcion', 'Monto'])
    for g in gastos:
        writer.writerow(g)
        
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=reporte_gastos.csv"}
    )

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)