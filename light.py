import RPi.GPIO as GPIO
from flask import Flask, render_template
import time
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
relay = 23
GPIO.setup(relay,GPIO.OUT)

app = Flask(__name__)

status = False
timerStatus = False

def timerSet(duration, act):
    global timerStatus
    timerStatus = True
    time.sleep(duration)
    global status
    if(act == "on"):
        if not (GPIO.input(relay)):
            status = True
            GPIO.output(relay, True)
    elif(act == "off"):
        if(GPIO.input(relay)):
            status = False
            GPIO.output(relay, False) 
    timerStatus = False


@app.route('/')
def index():
    global status
    return render_template('index.html', status = status, czas = None)

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
    
    return render_template('index.html', status = status, czas = None)

@app.route("/timer/<czas>/<akcja>")
def test(czas, akcja):
    global status
    global timerStatus
    if not (timerStatus):
        x = threading.Thread(target=timerSet, args=(int(czas),), kwargs={'act': akcja})
        x.start()
    return render_template('index.html', status = status, czas = int(czas))

if __name__ == '__main__':
    app.run(debug=True, port=82, host='0.0.0.0')
