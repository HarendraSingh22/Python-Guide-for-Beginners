#python version 2.7
#open the file in writing mode. If it doesn't exist, it will be created
# if no path is specified, it will save to the root folder of the script.

file=open("Helloworld.txt", "w")

#now that the file is open, let's write something to it

file.write("Hello world!")

#make sure to close the file when you're finished. This is how to save it in python
file.close()
