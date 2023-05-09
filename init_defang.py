import re 

def defang (ip_address):

    return ip_address.replace( '.','[.]')

ip_defang = open('new_ips.txt', 'r')
ip_defanged = open('defanged_ips.txt', 'w')

for line in ip_defang:
    ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)

    for ip_address in ip_addresses: 
        defanged_ip = defang(ip_address)    
        line = line.replace(ip_address, defanged_ip)
        
        ip_defanged.write(line)

ip_defang.close()
ip_defanged.close() 
