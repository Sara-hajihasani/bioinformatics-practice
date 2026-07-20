#working with files
with open('hello.txt') as file:
   for index,line in enumerate(file,start=1):
        if index % 2 == 0:
            print(line.strip())
