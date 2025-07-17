from flask import Flask, render_template, request, send_file
from xhtml2pdf import pisa
from io import BytesIO

app = Flask(__name__)

# 🔹 Home page with form
@app.route('/')
def home():
    return render_template('index.html')

# 🔹 Handle form submission and display results
@app.route('/generate', methods=['POST'])
def generate():
    data = {
        'fluid': request.form.get('fluid'),
        'solid_content': request.form.get('solid_content'),
        'flow_direction': request.form.get('flow_direction'),
        'pressure': float(request.form.get('pressure', 0)),
        'temperature': float(request.form.get('temperature', 0)),
        'line_size': request.form.get('line_size'),
        'installation_position': request.form.get('installation_position'),
        'body_material': request.form.get('body_material'),
        'seat_type': request.form.get('seat_type'),
        'gate_material': request.form.get('gate_material'),
        'port_design': request.form.get('port_design'),
        'flange_type': request.form.get('flange_type'),
        'actuation_type': request.form.get('actuation_type'),
        'voltage': request.form.get('voltage'),
        'control_type': request.form.get('control_type'),
        'signal_type': request.form.get('signal_type'),
        'enclosure_rating': request.form.get('enclosure_rating'),
        'manual_override': request.form.get('manual_override'),
        'air_supply': request.form.get('air_supply'),
        'positioner': request.form.get('positioner'),
        'solenoid_valve': request.form.get('solenoid_valve'),
        'limit_switches': request.form.get('limit_switches'),
        'frl': request.form.get('frl'),
        'cycle_frequency': request.form.get('cycle_frequency'),
        'opening_speed': request.form.get('opening_speed'),
        'space': request.form.get('space'),
        'conditions': request.form.get('conditions'),
        'certifications': request.form.get('certifications')
    }

    recommendations = generate_recommendations(data)

    result = "Custom Knife Gate Valve configuration received. Please review your inputs and the recommended options."

    return render_template('index.html', result=result, data=data, recommendations=recommendations)

# 🔹 Smart advisor logic
def generate_recommendations(data):
    rec = {}

    # Seat Type
    if data['fluid'] and data['fluid'].lower() == 'water' and data['temperature'] > 100:
        rec['seat_type'] = 'PTFE'
    elif data['solid_content'] and ('slurry' in data['fluid'].lower() or 'high' in data['solid_content'].lower()):
        rec['seat_type'] = 'Metal'
    else:
        rec['seat_type'] = 'EPDM'

    # Body Material
    if data['fluid'] and ('acid' in data['fluid'].lower() or 'chemical' in data['fluid'].lower()):
        rec['body_material'] = 'Stainless Steel'
    elif data['temperature'] > 150:
        rec['body_material'] = 'Carbon Steel'
    else:
        rec['body_material'] = 'Ductile Iron'

    # Actuation
    actuation = data.get('actuation_type', '').lower()
    if actuation == 'pneumatic':
        if data['cycle_frequency']:
            try:
                cycles = int(data['cycle_frequency'].split('/')[0])
                if cycles > 30:
                    rec['actuation'] = 'Pneumatic, Double-Acting, With Positioner'
                else:
                    rec['actuation'] = 'Pneumatic, Single-Acting'
            except:
                rec['actuation'] = 'Pneumatic Actuator'
        else:
            rec['actuation'] = 'Pneumatic Actuator'
    elif actuation == 'electric':
        if data['conditions'] and 'outdoor' in data['conditions'].lower():
            rec['actuation'] = 'Electric Actuator, IP67 Enclosure'
        else:
            rec['actuation'] = 'Electric Actuator, IP65 Enclosure'
    else:
        rec['actuation'] = 'Manual (Handwheel or Gear)'

    return rec

# 🔹 PDF generation
@app.route('/pdf', methods=['POST'])
def generate_pdf():
    data = request.form.to_dict()

    recommendations = generate_recommendations({
        **data,
        'temperature': float(data.get('temperature', 0)),
        'pressure': float(data.get('pressure', 0)),
        'solid_content': data.get('solid_content', ''),
        'fluid': data.get('fluid', ''),
        'actuation_type': data.get('actuation_type', ''),
        'conditions': data.get('conditions', ''),
        'cycle_frequency': data.get('cycle_frequency', '')
    })

    html = render_template('pdf_template.html', data=data, recommendations=recommendations)
    pdf = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf)
    pdf.seek(0)

    if pisa_status.err:
        return "Error generating PDF", 500

    return send_file(pdf, as_attachment=True, download_name="datasheet.pdf", mimetype='application/pdf')

# 🔹 Run the app
if __name__ == '__main__':
    app.run(debug=True port=5001)
