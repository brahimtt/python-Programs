def items_of_list(list):
    for i in list:
        if list.index(i)!=len(list)-1:
            print(i,end=',')
        else:
            print('and '+i)
list = []
while True:
  name = input()
  if name == '':
    break
  list = list + [name]

items_of_list(list)    
