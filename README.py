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
