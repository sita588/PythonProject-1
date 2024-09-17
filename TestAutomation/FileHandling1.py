
obj=open("E:\\TestDemo.txt",'r')
#Reading all characters from the file and display one by one

# for i in obj.read():
#     print(i)

#Reading all characters from the file and display line by line
s=obj.readline()
while(s):
    print(s)
    s=obj.readline()