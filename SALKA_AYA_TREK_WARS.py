import unittest
import math


class alignment:
    def __init__(self):
        self.us = 1
        self.them = 2
        self.chaotic = 3
              
class Ship:
    def __init__(self, name = "Ship", align = alignment().chaotic, x_location = 0, y_loc = 0, range = 0, max_health = 0, attack_power = 0, current_health = 0):
        self.name = name
        self.align = align
        self.x_location = x_location
        self.y_loc = y_loc
        self.range = range
        self.current_health = current_health
        self.attack_power = attack_power
        self.max_health = max_health
            
    def attack(self, Ship): 
        pass
    def getType(self): 
        return ""
    def getX(self):
        return self.x_location
    def getY(self):
        return self.y_loc
    def getAlign(self):
        return self.align

    def status(self):
        status = ""
        status += "Name: " + self.name
        status += " Type: " + self.getType() + " "  
        status += "Health: " + str(self.current_health) + " " 
        status += "Location: (" + str(self.x_location) + "," + str(self.y_loc) + ")"  
        if self.getType() == "BattleShip":
            print("Torpedos: ", self.torpedos)
        return status
    def move(self): 
        pass  
    def change_alignment(self, align_new):
        self.align = align_new
        return align_new
    def assess_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        elif self.current_health > self.max_health:
            self.current_health = self.max_health

    def if_its_in_range(self, enemy):
        num_of_range = math.sqrt((self.x_location - enemy.x_location)**2 + (self.y_loc - enemy.y_loc)**2)
        if num_of_range <= enemy.range:
            return 1 # In range
        elif num_of_range > enemy.range:
            return 0  # Out of range
            
class Battle(Ship):
    def __init__(self, name, align, x_location, y_loc):
        super().__init__(name, align, x_location, y_loc, 10, 10, 100)
        self.torpedos = 10

    def getType(self):
        return "BattleShip"

    def move(self):
            self.x_location = self.x_location-1
            self.y_loc = self.y_loc-1
            
            if self.current_health < self.max_health:
                self.current_health = self.current_health + 1

    def attack(self, enemy):
            if self.if_its_in_range(enemy): 
                 if (self.align != enemy.align):
                     if self.torpedos > 0:
                         self.torpedos = self.torpedos -1
                         enemy.current_health = enemy.current_health - 10
   
    
      

class Cruiser(Ship):
    def __init__(self, name, align, x_location, y_loc):
        super().__init__(name, align, x_location, y_loc, 50, 50, 5)

    def move(self):
        self.x_location += 1
        self.y_loc += 2
        
        if self.current_health < self.max_health:
            self.current_health += 1

    def attack(self, enemy):
        if self.if_its_in_range(enemy):
            if (self.align != enemy.align):
                    enemy.current_health -= 5

    def getType(self):
        return "Cruiser"

class Corvette(Ship):
    def __init__(self, name, align, x_location, y_loc):
        super().__init__(name, align, x_location, y_loc, 25, 20)

    def move (self):
        self.x_location += 5
        self.y_loc += 5

        if self.current_health < self.max_health:
            self.current_health += 1

    def attack(self, enemy):
        align = alignment()
        if self.if_its_in_range(enemy):
            if enemy.align == align.us and self.align == align.them:
                enemy.align = align.them
            elif enemy.align == align.them and self.align == align.us:
                enemy.align = align.us

    def getType(self):
        return "Corvette"

class Repair(Cruiser):
    def __init__(self, name, align, x_location, y_loc):
        super().__init__(name, align, x_location, y_loc)
       
    def attack (self, enemy):
            if self.align == enemy.align:
                enemy.current_health = self.max_health

    def getType(self):
        return "Repairship"



def main():
        b = Battle("Santa", "us", 1, 2)
        b.current_health = 10
        b.range = 10
        status = b.status()
        print(status)
      


class TestShips(unittest.TestCase):     
    def test_ship_init(self):
        align = alignment()
        test_ship = Ship("TestShip", align.us , 10, 20, 15, 100, 10, 50)
        self.assertEqual(test_ship.name, "TestShip")
        self.assertEqual(test_ship.align, align.us)
        self.assertEqual(test_ship.x_location, 10)
        self.assertEqual(test_ship.y_loc, 20)
        self.assertEqual(test_ship.range, 15)
        self.assertEqual(test_ship.current_health, 50)
        self.assertEqual(test_ship.attack_power, 10)
        self.assertEqual(test_ship.max_health, 100)


    def test_battle_getType(self):
        align = alignment()
        test_battle = Battle("Santa", align.them, 3, 4)
        test_battle.getType()
        self.assertEqual(test_battle.getType(), "BattleShip")

    def test_cruiser_getType(self):
        align = alignment()
        test_cruiser = Cruiser("Vixen", align.them, 4, 5)
        test_cruiser.getType()
        self.assertEqual(test_cruiser.getType(), "Cruiser")

    def test_corvette_getType(self):
        align = alignment()
        test_corvette = Corvette("Dasher", align.chaotic, 5, 6) 
        test_corvette.getType()
        self.assertEqual(test_corvette.getType(), "Corvette")

    def test_repair_getType(self):
        align = alignment()
        test_repair = Repair("Prancer", align.us, 8, 2)
        test_repair.getType()
        self.assertEqual(test_repair.getType(), "Repairship")

    def test_x_and_y(self):
        align = alignment()
        test_ship = Ship("Rudolph", align.us, 1, 2)
        test_repair = Repair("Prancer", align.us, 8, 2)
        test_battle = Battle("Santa", align.them, 3, 4)
        test_battle.move()
        self.assertEqual(test_battle.getX(), 2)   
        self.assertEqual(test_battle.getY(), 3)
        test_cruiser = Cruiser("Vixen", align.them, 4, 5)
        test_cruiser.move()
        self.assertEqual(test_cruiser.getX(), 5)
        self.assertEqual(test_cruiser.getY(), 7)
        test_corvette = Corvette("Dasher", align.chaotic, 5, 6) 
        test_corvette.move()
        self.assertEqual(test_corvette.getX(), 10)
        self.assertEqual(test_corvette.getY(), 11)

    def test_battle_if_its_in_range(self): 
        align = alignment()
        test_battle = Battle("Santa", align.them, 3, 4)
        test_enemy = Battle("Enemy", align.us, 4, 5)
        self.assertEqual(test_battle.if_its_in_range(test_enemy), 1)

    def test_cruiser_if_its_in_range(self): 
        align = alignment()
        test_cruiser = Cruiser("Vixen", align.them, 4, 5)
        test_enemy = Cruiser("Enemy", align.us, 6, 9)
        self.assertEqual(test_cruiser.if_its_in_range(test_enemy), 1)

    def test_corvette_if_its_in_range(self):
        align = alignment() 
        test_corvette = Corvette("Dasher", align.chaotic, 5, 6)
        test_enemy = Corvette("Enemy", align.us, 6, 9)
        self.assertEqual(test_corvette.if_its_in_range(test_enemy), 1)

    def test_ship_getAlign(self):
        align = alignment()
        test_ship = Ship("Rudolph", align.us, 1, 2) 
        self.assertEqual(test_ship.getAlign(), align.us)

    def test_ship_assess_damage_health_doesnt_go_below_zero(self):
        align = alignment()
        test_ship = Ship("Rudolph", align.us, 1, 2)
        test_ship.assess_damage(100) 
        self.assertEqual(test_ship.current_health, 0 )

    def test_battle_inherits_from_ship(self):
        align = alignment()
        test_ship = Ship("Rudolph", align.us, 1, 2)
        test_battle = Battle("Santa", align.them, 3, 4)
        self.assertIsInstance(test_ship, Ship)
        self.assertIsInstance(test_battle, Battle)

    def test_cruiser_inherits_from_ship(self):
        align = alignment()
        test_ship = Ship("Rudolph", align.us, 1, 2)
        test_cruiser = Cruiser("Vixen", align.them, 4, 5)
        self.assertIsInstance(test_ship, Ship)
        self.assertIsInstance(test_cruiser, Cruiser) 

    def test_corvette_inherits_from_ship(self):
        align = alignment()
        test_ship = Ship("Rudolph", align.us, 1, 2)
        test_corvette = Corvette("Dasher", align.chaotic, 5, 6)
        self.assertIsInstance(test_ship, Ship)
        self.assertIsInstance(test_corvette, Corvette)

    def test_repair_inherits_from_cruiser(self):
        align = alignment()
        test_repair = Repair("Prancer", align.us, 8, 2)
        test_cruiser = Cruiser("Vixen", align.them, 4, 5)
        self.assertIsInstance(test_cruiser, Cruiser)
        self.assertIsInstance(test_repair, Repair)

    def test_ship_getX(self):
        align = alignment()
        test_ship = Ship("Rudolph", align.us, 1, 2)
        self.assertEqual(test_ship.getX(),1)

    def test_ship_getY(self):
        align = alignment()
        test_ship = Ship("Rudolph", align.us, 1, 2)
        self.assertEqual(test_ship.getY(),2)

    def test_ship_status(self):
        align = alignment()
        test_ship = Ship("Rudolph", align.us, 1, 2)
        self.assertEqual(test_ship.status(), "Name: Rudolph Type:  Health: 0 Location: (1,2)")

    def test_ship_change_alignment(self): 
        align = alignment()
        test_ship = Ship("Rudolph", align.us, 1, 2)
        align_new = Ship("Rudolph", align.them, 1, 2)
        self.assertEqual(test_ship.change_alignment(align_new), align_new) 

    def test_battle_increase_health_by_one(self):
       align = alignment()
       test_battle = Battle("Santa", align.them, 3, 4)
       current_health = test_battle.current_health
       test_battle.move()
       self.assertEqual(test_battle.current_health, current_health + 1)

    def test_battle_attack_torpedos_one_less_torpedo(self):
        align = alignment()
        test_battle = Battle("Santa", align.us, 3, 4)
        test_enemy = Battle("Enemy", align.chaotic, 2, 3)
        torpedos = test_battle.torpedos
        range = test_battle.range
        test_battle.attack(test_enemy)
        self.assertEqual(test_battle.torpedos, torpedos - 1)

    def test_battle_damage_ten(self):
        align = alignment()
        test_battle = Battle("Santa", align.us, 3, 4)
        test_enemy = Battle("Enemy", align.chaotic, 2, 3)
        current_health = test_enemy.current_health
        test_battle.attack(test_enemy)
        self.assertEqual(test_enemy.current_health, current_health - 10)

    def test_cruiser_attack(self):
        align = alignment()
        test_cruiser = Cruiser("Vixen", align.them, 4, 5)
        test_enemy = Battle("Enemy", align.chaotic, 2, 3)
        current_health = test_enemy.current_health
        test_cruiser.attack(test_enemy)
        self.assertEqual(test_enemy.current_health, current_health - 5)

    def test_corvette_attack(self):
        align = alignment()
        test_corvette = Corvette("Dasher", align.us, 5, 6)
        test_enemy = Corvette("Enemy", align.them, 2, 3)
        test_corvette.attack(test_enemy)
        self.assertEqual(test_enemy.align, align.us ) 

    def test_repair_attack(self):
        align = alignment()
        test_repair = Repair("Prancer", align.us, 8, 2)
        test_enemy = Battle("Prancer", align.us, 8, 2)
        test_repair.attack(test_enemy)
        self.assertEqual(test_enemy.current_health, test_repair.max_health)

    def test_main(self):
        main()