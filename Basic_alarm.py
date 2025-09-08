import datetime
import time
import pygame

def Alarm_clock(args):  
    reminder_times = [datetime.datetime.strptime(r, "%Y-%m-%d %H:%M:%S") for r in args]
    while reminder_times:
        now = datetime.datetime.now()
        for reminder in reminder_times[:]:
            if now >= reminder:
                print(f"⏰ Reminder at {reminder.strftime('%Y-%m-%d %H:%M:%S')}")
                pygame.mixer.init()
                pygame.mixer.music.load(r"c:\Users\Rishi Roychowdhury\Downloads\beep.mp3.mp3")
                pygame.mixer.music.play()
                reminder_times.remove(reminder)
        time.sleep(1)

reminder_time = []
while True:
    user_input = input("Enter date_time: ")
    if user_input.lower() == 'done':
        break
    else:
        reminder_time.append(user_input)
Alarm_clock(reminder_time)