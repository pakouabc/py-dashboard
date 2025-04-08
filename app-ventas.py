from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def dashboard():
    labels = []
    ventas = []

    # Leer archivo CSV
    with open('ventas.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            labels.append(row['mes'])
            ventas.append(int(row['ventas']))

    return render_template('dashboard-ventas.html', labels=labels, ventas=ventas)

if __name__ == '__main__':
    app.run(debug=True)
