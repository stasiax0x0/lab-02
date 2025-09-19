with open('sample.txt','r') as input,open('copy.txt','w') as output:
    for line in input:
        output.write(line)