
class Clock:

  def __init__(self, hour, minute):
    self.minutes = hour % 24 * 60 + minute 

  def __str__(self):
    return "{:02d}:{:02d}".format(*self.calc())

  def __eq__(self, other):
    return self.calc() == other.calc()

  def calc(self):
    minute = self.minutes % 60
    hour = self.minutes // 60 % 24
    return hour, minute
    
  def add(self, n):
    self.minutes += n
    return self.__str__()
