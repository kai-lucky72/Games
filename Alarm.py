import datetime
import tkinter as tk
from tkinter import Label, Entry, Button, StringVar
from playsound import playsound


def set_alarm():
    global alarmtime, alarmmin, alarmhour
    alarmhour = int(entry_hour.get())
    alarmmin = int(entry_minute.get())
    alarmsec = int(entry_second.get())
    window.destroy()


alarmtime = input("am / pm: ")
alarmhour = int(input("enter hour: "))
alarmsec = int(input("enter seconds: "))
alarmmin = int(input("enter minutes: "))

if alarmtime.lower() == "pm":
    alarmhour += 12

window =tk.Tk()
window.title("Alarm Clock")

label_hour = tk.Label(window, text="Hour:")
label_hour.grid(row=0, column=0)
entry_hour = tk.Entry(window)
entry_hour.grid(row=0, column=1)

label_minute = tk.Label(window, text="Minute:")
label_minute.grid(row=1, column=0)
entry_minute = tk.Entry(window)
entry_minute.grid(row=1, column=1)

label_second = tk.Label(window, text="Second:")
label_second.grid(row=2, column=0)
entry_second =tk.Entry(window)
entry_second.grid(row=2, column=1)

set_alarm()

set_button = tk.Button(window, text="set alarm", command=ser_alarm)
while True:
    if alarmhour == datetime.datetime.now().hour and alarmmin == datetime.datetime.now().minute:
        print("Playing..")
        window = tk.Tk()
        window.title("Alarm Clock")
        break

window.mainloop()
if __name__=='__main__':
    