import random
from datetime import datetime

def randomYear():
    startYear = 1997
    boundaryYear = datetime.now().year - 1
    return  random.randint(startYear, boundaryYear)


print(randomYear())