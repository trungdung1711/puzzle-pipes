from .data1 import data1
from .data2 import data2
from .data3 import data3
from .data4 import data4
from .data5 import data5
from .data6 import data6
from .data7 import data7
from .data8 import data8
from .data9 import data9
from .data10 import data10
from .data11 import data11
from .data12 import data12
from .data13 import data13
from .data14 import data14
from .data15 import data15
from .data16 import data16
from .data17 import data17
from .data18 import data18
from .data19 import data19
from .data20 import data20
from .data21 import data21
from .data22 import data22
from .data23 import data23
from .data24 import data24
from .data25 import data25
from .datas import datas

from .datadump import data100


data = {
    # --------------------- Medium puzzle (can solve but take a long time)
    1: data1,   #       OK
    2: data2,   #       OK
    3: data3,   # OK    OK
    4: data4,   #       OK
    5: data5,   #       OK
    6: data6,   # OK    OK
    7: data7,   #       OK
    8: data8,   #       OK
    9: data9,   #       OK
    # --------------------- Real puzzle from https://www.puzzle-pipes.com/
    10: data10, #       OK
    11: data11, #       OK
    12: data12, # OK    OK
    13: data13, #       OK
    14: data14,
    15: data15,
    16: data16,
    17: data17,
    18: data18,
    19: data19,
    20: data20,
    # ---------------------- Simple puzzle (a few step)
    21: data21,     # OK
    22: data22,     # OK    OK
    23: data23,     # OK
    24: data24,     # OK
    25: data25,     # OK
    100 : datas,
    # ---------------------- Sample puzzle
    1000: data100
}