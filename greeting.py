# Greeting morning, afternoon, evening, night
import time

def greet():
   current_hour = time.localtime().tm_hour
   if 4 <= current_hour <11:
    print("Good morning")
   elif 12 <= current_hour <15:
    print("Good afternoon")
   elif 15 <= current_hour <18:
    print("Good evening")
   else:
    print("Good night 💙")

greet()