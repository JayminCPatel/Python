#Author :- Jaymin Patel
#Practice :- WAP to take two lists of numbers from the user and create a new list such that it contains odd numers from the first list and even numbers from the second list

mainlist = []
oddlist = []
evenlist = []
num=int(input("enter how many number you want to insert\n"))
list=[]
for i in range(0,num):
  x = int(input("enter no\n"))
  mainlist.append(x)
print(list)
print ("----Split list into Odd and Even----")
for i in range(0,len(mainlist)) :
  print("List element : ", mainlist[i])
  if (mainlist[i]%2 == 0):
    evenlist.append(mainlist[i])
  else :
    oddlist.append(mainlist[i])

print("---Odd List---")
for i in range(len(oddlist)):
  print("Odd item : ",oddlist[i])

print("---Even List---")
for i in range(len(evenlist)):
  print("Even item : ",evenlist[i])


