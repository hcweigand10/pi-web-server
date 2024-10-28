from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)

# Example route: Home page with weather control
@app.route('/', methods=['GET', 'POST'])
def index():
    script_path = os.path.expanduser('~/led/rpi-rgb-led-matrix/bindings/python/samples/dashboard.py')
    if request.method == 'POST':
        new_location = request.form['location']
        # Use subprocess to call the LEDMatrixDashboard with the new location
        # Kill the old subprocess if it exists
        if hasattr(app, 'process') and app.process.poll() is None:
            app.process.terminate()
            app.process.wait()

        # Start a new subprocess with the new location
        app.process = subprocess.Popen(['sudo', 'python3', script_path, new_location])
        return redirect(url_for('index'))
    return render_template('index.html')

# Start the web server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
