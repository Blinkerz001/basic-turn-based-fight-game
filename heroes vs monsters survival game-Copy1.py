#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import sys
import time
import random
import numpy as np


# In[4]:


###this function prints words one letter at a time - copied from google
###https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line

def delay_print(s):
    for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
        
    #class of fighters
class heroes:
    def __init__(self, name, types, attack_Move, EVs, health='=========='):
        ###makes things in class have those variables
        self.name = name
        self.types = types #ranged or melee
        self.attack_Move = attack_Move
        self.damage = EVs['DAMAGE']
        self.defense = EVs['DEFENSE']
        self.hp = 50 #health points left - 50hp is the default
                
def battle(self, heroes2):
    print(f"--You have encountered a {self.type} attacker on your journey!!!--")
    print(f"\n{self.name}")
    print("DAMAGE/", self.damage)
    print("DEFENSE/", self.defense)
    print("LVL/", 5*(1+np.mean([self.damage, self.defense])))
    print("\nVS")
 ### below is your character information - used in battle
    print(f"\n{heroes2.name}")
    print("DAMAGE/", heroes2.damage)
    print("DEFENSE/", heroes2.defense)
    print("LVL/", 5*(1+np.mean([heroes2.damage, heroes2.defense])))
    time.sleep(2)
    
    rangedAttack = [0,self.damage*abs(distance_between_fighters)] ### damage scaled based on distance between hero and enemy
    meleeAttack = [0,self.damage/(abs(distance_between_fighters))] ### 0 is there as there will be a chance to miss
    
### battle script
    if (self.hp > 0) and (heroes2.hp > 0):
        print(f"{self.name} -- HP = {self.hp}")
        print(f"{heroes2.name} -- HP = {heroes2.hp}")

    

    

        ### distance_between_fighters -- need to define this function. should be random start but can be reduced or increased by skipping a turn
        ### abs value of x1 - x2 + abs value of y1 - y2 

        
        ### option on moving closer to opponent or further away
   


# In[ ]:





# In[ ]:




