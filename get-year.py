import random
from datetime import datetime

availableYears = list(range(1997, datetime.now().year + 1))

def randomYear():
    index = random.randrange(len(availableYears))
    return availableYears.pop(index)

for i in range(len(availableYears)):
    print(randomYear())


# 1999
# 2004
# 2026
# 2000
# 2003
# 2014
# 2008
# 2019
# 2018
# 2011
# 2021
# 2007
# 2010
# 2022
# 2009
# 2001
# 2013
# 2023
# 1997
# 2006
# 1998
# 2025
# 2012
# 2020
# 2002
# 2015
# 2005
# 2016
# 2017
# 2024