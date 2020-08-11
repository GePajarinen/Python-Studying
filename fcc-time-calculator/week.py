def whichDayOfWeek(weekday, days):

  week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

  x = week.index(weekday)
  theday =  round(((x + days)/7 - ((x + days)//7)) * 7)

  return week[theday] 
  