from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Datos simulados que podrían venir de una base de datos
    labels = ['Enero', 'Febrero', 'Marzo', 'Abril']
    ventas = [12000, 15000, 14000, 17000]

    return render_template('dashboard-render.html', labels=labels, ventas=ventas)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/simple")
def simple():
    return render_template('dashboard-simple.html')

@app.route("/grafica")
def grafica():
    return render_template('dashboard-graph.html')