import random
from data_prep import test_data

# n-th line set to 0 or 1
def line_strip(line: int, data: list, value: int) -> list:
     new_data = data[:]
     length = len(data)
     for i in range(length):
          for j in range(int(len(data[0])**0.5)):
               new_data[i][int(len(data[0])**0.5)*(line-1)+j] = value

     return new_data

# n-th column set to 0 or 1
def column_strip(column: int, data: list, value: int) -> list:
     new_data = data[:]
     length = len(data)
     for i in range(length):
          for j in range(int(len(data[0])**0.5)):
               new_data[i][j*(int(len(data[0])**0.5))+column-1] = value 
     
     return new_data

# every component is increased by the shift_value until they reach 1
def light_shift(shift_value: float, data: list) -> list:
     new_data = data[:]
     length = len(data)
     for i in range(length):
          for j in range(len(data[0])):
               if new_data[i][j] + shift_value <= 1:
                    new_data[i][j] += shift_value
               else:
                    new_data[i][j] = 1

     return new_data
     
# every component is decreased by the shift_value until they reach 0
def dark_shift(shift_value: float, data: list) -> list:
     new_data = data[:]
     length = len(data)
     for i in range(length):
          for j in range(len(data[0])):
               if new_data[i][j] - shift_value >= 0:
                    new_data[i][j] -= shift_value
               else:     
                    new_data[i][j] = 0

     return new_data
     
def random_set(value: int, amount: int, data: list) -> list:
     new_data = data[:]
     length = len(data)
     for i in range(length):
          j = 0
          used = []
          while j < amount:
               index = random.randint(1,784)
               if index not in used:
                    new_data[i][index] = value
                    j += 1
                    used.append(index)

     return new_data

