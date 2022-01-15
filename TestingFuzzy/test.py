import numpy as np
from numpy.lib.function_base import average
import skfuzzy as fuzz
from skfuzzy import control as ctrl





numPerson = ctrl.Antecedent(np.arange(0,12,1), 'numPerson')           # making the intervale 
speedChange = ctrl.Antecedent(np.arange(0,12,1), 'speedChange')# of the values
#timeObjAb = ctrl.Antecedent(np.arange(0,6,1), 'timeObjAb')
tip = ctrl.Consequent(np.arange(0,101,1), 'tip')

numPerson.automf(3)   # divising the values of
speedChange.automf(3) # the variables to three (poor, average, good)
#timeObjAb.automf(3)

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 30])
tip['medium'] = fuzz.trimf(tip.universe, [30, 60, 60])
tip['high'] = fuzz.trimf(tip.universe, [60, 100, 100])


#numPerson.view()
# making simple rules
rule1 = ctrl.Rule(numPerson['poor'] & speedChange['poor'], tip['low'])
rule2 = ctrl.Rule(numPerson['average'] & speedChange['average'], tip['medium'])
rule3 = ctrl.Rule(numPerson['good'] | speedChange['good'], tip['high'])



tipping_ctrl = ctrl.ControlSystem([rule1,rule2,rule3]) #just test comment!!

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['numPerson'] = float(input('Enter the number of person:  '))  # we are going to change here cause we need the values
tipping.input['speedChange'] = float(input('Enter the speed of change:  '))# from the videos just for testing i used input() function!
#tipping.input['timeObjAb'] = float(input())


tipping.compute()




print('The result of calculating:   ',tipping.output['tip']) # the result is a float value 

    