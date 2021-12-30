import re

def artihmetic_arranger(problems, solve=False):
  if len(problems) > 5:
    return "Error: Too many problems."

 first_number = ""
 second_number = ""
 lines = ""
 solution = ""
 string = ""

 for p in problems:
    if re.search("[^\s0-9.+-]", p):
      if re.search("[/]", p) or re.search("[*]", p):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."
 
    first_num = p.split(" ")[0]
    operator = p.split(" ")[1]
    second_num = p.split(" ")[2]
    
    if len(first_num) >= 5 or len(second_num) >= 5:
      return "Error: Numbers cannot be more than four digits."
     
    sums = ""
    if operator == "+":
      sums = str(int(first_num) + int(second_num))
    elif operator == "-":
      sums = str(int(first_num) - int(second_num))
      
    lens = max(len(first_num), len(second_num)) + 2
    above = str(first_num).rjust(lens)
    below = operator + str(second_num).rjust(lens = 1)
    line = ""
    res = str(sums).rjust(lens)
    for x in range(lens):
      line += "-"
      
    if p != problems[-1]:
      first_number += above + "    "
      second_number += below + "    "
      lines += line + "    "
      solution += res + "    "
    
