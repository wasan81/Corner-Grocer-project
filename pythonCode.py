######################################################################
#   Wasan Alabed
#   CS210: corner grocer project 
#   August 19,2022
#   This  python code read a list of all items from (item text file) purchased in a given day along with the number of times each item was purchased.
#
#   Rearranging their produce section to know how often items are purchased.
#
#   Save the result in frequencey dot file. 
##########################################################################

FILENAME = open("item.txt")

def readFile(filename):
    
   # Get the list of lines read in from the file in raw form.
   
    lines = None
    
    with open("item.txt", "r") as file:
        lines = file.readlines()
     
    return lines   #return - the list of lines


def getInventory():
    '''
    Get the inventory read in from the file.
    @return - dictionary of inventory in the form {item : frequency}
    '''
   # Dictionary of {item : frequency} 
    inventory = {}
    #read item from the item.txt file
    items =readFile(FILENAME)
   # Loop through the list of items
    
    for item in items:
        
        # Remove the newline character at end of line. 
        item = item.strip()
   # Update existing frequency; otherwise add item to dictionary
        if item in inventory:
            inventory[item] +=1 # accumulate to the dictionary item
        else:
            inventory[item] =1
            
    return inventory

    
def determineInventory():
    # Get the inventory
   inventory = getInventory()
   
    # loop through the dictionary's keys and values
   
   for item, frequency in inventory.items():
       print(item,":", frequency) # print the output

def determineFrequency(item):
    # Get the inventory
    inventory = getInventory()
   
    # Access the item from the inventory
    
    return inventory[item] # return single item

def output():
    #get the inventory
    inventory = getInventory()
   
    # Loop through the dictionary and write to the loop through the dictionary's keys and valuest file
   

    myFile = open("frequency.dat", "w")
   
    for item, frequency in inventory.items():
    	myFile.write(item+" "+str(frequency)+"\n")
    
    
    
