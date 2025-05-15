import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import threading
from playsound import playsound

def set_reminder():
    reminder_time = time_entry.get()
    reminder_msg = message_entry.get()
    
    try:
        reminder_datetime = datetime.strptime(reminder_time, "%H:%M")
    except ValueError:
        messagebox.showerror("Invalid Time Format", "Please enter time in HH:MM format.")
        return

    def wait_and_alert():
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            if current_time == reminder_time:
                messagebox.showinfo("Reminder", reminder_msg)
                playsound("alarm.mp3")  # Replace with your sound file name
                break
            time.sleep(10)

    threading.Thread(target=wait_and_alert).start()

# GUI setup
root = tk.Tk()
root.title("Reminder App")

tk.Label(root, text="Enter time (HH:MM):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Label(root, text="Enter reminder message:").pack()
message_entry = tk.Entry(root)
message_entry.pack()

tk.Button(root, text="Set Reminder", command=set_reminder).pack()

root.mainloop()