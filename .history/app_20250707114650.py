from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    fluid = request.form['fluid']
    pressure = request.form['pressure']
    temperature = request.form['temperature']

    if fluid.lower() == 'water' and int(pressure) <= 16 and int(temperature) < 100:
        valve = "TECFLY Butterfly Valve"
    else:
        valve = "Consult the technical department"

    return render_template('index.html', result=valve, fluid=fluid, pressure=pressure, temperature=temperature)

if __name__ == '__main__':
    app.run(debug=True)
