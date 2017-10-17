import re
import os
import json
import webbrowser

path = 'Email/'  #Create a folder named "Email" to place Enron emails into
values = []
run = 0
tempEmail = ""
list = {}
list2 = {}
reg = re.compile(r'[a-zA-Z0-9\._-]+@+\w+\.+[\.\w]*',re.I|re.M)  #Recompile regex for efficiency

for subdir, dir, files in os.walk(path):
    for file in files:
        filePath = open(os.path.join(subdir, file), 'r')        #Open files to read them
        readFile = filePath.read()
        emailAddress = re.findall(reg, readFile)            #Regex search for From and To email addresses

        for index, email in enumerate(emailAddress):                  #Search through each regex set of emails
            if run == 0:                            #Run count check
                run = run + 1
                tempEmail = email                   #Storage for From emails
                if index == (len(emailAddress)-1):  # If End of List Reset Values
                    #print("Im Here and I just Started!")
                    run = 0
                    tempEmail = ""
                continue
            elif len(email) == 0:                 #Check for empty string
                continue
            else:
                if tempEmail == email:              #If sender and receiver are same; skip!
                    continue
                else:
                    list["source"] = tempEmail        #Add From addresses into new dictionary
                    list["target"] = email             #Add To addresses into same dictionary
                    values.append(list)
                    list = {}                       #Clean the dictionary
                if index == (len(emailAddress)-1):    #If End of List Reset Values
                    run = 0
                    tempEmail = ""
        filePath.close()


with open('data.json', 'w') as outfile:
    list2["emails"] = values                                                #Place results into another dictionary
    json.dump(list2, outfile)                                               #Dumb results into a json file

webbrowser.open('file://' + os.path.realpath('graph.html'))  #Open the graph on browser
