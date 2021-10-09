# Write a function to check if the list has duplicate elements. 

list_ = [1, 2, 3, 4, 4, 5]
list_2 = []
def dup_check(list_): 
  for i in list_: 
    if i not in list_2:
      list_2.append(i)
      print(list_2)
    else: 
      print('There are dupes!') 

dup_check(list_)

# What if we had a differnt data type? {}