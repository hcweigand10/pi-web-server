from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

# Example route: Home page with weather control
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_location = request.form['location']
        # Use subprocess to call the LEDMatrixDashboard with the new location
        subprocess.run(['python3', 'led_dashboard.py', new_location])
        return redirect(url_for('index'))
    return render_template('index.html')

# Start the web server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
