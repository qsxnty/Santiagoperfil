from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('contacto.html')

@app.route('/contact', methods=['POST'])
def contact():
    nombre = request.form['nombre']
    email = request.form['email']
    asunto = request.form['asunto']
    mensaje = request.form['mensaje']
    
   
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print(f"Asunto: {asunto}")
    print(f"Mensaje: {mensaje}")
    
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return "¡Gracias por tu mensaje! Te responderemos pronto."

if __name__ == '__main__':
    app.run(debug=True)
