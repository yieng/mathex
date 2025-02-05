import random
import math
### import re # regex

# changing this number may necessitate changing the regex
N = 5

# regex (regular expressions)
### regex_monomial = "[0-9]{0,2}[a-z]?"
### regex_binomial = "[0-9]{0,2}[a-z]?[+|-][0-9]{0,2}[a-z]?"
### regex_trinomial = "[0-9]{0,2}[a-z]?[+|-][0-9]{0,2}[a-z]?[+|-][0-9]{0,2}[a-z]?"

correct_count = 0
total_count = 0

operators = ['+','-','*','//']
Operators = ['+','−','×','÷']
L = len(operators)

success = ['✅','✔️','💯','🎯','🏆','🎉','🤗','🥳','😎','🥇','💥','💖','🔥','❤️','⭐','🙌']
try_again = ['🤔','💪','🧐']

def tuple2polynomial(myTuple):
   var = ['x','y','z']
   polynomial = ''
   for i in range(len(myTuple)):
      coeff = myTuple[i]
      #print(coeff)
      if coeff==1:
         polynomial += '+' + var[i]
      elif coeff>1:
         polynomial += '+' + str(coeff) + var[i]
      elif coeff==-1:
         polynomial += '-' + var[i]
      elif coeff<-1:
         polynomial += str(coeff) + var[i]
      else: # i==0
         continue
   #print(polynomial)
   if polynomial[0]=='+':
      polynomial = polynomial[1::]
   return polynomial

while True: # infinite loop

   # of the format #(#x+#y) or #(#x+#y+#z).
   # next time: (#a+#b)(#c+#d) and (#a+#b)(#c+#d+#e).
   
   tuplelength = random.randint(2,3)
   # Power of (-1): 0 = positive, 1 = negative
   coeff = [(-1)**random.randint(0,1)*random.randint(1,N) for j in range(tuplelength)]   
   b = 1
   while b==1:
      b = (-1)**random.randint(0,1)*random.randint(1,N)

   if b==-1:
      b0 = '-'
   else:
      b0 = str(b)

   expression = b0 + '(' + tuple2polynomial(coeff) + ')'
   
   answerTuple = [b*coeff[i] for i in range(len(coeff))]
      
   first_try = True
   correct = False
   
   while not(correct):
       y = input(expression+' = ')
       x = tuple2polynomial(answerTuple)
       correct = (x==y)

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
       

