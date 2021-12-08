import math

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return (2 * self.height) + (2 * self.width)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5


  def get_picture(self):
    
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    picture = ''
    for i in range(self.height):
      for j in range(self.width):
        picture += "*"
      picture += '\n'
    return picture

  def get_amount_inside(self, testObject): 
    widthCount = math.floor((self.width/testObject.width))
    heightCount = math.floor((self.height/testObject.height))
    return heightCount * widthCount

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
  def __init__(self, width):
    super().__init__(width, width)

  def set_side(self, length):
    self.width = length
    self.height = length
  
  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)

  def __str__(self):
    return f'Square(side={self.width})'

