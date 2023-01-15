class ABC:
  count=7
  def __init__(self):
    self.count=5
    ABC.count +=1

  def getCount(cls):
    return cls.count

print(ABC().getCount())


o/p=5


class Math:
  @staticmethod
  def divide(num1,num2):
    return num1/num2

math=Math()
if(2*2 == math.divide(12,3)):
  print("Equal")
else:
  print("not equal")

o/p=Equal
