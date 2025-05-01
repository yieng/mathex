import random
import math

success = ['✅','✔️','💯','🎯','🏆','🎉','🤗','🥳','😎','🥇','💥','💖','🔥','❤️','⭐','🙌']
try_again = ['🤔','💪','🧐']

correct_count = 0
total_count = 0

# Q1. A box contains 10 red cards and 90 yellow cards. What % of cards in the box are red?

def q1_tuple():
    N = random.randint(1,10)*100
    x = random.randint(1,N)
    y = N-x
    pa = round(x/N*100,1)
    pb = round(y/N*100,1)
    return [x,y,pa,pb]

def q1_generator(x,y):
    containers = ['box','container','suitcase','bag','trolley','trunk','truck','luggage','wheelbarrow']
    items = ['books', 'magazines', 'cards', 'dolls', 'stuffed animals', 'cups', 'water bottles', 'cookies', 'energy bars', 'tennis balls', 'sweatshirts', 'hats', 'scarves', 'gloves', 'umbrellas', 'pillows', 'blankets', 'headphones', 'earbuds', 'phone chargers', 'portable chargers', 'laptops', 'tablets', 'e-readers', 'cameras', 'snack bags', 'fresh fruit', 'nuts', 'dried fruit', 'granola bars', 'crackers', 'sandwiches', 'wraps', 'trail mix', 'candy', 'gum', 'mints', 'medicines', 'first aid kits', 'eye masks', 'earplugs', 'toothbrushes', 'hairbrushes', 'deodorant', 'lip balm', 'tissues', 'wet wipes', 'small toys', 'playing cards', 'board games']

    q1_template = f"A container contains {x} item_a and {y} item_b. What percentage of objects in the container are item_a?"
    q1a = q1_template.replace('container',random.choice(containers))\
         .replace('item_a',random.choice(items))\
         .replace('item_b',random.choice(items))
    q1_template = f"A container contains {x} item_a and {y} item_b. What percentage of objects in the container are item_b?"
    q1b = q1_template.replace('container',random.choice(containers))\
         .replace('item_a',random.choice(items))\
         .replace('item_b',random.choice(items))
    return [q1a, q1b]



# percentage & %∆ questions (in addition to polynomials; a mixed bag) <- new program!
# remember to make QR code

## OLD, NEW, %∆. Given any 2, find the last item.

while True: # infinite loop

   # Generate questions
   t1 = q1_tuple()
   coin = random.randint(0,1)
   question = q1_generator(t1[0], t1[1])[coin]
   answer = str(t1[2::][coin]).replace('.0','')+'% '

   print("=== Your answers should be rounded up to one decimal place. ===")
   print("=== % Percentage Change Answer Format %\n=== increase by 20% = +20% <- add an extra space before you press ENTER\n=== decrease by 5% = -5% <- add an extra space after '%' ===")
   print(question)
      
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
       

