from week import whichDayOfWeek

def add_time(start, duration, dayOfWeek=""):

  dayOfWeek = dayOfWeek.capitalize()

  s_time, s_moment = start.split(" ")
  s_hour, s_minute = s_time.split(":")
  d_hour, d_minute = duration.split(":")

  s_hour = int(s_hour)
  s_minute = int(s_minute)
  d_hour = int(d_hour)
  d_minute = int(d_minute)

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

  if sum_h > 0 and sum_h <=11:
    AP = "AM"
    total_h = sum_h
  elif sum_h == 24 or sum_h == 0:
    AP = "AM"
    total_h = 12
  else: #sum_h >11 and sum_h <=23
    AP = "PM"
    if sum_h == 12:
      total_h = sum_h
    else:
      total_h = sum_h -12
  

  if ext_day == 0: #On same day
    if len(dayOfWeek) > 0:
      new_time = str(total_h) + ":" + "{:02d}".format(minutes) + ' ' + AP + ', '+ dayOfWeek
    else:
      new_time = str(total_h) + ":" + "{:02d}".format(minutes) + ' ' + AP
    
  else: #Extra day > 0

    if ext_day == 1: #NEXT DAY
      if len(dayOfWeek) > 0: #With day of week
        d_week = whichDayOfWeek(dayOfWeek, ext_day)
        new_time = str(total_h) + ":" + "{:02d}".format(minutes) + ' ' + AP + ', ' + d_week + " (next day)"
      else: #No day of week
        new_time = str(total_h) + ":" + "{:02d}".format(minutes) + ' ' + AP + " (next day)"
    
    else: #MORE DAYS LATER
      if len(dayOfWeek) > 0: #With day of week
        d_week = whichDayOfWeek(dayOfWeek, ext_day)
        new_time = str(total_h) + ":" + "{:02d}".format(minutes) + ' ' + AP +', ' + d_week + ' (' + str(ext_day) + " days later)"
      else:  #No day of week
        new_time = str(total_h) + ":" + "{:02d}".format(minutes) + ' ' + AP + ' (' + str(ext_day) + " days later)"
  
  return new_time
