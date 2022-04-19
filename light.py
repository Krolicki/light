import RPi.GPIO as GPIO
from flask import Flask, render_template

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
relay = 23
GPIO.setup(relay,GPIO.OUT)

app = Flask(light)

status = False

@app.route('/')
def index():
    global status
    return render_template('index.html', status = status)

@app.route("/<akcja>")
def action(akcja):
    global status
    if (akcja == "on"):
        if (go==False):
          status = True
          GPIO.output(relay, True) 
    if (akcja == "off"):
        if (go==True):
          status = False
          GPIO.output(relay, False)
    
    return render_template('index.html', status = status)

if light == 'main':
    app.run(debug=True, port=82, host='0.0.0.0')