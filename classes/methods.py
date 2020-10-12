class Circle:

    pi = 3.14
    def __init__(self, radius = 1):
      self.radius = radius
    
    def get_area(self):
        return self.pi*self.radius**2


circle1 = Circle(12)

print(circle1.get_area())