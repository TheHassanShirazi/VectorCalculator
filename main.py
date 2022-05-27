import math


response = input("What do you want to calculate? (Type help for possible inputs) ")


def findLength(vector):
    sum = 0.0
    for i in vector:
        sum += float(i) ** 2
    length = sum ** 0.5
    return length


def addVectors(vector1, vector2):
    added = vector1[0] + vector2[0], vector1[1] + vector2[1], vector1[2] + vector2[2]
    return added


def multiplyByConstant(vector1, constant):
    constant = float(constant[0])
    product = vector1[0] * constant, vector1[1] * constant, vector1[2] * constant
    return product


def angleBetween(vector1, vector2):
    sum1 = 0.0
    sum2 = 0.0
    angle = 0.0
    dotproduct = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
    for i in vector1:
        sum1 += float(i) ** 2
    length1 = sum1 ** 0.5
    for i in vector2:
        sum2 += float(i) ** 2
    length2 = sum2 ** 0.5
    angle = math.acos(dotproduct / (length1 * length2))
    angle = (angle * 180) / math.pi
    return angle


def dotProduct(vector1, vector2):
    dotproduct = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
    return dotproduct


def crossProduct(vector1, vector2):
    crossproduct = vector1[1]*vector2[2] - vector1[2]*vector2[1], vector1[0]*vector2[2] - vector1[2]*vector2[0], vector1[0]*vector2[1] - vector1[1]*vector2[0]
    return crossproduct


newres1 = response.split("[")[1].split("]")[0].split(",")

if "and" in response:
    newres2 = response.split("and ")[1].split("[")[1].split("]")[0].split(",")
else:
    pass

newres1 = [float(i) for i in newres1]
newres2 = [float(i) for i in newres2]


response = response.lower()

if response.startswith("help"):
  print("'Find length [vector], Add [vector] and [vector], Multiply [vector] and [constant]'")

elif response.startswith("length of"):
    print(findLength(newres1))

elif response.startswith("add"):
    print(addVectors(newres1, newres2))

elif response.startswith("multiply"):
    print(multiplyByConstant(newres1, newres2))

elif response.startswith("angle between"):
    print(angleBetween(newres1, newres2))

elif response.startswith("dot product of"):
    print(dotProduct(newres1, newres2))

elif response.startswith("cross product of"):
    print(crossProduct(newres1, newres2))

else:
    pass
