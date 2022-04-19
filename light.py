import RPi.GPIO as GPIO
from flask import Flask, render_template

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
relay = 23
GPIO.setup(relay,GPIO.OUT)

app = Flask(__name__)

status = False

@app.route('/')
def index():
    global status
    return render_template('index.html', status = status)

@app.route("/<akcja>")
def action(akcja):
    global status
    if (akcja == "on"):
        if (status==False):
          status = True
          GPIO.output(relay, True) 
    if (akcja == "off"):
        if (status==True):
          status = False
          GPIO.output(relay, False)
    
    return render_template('index.html', status = status)

if __name__ == '__main__':
    app.run(debug=True, port=82, host='0.0.0.0')
