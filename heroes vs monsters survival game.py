import sys
import time
import random
import numpy as np

        
    #class of fighters
class heroes:
    def __init__(self, name,location, types, attack_Move, EVs, HP):
        ###makes things in class have those variables
        self.name = name
        self.location = location
        self.types = types #ranged or melee
        self.attack_Move = attack_Move
        self.damage = EVs['DAMAGE']
        self.defense = EVs['DEFENSE']
        self.HP = HP #health
                
    def battle(self, enemy):
        print(f"--You have encountered a {self.types} attacker on your journey!!!--")
        print(f"\n{self.name}")
        print(f"Position is {self.location}")
        print("DAMAGE/", self.damage)
        print("DEFENSE/", self.defense)
        print("\nVS")
        time.sleep(1)
 ### below is your character information
        print(f"\n{enemy.name}")
        print(f"position is {enemy.location}")
        print("DAMAGE/", enemy.damage)
        print("DEFENSE/", enemy.defense)
        time.sleep(1)

        distance = self.location - enemy.location
        if self.types == 'melee':
            self.damage = self.damage/(abs(distance))  ### 0 is there as there will be a chance to miss
        else:
            self.damage = self.damage*abs(distance) ### damage scaled based on distance between hero and enemy
        if enemy.types == 'melee':
            enemy.damage = enemy.damage/(abs(distance))
        else:
            enemy.damage = rangedAttack2 = enemy.damage*abs(distance)  
        

       

    
        
### battle script
        
        if (self.HP > 0) and (enemy.HP > 0):
            print(f"{self.name} - HP = {self.HP}")
            print(f"{enemy.name} - HP = {enemy.HP}")
             
            print(f"{self.name} choose a move")
            choice_self =input("attack (1) or heal (2)")
            if int(choice_self) == 1:
                print(f"{self.name} attacked using {self.attack_Move} ")
                enemy.HP = enemy.HP - self.damage
            else:
                self.HP = self.HP + self.defense
            
            if enemy.HP <= 0:
                print("enemy was killed \n congratulations")
                return
            
            else:
                print(f"{enemy.name} choose a move")
                choice_enemy =input("attack (1) or heal (2)")
                if int(choice_enemy) == 1:
                   print(f"{enemy.name} attacked using {enemy.attack_Move}")
                   self.HP = self.HP - enemy.damage
                else:
                    enemy.HP = enemy.HP + enemy.defense

            if self.HP <= 0:
                print(" you have died")
                return
            

if __name__ == '__main__':
    #create attacker
    warrior1 = heroes('Warrior',random.randint(1,100), 'Melee','slash',{'DAMAGE':float(10),'DEFENSE':float(30)}, float(100) )
    warrior2 = heroes('Warrior_enemy',random.randint(1,100), 'Melee','slash',{'DAMAGE':float(10),'DEFENSE':float(30)}, float(100) )




