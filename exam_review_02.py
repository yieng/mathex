import random
import math

success = ['✅','✔️','💯','🎯','🏆','🎉','🤗','🥳','😎','🥇','💥','💖','🔥','❤️','⭐','🙌']
try_again = ['🤔','💪','🧐']

correct_count = 0
total_count = 0

# charts & stats: stem and leaf diagram, frequency distribution tables, mean, median, mode

# Q9. The stem-and-leaf diagram below shows the marks of S1A students in a Science test.

def question():

    # create a suitable stem-and-leaf diagram
    count = 0
    while True:
        N_tens = random.randint(3,8)
        N = N_tens*10 # number of data
        delimiter = N//2
        
        data = [random.randint((N-delimiter)//2,(N+delimiter)//2) for d in range(0,N)]
        data.sort()

        stems_all = [d//10 for d in data]
        stems = list(set(stems_all))
        leaves = [d%10 for d in data]

        i = 0
        stem_length = len(stems)
        num_of_leaves = [0 for s in stems]
        rows_of_leaves = []
        for s in stems:
            row_of_leaves = []
            while True:
                row_of_leaves.append(str(leaves[i]))
                num_of_leaves[stems.index(s)] += 1
                i += 1
                if (i==len(leaves)):
                    break
                elif (leaves[i]<leaves[i-1]):
                    break
            rows_of_leaves.append(row_of_leaves)

        count += 1
        if (stem_length>=max(3,N_tens) and max(num_of_leaves)<=N//stem_length*(stem_length-1)):
            break
        if count>10:
            continue

    q_format = f"The stem-and-leaf diagram below shows the quantity of {N} subjects in an important survey:"

    quantities = ['marks', 'scores', 'volumes', 'heights', 'weights', 'temperatures', 'pressures', 'speeds', 'distances', 'times', 'frequencies', 'amplitudes', 'wavelengths', 'energies', 'forces', 'torques', 'moments', 'accelerations', 'velocities', 'capacities', 'resistances', 'inductances', 'conductances', 'concentrations', 'yields', 'ratios', 'proportions', 'percentages', 'grades', 'ratings', 'levels', 'intensities', 'fluxes', 'densities', 'viscosities', 'conductivities', 'permeabilities', 'lengths', 'widths', 'depths', 'areas', 'volumes', 'masses', 'flow rates', 'powers', 'times', 'prices', 'costs', 'magnitudes', 'altitudes']
    quantity = ['mark', 'score', 'volume', 'height', 'weight', 'temperature', 'pressure', 'speed', 'distance', 'time', 'frequency', 'amplitude', 'wavelength', 'energy', 'force', 'torque', 'moment', 'acceleration', 'velocity', 'capacity', 'resistance', 'inductance', 'conductance', 'concentration', 'yield', 'ratio', 'proportion', 'percentage', 'grade', 'rating', 'level', 'intensity', 'flux', 'density', 'viscosity', 'conductivity', 'permeability', 'length', 'width', 'depth', 'area', 'volume', 'mass', 'flow rate', 'power', 'time', 'price', 'cost', 'magnitude', 'altitude']
    subjects = ['students', 'athletes', 'buildings', 'mountains', 'trucks', 'patients', 'weather stations', 'airplanes', 'runners', 'cities', 'radio stations', 'speakers', 'microscopes', 'power plants', 'construction sites', 'engines', 'vehicles', 'cyclists', 'swimmers', 'warehouses', 'electronic devices', 'resistors', 'chemical plants', 'laboratories', 'crops', 'businesses', 'governments', 'schools', 'hospitals', 'airports', 'seismometers', 'light bulbs', 'thermometers', 'dams', 'pipelines', 'computers', 'servers', 'roads', 'tunnels', 'bridges', 'factories', 'storage tanks', 'rockets', 'rivers', 'generators', 'transformers', 'wind turbines', 'solar panels', 'earthquakes', 'volcanoes']
    survey = ['exam', 'test', 'survey', 'questionnaire', 'quiz', 'assessment', 'evaluation', 'interview', 'poll', 'opinion', 'feedback form', 'rating', 'review', 'investigation', 'inquiry', 'research study', 'study', 'analysis', 'audit', 'check', 'inspection', 'appraisal', 'measurement', 'observation', 'monitoring', 'tracking', 'follow-up', 'checklist', 'inventory', 'census', 'headcount', 'tally', 'score', 'assessment', 'ranking', 'grade', 'marking', 'appraisement', 'valuation', 'estimate', 'projection', 'forecast', 'prediction', 'diagnostic', 'screening', 'assessment', 'review', 'audit', 'investigation', 'proposal']
    standards = ['standard',  'quality', 'passing', 'operating', 'target', 'compliance', 'threshold', 'success', 'tolerance', 'performance', 'breaking', 'critical', 'expected', 'optimal', 'benchmark']
    q0 = random.choice(quantities)
    q1 = quantity[quantities.index(q0)]
    s0 = random.choice(subjects)
    s1 = random.choice(survey)
    s2 = random.choice(standards)
    q_description = q_format.replace('quantity',q0)\
                            .replace('subjects',s0)\
                            .replace('survey',s1)
    print(q_description)
    print('Stem (tens) | Leaves (units)')

    for s in stems:
        print(str(s).rjust(11-len(str(s))),' | ', ' '.join(rows_of_leaves[stems.index(s)]))    

    passing_score = random.randint(delimiter-5,delimiter+5)
    coin = random.randint(0,1)
    if coin == 1: # success
        q_format1 = f"If the passing score is {passing_score}, how many subjects achieved this score?"
        q_statement = q_format1.replace('passing',s2)\
                               .replace('score',q1)\
                               .replace('subjects',s0)
        print(q_statement)
    else: # failure
        q_format2 = f"If the passing score is {passing_score}, how many subjects failed to achieve this score?"
        q_statement = q_format2.replace('passing',s2)\
                               .replace('score',q1)\
                               .replace('subjects',s0)
        print(q_statement)

    # now to generate and return the answers
    if coin == 1:
        answer = len([d for d in data if d >= passing_score])
    else:
        answer = len([d for d in data if d < passing_score])
    return str(answer)

# remember to make QR code

while True: # infinite loop

   # Generate questions
   answer = question()
   
   #print(question)
      
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
       

