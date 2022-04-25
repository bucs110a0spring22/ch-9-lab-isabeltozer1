import Rectangle

class Surface:
  def __init__(self, filename, x, y, h, w):
    '''
      initializes Surface object by using Rectangle object

      filename (string): name of file
      x (int): x value of rectangle (+)
      y (int): y value of rectangle (+)
      height (int): height of rectangle (+)
      width (int): width of rectangle (+)

      return: None
    '''
    self.rect = Rectangle.Rectangle(x, y, h, w)
    self.image = filename

  def getRect(self):
    '''
      Returns Rectangle object of Surface object

      return: (Rectangle)
    '''
    return self.rect