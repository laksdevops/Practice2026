class Flower:
    def __init__(self, color):
        self.color = color


flower = Flower("red")

print(flower.__dict__)

# Add a new property
flower.height = 10

print(flower.__dict__)



# class Car:

#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     def start(self):
#         print("Car started")

#     def stop(self):
#         print("Car stopped")

# car1 = Car("Black", "BMW")
# car2 = Car("red", "Audi")

# class Flower:
#     stem = 'green'
#     def __init__(self, petals=True, thorns=False):
#         self.petals = petals
#         self.thorns = thorns

# flower = Flower()
# print(type(flower.__dict__))

