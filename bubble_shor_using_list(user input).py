print("program in assending order by user input:")
list1=[]
num=int(input('how many number you want to enter:-'))
print("enter values do you wants:")
for k in range(num):
    list1.append(int(input("enter element:-")))
print("user entered list:",list1)

for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
print("sorted list is:",list1)
