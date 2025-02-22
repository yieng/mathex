import random
import math

# polynomials of (ax+by)(cx+dy) orn (ax+b)(cx+d) format






# changing this number may necessitate changing the regex
try:
   N = int(input("Input the maximum coefficient for all questions in this session: "))
except ValueError:
   N = 5 #default
# to avoid errors in "random"
if N<=0:
   N = max(-N,5)

correct_count = 0
total_count = 0

operators = ['+','-','*','//']
Operators = ['+','−','×','÷']
L = len(operators)

success = ['✅','✔️','💯','🎯','🏆','🎉','🤗','🥳','😎','🥇','💥','💖','🔥','❤️','⭐','🙌']
try_again = ['🤔','💪','🧐']

var_string = 'abcdefghmnpqrstuvwxyz'
def getVar(var_string):
   # randomly select 3 consecutive characters as variables/unknowns
   V = var_string
   v = random.choice(V[0:-2])
   var = [v, V[V.index(v)+1], random.choice([V[V.index(v)+2],''])]
   return var

def tuple2polynomial(myTuple, var):
   polynomial = ''
   for i in range(len(myTuple)):
      coeff = myTuple[i]
      #print(coeff)
      if coeff==1 and var[i]!='':
         polynomial += '+' + var[i]
      elif coeff>1 or (coeff==1 and var[i]==''):
         polynomial += '+' + str(coeff) + var[i]
      elif coeff==-1 and var[i]!='':
         polynomial += '-' + var[i]
      elif coeff<-1 or (coeff==-1 and var[i]==''):
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
   var0 = getVar(var_string)
   
   # Power of (-1): 0 = positive, 1 = negative
   coeff = [(-1)**random.randint(0,1)*random.randint(1,N) for j in range(tuplelength)]   
   b = 1
   while b==1:
      b = (-1)**random.randint(0,1)*random.randint(1,N)

   if b==-1:
      b0 = '-'
   else:
      b0 = str(b)

   expression = b0 + '(' + tuple2polynomial(coeff,var0) + ')'
   
   answerTuple = [b*coeff[i] for i in range(len(coeff))]
      
   first_try = True
   correct = False
   
   while not(correct):
       y = input(expression+' = ')
       x = tuple2polynomial(answerTuple,var0)
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
       

