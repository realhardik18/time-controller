from PIL import Image
import time
print("hello realhardik18, enter the amount of time(minutes) your gonna do the task so we can remind you on time below")
user_input=input()
timee=int(user_input)*60
time.sleep(timee)
img=Image.open("snap.png")
img.show()
print("cya later than")