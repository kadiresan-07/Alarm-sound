!pip install plyer
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import threading
from plyer import notification 
from playsound import playsound

def set_reminder():
    reminder_time = input("Enter time (HH:MM): ")  
    reminder_msg = input("Enter reminder message: ") 
    
    try:
        reminder_datetime = datetime.strptime(reminder_time, "%H:%M")
    except ValueError:
        print("Invalid Time Format. Please enter time in HH:MM format.")  
        return
    def wait_and_alert():
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            if current_time == reminder_time:
                notification.notify(
                    title="Reminder",
                    message=reminder_msg,
                    app_name="Reminder App",
                    timeout=10 
                )
                playsound("alarm.mp3") 
                break
            time.sleep(10)
    threading.Thread(target=wait_and_alert).start()
set_reminder()