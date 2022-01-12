
# r for reading
# w for writing or creating a file
# a for appending to file

# open reads file as string
fl = open("C:\\Users\\vishw\\OneDrive\\Documents\\pythonlearn\\cde.csv","r")

content = fl.read()

# print(type(content))
print(content)

# for ln in content:
#     print(ln)

with open("C:\\Users\\vishw\\PycharmProjects\\python-data-engineering-interviews\\data\\data.csv","w") as f:
    f.write(("write from within code"))

with open("C:\\Users\\vishw\\PycharmProjects\\python-data-engineering-interviews\\data\\data.csv","a") as f:
    f.write(("append within code"))

# readlines

with open("C:\\Users\\vishw\\OneDrive\\Documents\\pythonlearn\\cde.csv","r") as a:
    lines = a.readlines()
    print(lines)



fl.close()
