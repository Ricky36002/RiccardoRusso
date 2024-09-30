#1)domanda
#a) False, b) True, c) True, d) True

#2)Domanda
def transform(x: int) -> int:
    if x % 2 == 0:
        x /= 2
    else:
        x*=3
        x-= 1 
    return x

#3)Domanda


#4)Domanda
def print_seq(): 
    
    print("Sequenza a):")
    for i in range(1, 8):
        print(i)
    print()
    print("Sequenza b):")
    for i in range(3, 28, 5):
        print(i)
    print()

    print("Sequenza c):")
    for i in range(20, -16, -6):
        print(i)
    print()    
    print("Sequenza d):")
    for i in range(19, 59, 8):
        print(i)
    
    return

#5)Domanda
def integerPower(base, exponent):
    result = 1  
    for _ in range(exponent):
        result *= base  
    return result

#6)Domanda
import math

def hypotenuse(a: float, b: float) -> float:
    return math.sqrt(a**2 + b**2)

#7)Domanda


#8)Domanda


#9)Domanda


#10)Domanda







#coso zoo
# Example usage
#zoo = Zoo()
#keeper = ZooKeeper(name="Lorenzo", surname="Maggi", id=1234)
#zoo.add_zoo_keeper(keeper)

#fence = Fence(area=100, temperature=25, habitat="Continent")
#zoo.add_fence(fence)

#animal1 = Animal(name="Scoiattolo", species="Blabla", age=25, height=0.5, width=0.2, preferred_habitat="Continent")
#animal2 = Animal(name="Lupo", species="Lupus", age=14, height=1.0, width=0.5, preferred_habitat="Continent")

#zoo.add_animal(animal1, fence)
#zoo.add_animal(animal2, fence)

#zoo.describe_zoo()