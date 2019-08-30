n = int(input("Enter number of students: "))
list1=[]
list2=[]
for x in range(n):
    list1.append(float(input("Enter student "+str(x+1)+" weight: ")))
for x in range(n):
    list2.append((list1[x]*0.454))
print("Weights of students in kgs: " +str(list2))

def string_alternative():
    str= input("Enter the string: ")
    str1 = ""
    for i in range(len(str)):
        if(i%2==0):
            str1=str1+str[i]
    print("Printing alternate characters of the string: " +str1)
string_alternative()


file_name=input("Enter the file name: ")
f=open(file_name, "r")
count = {}
k=f.readline()
while(k!=""):
    word = k.split(" ")

    for s in word:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    k=f.readline()
print(count)

file_name_dest = input("Enter the destination file name: ")
f=open(file_name_dest, "w+")
for i in count:
     f.write(i+" : "+str(count[i]))
f.close()
print(count)