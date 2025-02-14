from data1 import data1
from data2 import data2
from data3 import data3
from data4 import data4
from data5 import data5


grid1 = data1()
grid2 = data2()
grid3 = data3()
grid4 = data4()
grid5 = data5()
# False
print("Test 1:")
print(grid1.is_goal_state())
# True
print("Test 2:")
print(grid2.is_goal_state())
# Loop
print("Test 3:")
print(grid3.is_goal_state())
# True
print("Test 4:")
print(grid4.is_goal_state())
# Loop
print("Test 5:")
print(grid5.is_goal_state())