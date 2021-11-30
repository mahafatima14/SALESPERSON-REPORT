"""Generate sales report showing total melons each salesperson sold."""


salespeople = []                        #initialize an empty list called salespeople
melons_sold = []                        #initialize an empty list called melon_sold

f = open('sales-report.txt')            #open the file sales-report.txt for python to read
for line in f:                          #iterate over each line in the file
    line = line.rstrip()                #get rid of the trailing white space 
    entries = line.split('|')           #split the data by '|' and place it in a list called entries
    #print("entries at the beginning", entries)
    salesperson = entries[0]            #assign salesperson to list at index 0
    melons = int(entries[2])            #assign melons to an integer value of list at index 2
    #print(f"entries at the end {entries}")
    
    
    if salesperson in salespeople:                  #loop through the salespeople list and find if the salesperson is in the list            
        position = salespeople.index(salesperson)   #go to that index (so we know which position the person is at)
        #print(f"position is :{position}, salespeople is {salespeople}")
        melons_sold[position] += melons             #add the number of melons to the exsiting melons
    else:
        salespeople.append(salesperson)             #if the salesperson is not in salespeople, append their name to the list
        melons_sold.append(melons)                  #append the melons they sold 


for i in range(len(salespeople)):                               # for the lenght of the list salespeople, print out the salesperson and the melons they sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
