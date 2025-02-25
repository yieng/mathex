import random
import math

success = ['✅','✔️','💯','🎯','🏆','🎉','🤗','🥳','😎','🥇','💥','💖','🔥','❤️','⭐','🙌']
try_again = ['🤔','💪','🧐']

N = 20

fivePercentOf100Denominator = 20

aHundred = 100

def neatPercentages(num):
   available_divisors = [2, 4, 5, 10, 20] # 50%, 25%, 20%, 10%, 5%
   approved_divisors = [a for a in available_divisors if num % a == 0]
   percentages = [100//a for a in available_divisors if num % a == 0]
   return percentages

def questionTuple():
   while True:
      base_num = random.randint(1,N)
      old = random.choice([base_num*i for i in range(1,N)])
      neat_percentages = neatPercentages(old)
      if len(neat_percentages)==0:
         continue
      percent_value = random.choice(neat_percentages)
      direction = (-1)**random.randint(0,1) # (-1)^0 = 1, increase; (-1)^1 = -1, decrease
      if direction==1:
         sign = '+'
      elif direction==-1:
         sign = '-'
      new = old + old*direction*percent_value//aHundred
      questionTuple = {"old": str(old),
                       "+-": sign,
                       "%": str(percent_value),
                       "new": str(new)}
      return questionTuple

correct_count = 0
total_count = 0

# percentage & %∆ questions (in addition to polynomials; a mixed bag) <- new program!
# remember to make QR code

## OLD, NEW, %∆. Given any 2, find the last item.

while True: # infinite loop

   # Generate questions
   change_terms = {"all": [["increased","decreased"], ["incremented","decreased"]],
                   "price": [["risen","fallen"], ["risen","dropped"]],
                   "size": [["enlarged","shrunken"], ["dilated","shrunken"]]}
   quantity_terms = ["number of " + random.choice(["girls in ABC School",
                                                   "number of pineapple buns sold in the morning",
                                                   "seats in Auditorium 501",
                                                   "Instagram followers Holly has",
                                                   "views of Emily's animal documentary",
                                                   "passengers on the 6pm flight to Hong Kong",
                                                   "beds in Rosalie Hospital",
                                                   ]),
                     "size of " + random.choice(["Joanne's rice serving (in g)",
                                                 "the population of Little Community (in thousands)",
                                                 "each card that Fred buys for lunch (in cm^2)",
                                                 "the unknown plant in Gerald's flowerpot (in cm)",
                                                 "ice cream tubs that Donnie sells (in cm^3)",
                                                 "medicine in Dr Bo's capsule (in mg)",
                                                 "the country of Alapaca after their war with Blusaket (in km^3)"
                                                 ]),
                     "price ($) of " + random.choice(["a bottle of guava juice by Walter's Water",
                                                  "a handbag made by Sandy",
                                                  "a pasta bolognaise dish made by Chef John",
                                                  "a cellphone sold by Thomas",
                                                  "a baseball cap from George's shop"
                                                  ]),
                     "volume of " + random.choice(["water in Daisy's swimming pool (in L)",
                                                   "orange juice in Eric's carton (in ml)",
                                                   "wine in Mr Oldman's bottle (in ml)",
                                                   "lavender-scented hand lotion (in ml)",
                                                   "each ceramic bowl made by Nora (in ml)",])
                     ]
   Q = random.choice(quantity_terms)
   if "price" in Q:
      C = random.choice([*change_terms['all'], *change_terms['price']])
   elif "size" in Q:
      C = random.choice([*change_terms['all'], *change_terms['size']])
   else:
      C = random.choice(change_terms['all'])
   change = {"+":C[0],"-":C[1]} # characteristic function
   change_placeholder = "changed"
   quantity_placeholder = "quantity"
   old_placeholder = "X"
   new_placeholder = "Y"
   percentage_placeholder = "P"
   question_format = ["The quantity has changed from X to Y. What is the percentage change?",
                      "The quantity has changed by P% to Y. What is the original quantity?",
                      "The quantity has changed by P% from X. What is the new quantity?"]
   qT = questionTuple()
   qa = [[question_format[0], qT["+-"]+qT["%"]+'%'],
         [question_format[1], qT["old"]],
         [question_format[2], qT["new"]]]
   choice = random.choice(qa)
   question = choice[0]
   answer = choice[1]
   question_display = question.replace(old_placeholder, qT["old"])\
                              .replace(new_placeholder, qT["new"])\
                              .replace(quantity_placeholder, Q)\
                              .replace(change_placeholder, change[qT["+-"]])\
                              .replace(percentage_placeholder, qT["%"])

   print("=== % Percentage Change Answer Format %\n=== increase by 20% = +20%, decrease by 5% = -5% ===")
   print(question_display)
      
   first_try = True
   correct = False
   
   while not(correct):
       y = input("Answer: ")
       x = answer
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
   print('Correct on first attempt: ', correct_count,\
         '\nTotal questions attempted: ', total_count,\
         '\n====================================================')
       

