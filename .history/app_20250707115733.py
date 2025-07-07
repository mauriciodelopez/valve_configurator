from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = {
        'fluid': request.form['fluid'],
        'solid_content': request.form['solid_content'],
        'flow_direction': request.form['flow_direction'],
        'pressure': request.form['pressure'],
        'temperature': request.form['temperature'],
        'line_size': request.form['line_size'],
        'installation_position': request.form['installation_position'],
        'body_material': request.form['body_material'],
        'seat_type': request.form['seat_type'],
        'gate_material': request.form['gate_material'],
        'port_design': request.form['port_design'],
        'flange_type': request.form['flange_type'],
        'actuation_type': request.form['actuation_type'],
        'voltage': request.form.get('voltage'),
        'control_type': request.form['control_type'],
        'signal_type': request.form.get('signal_type'),
        'enclosure_rating': request.form.get('enclosure_rating'),
        'manual_override': request.form.get('manual_override'),
        'air_supply': request.form.get('air_supply'),
        'positioner': request.form.get('positioner'),
        'solenoid_valve': request.form.get('solenoid_valve'),
        'limit_switches': request.form.get('limit_switches'),
        'frl': request.form.get('frl'),
        'cycle_frequency': request.form['cycle_frequency'],
        'opening_speed': request.form['opening_speed'],
        'space': request.form['space'],
        'conditions': request.form['conditions'],
        'certifications': request.form['certifications']
    }

    result = "Custom Knife Gate Valve configuration received. Please review your inputs."

    return render_template('index.html', result=result, data=data)

if __name__ == '__main__':
    app.run(debug=True)