import random
import math

# changing this number may necessitate changing the regex
try:
   N = int(input("Input a positive integer: "))
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
def getVarConst(var_string):
   # randomly select 3 consecutive characters as variables/unknowns
   V = var_string
   v = random.choice(V)
   var = [v, '']
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

# polynomials of (ax+by)(cx+dy) or (ax+b)(cx+d) format

while True: # infinite loop

   # of the format: (#a+#b)(#c+#d) - not yet (#a+#b)(#c+#d+#e).
   
   tuplelength = 2
   var0 = getVarConst(var_string)
   v = var0[0]

   print("=== Answer in the following format, \n=== with variable x and non-0,1 constants A, B, C: \n===      Ax^2±Bx±C \n=== (type '^' using SHIFT+6) :".replace('x',v))

   twoTuples = []

   for k in range(0,2):
      # Power of (-1): 0 = positive, 1 = negative
      coeff = [(-1)**random.randint(0,1)*random.randint(1,N) for j in range(tuplelength)]   
      #b = 1
      #while b==1:
      #   b = (-1)**random.randint(0,1)*random.randint(1,N)

      #if b==-1:
      #   b0 = '-'
      #else:
      #   b0 = str(b)

      #expression = b0 + '(' + tuple2polynomial(coeff,var0) + ')'
      
      #answerTuple = [b*coeff[i] for i in range(len(coeff))]

      twoTuples.append(coeff)

   monomials = [tuple2polynomial(t,var0) for t in twoTuples]
   expression = ''.join(['('+m+')' for m in monomials])
   # print(expression)

   ## (3f+3)(2f-5) = 3f(2f-5)+3(2f-5) = vertical calc = 6f^2+9f-15

   #print(twoTuples)

   R = range(len(twoTuples))

   coeff2 = eval('*'.join([str(twoTuples[i][0]) for i in R]))
   #print(coeff2)
   coeff0 = eval('*'.join([str(twoTuples[i][1]) for i in R]))
   #print(coeff0)
   coeff1 = []
   coeff1.append('*'.join([str(twoTuples[i][j]) for j in R for i in R if i==j]))
   coeff1.append('*'.join([str(twoTuples[i][j]) for j in R for i in R if i!=j]))
   coeff1 = eval('+'.join(coeff1))

   coeff_ = [coeff2, coeff1, coeff0]
   var1 = [v+'^2', v, '']
   
   first_try = True
   correct = False
   
   while not(correct):
       y = input(expression+' = ')
       x = tuple2polynomial(coeff_,var1)
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
   print('Correct on first attempt: ', correct_count, '\nTotal questions attempted: ', total_count, '\n==================================================')
       

