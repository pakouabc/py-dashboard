from flask import Flask, render_template, request, redirect
import csv
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # Max 2MB

# Crear carpeta de uploads si no existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    labels = []
    ventas = []

    if request.method == 'POST':
        file = request.files['archivo']
        if file and file.filename.endswith('.csv'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Leer archivo CSV subido
            with open(filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    labels.append(row['mes'])
                    ventas.append(int(row['ventas']))

            return render_template('dashboard-load.html', labels=labels, ventas=ventas)

    return render_template('dashboard-load.html', labels=labels, ventas=ventas)
