with open('sample.txt', 'r') as myfile:  #open and read sample.txt as myfile(variable)
    i=1                                   #initialise i
    for line in myfile:                    #for loop
        print(f"{i}:{line.strip()}")       #f=format
        i=i+1

