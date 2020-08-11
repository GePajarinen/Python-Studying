# This entrypoint file to be used in development. Start by reading README.md
#from time_calculator import add_time
#from unittest import main

#(start, duration, dayOfWeek = "")
#print(add_time("11:06 PM", "2:02"))

start = "11:40 PM"
duration = "100:05"

s_time, s_moment = start.split(" ")
s_hour, s_minute = s_time.split(":")
d_hour, d_minute = duration.split(":")

s_hour = int(s_hour)
s_minute = int(s_minute)
d_hour = int(d_hour)
d_minute = int(d_minute)
days= 0

if s_moment == "AM":
  if s_hour == 12:
    hour = 0
  else:
    hour = s_hour
else: #s_moment == "PM"
  if s_hour == 12:
    hour = s_hour
  else:
    hour = s_hour +12

ext_hour = (s_minute + d_minute)//60
minutes = round(((((s_minute + d_minute)/60) - ext_hour) * 60))

ext_day = (hour + d_hour + ext_hour) //24
sum_h = round(((((hour + d_hour + ext_hour)/24) - ext_day) * 24))

total_h = 0
AP= ""

if sum_h >= 0 and sum_h <=11 or sum_h == 24:
  AP = "AM"
  total_h = sum_h
else: #sum_h >11 and sum_h <=23
  AP = "PM"
  total_h = sum_h -12

f_time = ""

if ext_day == 0:
  f_time = str(total_h) + ":" + str(minutes) + ' ' + AP
  
else: #Extra day > 0

  if ext_day == 1:
    f_time = str(total_h) + ":" + str(minutes) + ' ' + AP + ' ' + "(next day)"

  else:
    f_time = str(total_h) + ":" + str(minutes) + ' ' + AP + ' (' + str(ext_day) + " days later)"
    

print(f_time)


# Run unit tests automatically
#main(module='test_module', exit=False)