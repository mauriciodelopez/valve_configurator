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
        'pressure': float(request.form['pressure']),
        'temperature': float(request.form['temperature']),
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

    # Call advisor logic
    recommendations = generate_recommendations(data)

    result = "Custom Knife Gate Valve configuration received. Please review your inputs and the recommended options."

    return render_template('index.html', result=result, data=data, recommendations=recommendations)

# 💡 Advisor Logic Function
def generate_recommendations(data):
    rec = {}

    # 🔹 Seat Type Logic
    if data['fluid'].lower() == 'water' and data['temperature'] > 100:
        rec['seat_type'] = 'PTFE'
    elif 'slurry' in data['fluid'].lower() or 'high' in data['solid_content'].lower():
        rec['seat_type'] = 'Metal'
    else:
        rec['seat_type'] = 'EPDM'

    # 🔹 Body Material Logic
    if 'acid' in data['fluid'].lower() or 'chemical' in data['fluid'].lower():
        rec['body_material'] = 'Stainless Steel'
    elif data['temperature'] > 150:
        rec['body_material'] = 'Carbon Steel'
    else:
        rec['body_material'] = 'Ductile Iron'

    # 🔹 Actuation Logic
    if data['actuation_type'].lower() == 'pneumatic':
        if float(data['cycle_frequency'].split('/')[0]) > 30:
            rec['actuation'] = 'Pneumatic, Double-Acting, With Positioner'
        else:
            rec['actuation'] = 'Pneumatic, Single-Acting'
    elif data['actuation_type'].lower() == 'electric':
        if 'outdoor' in data['conditions'].lower():
            rec['actuation'] = 'Electric Actuator, IP67 Enclosure'
        else:
            rec['actuation'] = 'Electric Actuator, IP65 Enclosure'
    else:
        rec['actuation'] = 'Manual (Handwheel or Gear)'

    return rec

if __name__ == '__main__':
    app.run(debug=True)
