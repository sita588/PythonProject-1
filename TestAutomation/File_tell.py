# tell is used to display current position of cursor
obj=open("E:\\TestDemo.txt",'r')
print(obj.tell())

# obj.readline()
# print(obj.tell())
#
# obj.readline()
# print(obj.tell())

obj.seek(5)
print(obj.tell())
