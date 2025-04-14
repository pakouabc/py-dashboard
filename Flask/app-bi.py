from flask import Flask, render_template, request
import csv
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    labels = []
    ventas = []
    resumen = {}
    chart_type = 'bar'

    if request.method == 'POST':
        file = request.files['archivo']
        chart_type = request.form.get('tipo_grafico', 'bar')

        if file and file.filename.endswith('.csv'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            with open(filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    labels.append(row['mes'])
                    ventas.append(int(row['ventas']))

            if ventas:
                resumen = {
                    'total': sum(ventas),
                    'promedio': round(sum(ventas)/len(ventas), 2),
                    'maximo': max(ventas)
                }

    return render_template('dashboard-bi.html',
                           labels=labels,
                           ventas=ventas,
                           resumen=resumen,
                           chart_type=chart_type)

if __name__ == '__main__':
    app.run(debug=True)
