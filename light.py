import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import time
import threading
from datetime import datetime, timedelta

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
relay = 23
GPIO.setup(relay,GPIO.OUT)

app = Flask(__name__)

status = False
timerStatus = False
timeToSwitch = "NULL"

def timerSet(duration, act):
    global timerStatus
    timerStatus = True
    timeToAdd = timedelta(seconds=duration)
    global timeToSwitch
    timeToSwitch =  datetime.now() + timeToAdd
    timeToSwitch = int(time.mktime(timeToSwitch.timetuple())) * 1000
    print(timeToSwitch)
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

@app.route("/timer")
def test():
    global status
    global timerStatus
    get_czas = int(request.args.get('time'))
    get_akcja = request.args.get('action')
    get_type = request.args.get('type')
    if(get_type == "min"):
        get_czas = get_czas*60
    if not (timerStatus):
        x = threading.Thread(target=timerSet, args=(get_czas,), kwargs={'act': get_akcja})
        x.start()
    return render_template('index.html', status = status, czas = int(get_czas), timeToSwitch = timeToSwitch)

if __name__ == '__main__':
    app.run(debug=True, port=82, host='0.0.0.0')
