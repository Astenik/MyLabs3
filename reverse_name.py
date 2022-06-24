name = input("insert the name: ")
rev_name = ' '
ind1 = len(name) - 1 
while ind1 >= 0:
      rev_name =  rev_name + name[ind1]
      ind1 -= 1


print(f'reversed string is: {rev_name}')
