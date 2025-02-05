import random
import math

N = 50
correct_count = 0
total_count = 0

operators = ['+','-','*','//']
Operators = ['+','−','×','÷']
L = len(operators)

success = ['✅','✔️','💯','🎯','🏆','🎉','🤗','🥳','😎','🥇','💥','💖','🔥','❤️','⭐','🙌']
try_again = ['🤔','💪','🧐']

while True: # infinite loop
   a = random.randint(-N,N+1)
   b = random.randint(-N,N+1)
   i = random.choice([i for i in range(0,L)])
   o = operators[i]
   O = Operators[i]
   correct = False
   
   if o == '//':
      d = a*b
      if b != 0:
        a = d
      else:
        b = d
        a = b
   if (a < 0):
      a1 = '('+str(a)+')'
      a2 = '(−'+str(-a)+')'
   else:
      a1 = str(a)
      a2 = str(a)
   if (b < 0):
      b1 = '('+str(b)+')'
      b2 = '(−'+str(-b)+')'
   else:
      b1 = str(b)
      b2 = str(b)
   c = a1 + o + b1
   first_try = True
   while not(correct):
       y = input(a2+O+b2+' = ')
       x = eval(c)
       correct = (str(x)==y)
       # print(first_try)
       if correct:
          print('Correct ' + random.choice(success))
          if first_try:
             correct_count += 1
             total_count += 1
          break
       else:
          print('Try again ' + random.choice(try_again))
          if first_try:
             total_count += 1
          first_try = False
   print('Correct on first attempt: ', correct_count, '\nTotal questions attempted: ', total_count, '\n===')
       
