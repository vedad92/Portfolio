class Person():
   
    def __init__(self, name, age):
        # Assign instance attributes
        self.name = name
        self.age = age

alice = Person('Alice', 20)

print(alice.age)

class Player():
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

        for value in [speed, endurance, accuracy]:
            if 0 >= value >= 1:
                raise ValueError

    def introduce(self):
        return print(f"Hello everyone, my name is {self.name}")


    def strength(self):
        if self.speed > self.endurance and self.speed > self.accuracy:
            return('speed', self.speed)

        if self.endurance > self.speed and self.endurance > self.accuracy:
            return('endurance', self.endurance)

        if self.accuracy > self.speed and self.accuracy > self.endurance:
            return('accuracy', self.accuracy)

        elif self.speed == self.endurance == self.accuracy:

            return('speed', self.speed)   

        elif self.endurance == self.accuracy:
            return ('endurance', self.endurance)    


bob = Player("Bob", 0.8, 0.5, 0.3)
jan = Player("Jan", 0.3, 0.7, 0.7)
bob.introduce()
print(bob.strength())
print(jan.strength())

class Commentator():

    def __init__(self, name):
        self.name = name
        return print(f'Hello {name}')

    def sum_player(self, player):
        speed = getattr(player, 'speed')
        endurance = getattr(player, 'endurance')
        accuracy = getattr(player, 'accuracy')
        return speed + endurance + accuracy


    def compare_players(self, player1, player2, attribute):
        speed1 = getattr(player1, 'speed')
        endurance1 = getattr(player1, 'endurance')
        accuracy1 = getattr(player1, 'accuracy')
        speed2 = getattr(player2, 'speed')
        endurance2 = getattr(player2, 'endurance')
        accuracy2 = getattr(player2, 'accuracy')
        
        if attribute == 'speed':
            if speed1 > speed2:
                return getattr(player1, 'name')
            
            elif speed1 == speed2:
                return 

            else:
                return getattr(player2, 'name') 
        
        if attribute == 'endurance':
            if endurance1 > endurance2:
                return getattr(player1, 'name')
            
            elif endurance1 == endurance2:

            else:
                return getattr(player2, 'name')    
        if attribute == 'accuracy':
            if accuracy1 > accuracy2:
                return getattr(player1, 'name')

            elif accuracy1 == accuracy2:
                return 
            else:
                return getattr(player2, 'name') 

print(Commentator('Henk Hudson').compare_players(bob, jan, 'speed'))
