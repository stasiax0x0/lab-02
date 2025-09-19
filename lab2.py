import re

with open('auth.log','r') as f:                 #opens auth.log to read
        content = f.read()                  #reads the file and sasves it as variable 'content'
        for line in f:                   #loops through each line in the file
                print(line.())             #prints each line and removes the extra new line
pattern = r"\d+\.\d+\.\d+\.\d+"
found_ips = re.findall(pattern, content)        #finds all IPs in content and saves them as found_ips

ips=[]                                   #creates an empty list
for ip in found_ips:                      #loops through each found IP
        ips.append(ip)          #adds each found IP to the list

print(ips)

#another way to do it
#ips = list(found_ips)                   #creates a list of IPS
#print(ips)


unique_ips = set(ips)           # Convert to a set to remove duplicates

print("Unique IPs:")            # Print each unique IP
for ip in unique_ips:
    print(ip)
 
with open('unique_ips.txt','w') as output:   #opens/creates a file unique_ips.txt to write
    for ip in unique_ips:                 #loops through each ip in unique_ips
        output.write(ip + '\n')            #writes each unique IP to the file and adds a new line after each IP