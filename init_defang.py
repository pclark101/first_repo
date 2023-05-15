#Imports Regular expression lib used for pattern matching 
import re

#Funtion defangs IPs using built-in python lib called replace

def defang (ip_address):

    return ip_address.replace( '.','[.]')

#Created inital input file and output file for defanged IPs 

ip_defang = open('new_ips.txt', 'r')
ip_defanged = open('defanged_ips.txt', 'w')

# Loops through text file using built-in python lib called findall 

for line in ip_defang:
    ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)

# Takes defanged IPs from findall and creates a line variable 

    for ip_address in ip_addresses: 
        defanged_ip = defang(ip_address)    
        line = line.replace(ip_address, defanged_ip)
        # Writes defanged IPs to a new file 
        ip_defanged.write(line)

#Closes all open files 

ip_defang.close()
ip_defanged.close() 
