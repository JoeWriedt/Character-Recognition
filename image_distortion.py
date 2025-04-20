
def line_strip(line: int, data: list) -> list:
     new_data = data[:]
     length = len(data)
     for i in range(length):
          for j in range(int(len(data[0])**0.5)):
               new_data[i][int(len(data[0])**0.5)*(line-1)+j] = 1 # random, 0 or 1

     return new_data

#Spalten verändern
def collumn_strip(collumn: int, data: list) -> list:
     new_data = data[:]
     length = len(data)
     for i in range(length):
          for j in range(int(len(data[0])**0.5)):
               new_data[i][j*(int(len(data[0])**0.5))+collumn-1] = 1 # random, 0 or 1
     
     return new_data

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
     

def inverting(data: list) -> list:
     new_data = data[:]
     length = len(data)
     for i in range(length):
          for j in range(len(data[0])):
               new_data[i][j] = 1-data[i][j]

     return new_data

