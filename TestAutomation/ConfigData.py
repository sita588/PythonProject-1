from configparser import ConfigParser

#Created an object of config parser class
obj=ConfigParser()

#to read data from config file
obj.read("./InputFiles/config.cfg")
print(obj.get("Section1","username"))
print(obj.get("Section1","password"))