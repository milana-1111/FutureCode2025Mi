from math import ceil, floor

x = 7.3
y = 2.8
result = ceil(x) + floor(y)
print(result)

from math import ceil, sqrt
from random import randint
import time
start = time.time()
num = randint(20, 30)
root = sqrt(num)
rounded = ceil(root)
end = time.time()
result = rounded + int((end - start) * 1000)
print(result)
