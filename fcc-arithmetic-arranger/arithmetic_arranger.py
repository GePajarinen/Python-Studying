def arithmetic_arranger(problems, withAnswer = False):
  
  if len(problems) >5:
    return "Error: Too many problems."
  else:  

    line1=[]
    line2=[]
    line3=[]
    line4=[]

    for i, prob in enumerate(problems):
      op1, sign, op2 = prob.split(" ")

      #Situations that will return an error:
      if len(op1) <= 4 and len(op2) <= 4:
        
        if op1.isdigit() == True and op2.isdigit() == True:
            
          if sign == '+':
            answ = str(int(op1) + int(op2))
          elif sign == '-':
            answ = str(int(op1) - int(op2))
          else:
            return "Error: Operator must be '+' or '-'."

        else:
          return "Error: Numbers must only contain digits."
      else:
        return "Error: Numbers cannot be more than four digits."    


      width = max(len(op1),len(op2)) +2
        
      line1.append(op1.rjust(width))
      line2.append(sign + op2.rjust(width-1))
      line3.append("-" * width)
      line4.append(answ.rjust(width))
    
    total = []
    total.append('    '.join(line1))
    total.append('    '.join(line2))
    total.append('    '.join(line3))
    total.append('    '.join(line4))
    
    if withAnswer == True:
      arranged_problems = '\n'.join(total)
      
    else:
      arranged_problems = '\n'.join(total[:-1])   

  return arranged_problems


"""" THIS MATH DOESNT WORK:
      if op1 > op2:
        part1= (" "*2)+ op1
        part2= sign+(' '* (len(part1)-1-len(op2)))+op2
        part3 = "-" * int(len(part1))
        part4 = " " * (len(part3)-len(answ)) + answ

      else:
        part1 = " "* ((len(op2)+2)-len(op1)) + op1
        part2 = sign + ' ' + op2
        part3= "-"* len(part2)
        part4 = " " * (len(part3)-len(answ)) + answ
"""
