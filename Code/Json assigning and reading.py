#first import the json module
import json

#next we will now ask the user for input and assign a variable
invar = input('What to ask')

#now we will make a empty json, which is a sort of organized file
data = {}

#we will now assign the "name" section to what the user types
data['name'] = invar

#next we will print the finalized json with json.dumps which cleans it up
print(json.dumps(data, indent=4))

#finally we can read from the json
print(data['name'])
