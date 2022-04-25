class Rectangle:
  def __init__(self, x, y, h, w):
    '''
      Initializes rectangle object
    
      x (int): x value of rectangle (+)
      y (int): y value of rectangle (+)
      height (int): height of rectangle (+)
      width (int): width of rectangle (+)

      return: None
    '''
    self.x = x
    self.y = y
    self.height = h
    self.width = w
    
    if x < 0:
      self.x = 0
      
    if y < 0:
      self.y = 0
      
    if h < 0:
      self.height = 0
      
    if w < 0:
      self.width = 0
      