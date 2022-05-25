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
timeToSwitch = None

def timerSet(duration, act):
    global timerStatus
    timerStatus = True
    timeToAdd = timedelta(seconds=duration)
    global timeToSwitch
    timeToSwitch =  datetime.now() + timeToAdd
    timeToSwitch = int(time.mktime(timeToSwitch.timetuple())) * 1000
    for i in range(duration):
        if timerStatus == False: 
            timeToSwitch = None
            return
        time.sleep(1)
    #time.sleep(duration)
    global status
    if(act == "on"):
        if not (GPIO.input(relay)):
            status = True
            GPIO.output(relay, True)
    elif(act == "off"):
        if(GPIO.input(relay)):
            status = False
            GPIO.output(relay, False) 
    timeToSwitch = None
    timerStatus = False


@app.route('/')
def index():
    global status
    global timeToSwitch
    return render_template('index.html', status = status, timeToSwitch = timeToSwitch)

@app.route("/<akcja>")
def action(akcja):
    global status
    global timerStatus
    global timeToSwitch
    if (akcja == "on"):
        if (status==False):
          status = True
          GPIO.output(relay, True) 
    if (akcja == "off"):
        if (status==True):
          status = False
          GPIO.output(relay, False)
    if (akcja == "cancel"):
        if (timerStatus == True):
            timerStatus = False
            time.sleep(1)
    return render_template('index.html', status = status, timeToSwitch = timeToSwitch)

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
    global timeToSwitch
    return render_template('index.html', status = status, timeToSwitch = timeToSwitch)

if __name__ == '__main__':
    app.run(debug=True, port=82, host='0.0.0.0')
