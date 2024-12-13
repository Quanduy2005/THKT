print("Sinh vien: Nguyen Duy Quan")
print("Ma so SV:235752021610107")
print("**************************")

class Hinhchunhat(object): 
   def __init__(self, dai, rong): 
      self.dai = dai
      self.rong = rong
############################### 
   def area(self): 
      return self.dai * self.rong
aHinhchunhat= Hinhchunhat(4, 5) 
print (aHinhchunhat.area())
