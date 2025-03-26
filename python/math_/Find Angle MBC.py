# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = float(input())
bc = float(input())

# In a right triangle, since M is the midpoint, AM=BM=CM
# Therefore angle BMC is equal to angle MCB
angle = math.atan(ab/bc)
print(f"{round(math.degrees(angle))}{chr(176)}")
