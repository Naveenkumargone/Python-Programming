l = []
for i in range(2): 
      user = int(input("Enter any number and hit: "))
      l.append(user)
      
list = l[0] * l[1]
      
if list > 500:
      print(l[0] + l[1])
else:
      print("Hello LNB code is running fine !!")