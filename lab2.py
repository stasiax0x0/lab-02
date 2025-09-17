# Step 1: Print the file lines


# Step 2: Extract IP addresses
import re

pattern = r"\d+\.\d+\.\d+\.\d+"
text = 'auth.log'
print(re.findall(pattern,text))
ips = []     # creates an empty list called ips
for ip in found_ips:
        ips.append(ip) # Add each ip to our list