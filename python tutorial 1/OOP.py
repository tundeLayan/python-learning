# object is a specific instance of a class

class Human:
  # constructor
  def __init__(self, name, occupation, age):
    self.name = name
    self.occupation = occupation
    self.age = age

  def do_work(self):
    if self.occupation == "tennis player":
      print(self.name, "plays tennis")
    elif self.occupation == 'actor':
      print(self.name, "shoots a film")

  def speaks(self):
    print(self.name, "says how are you?")


tom = Human('tom cruise', "actor", 29)
tom.do_work()
tom.speaks()