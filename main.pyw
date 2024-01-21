import time
import sched
from plyer import notification

scheduler = sched.scheduler(time.time, time.sleep)
alertInterval = 3600    # seconds between alerts
title = "Hydration Check!"  # title of alert
message = "Stretch, get water, and get your butt off your chair!" # message of alert

def sendAlert():
    notification.notify(title=title, message=message, app_name="Aiden's Alerts", app_icon="lightbulb.ico")
    
def repeatTask():
    scheduler.enter(alertInterval, 1, sendAlert, ())
    scheduler.enter(alertInterval, 1, repeatTask, ())
    
repeatTask()
scheduler.run()
    