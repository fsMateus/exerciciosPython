
filename = "squid.txt"
file = open(filename)
''' Request Variables '''
total_requests = 0
total_cache_hits = 0
total_cache_misses = 0
total_denied = 0
''' Byte Total Variables '''
total_requested_bytes = 0
total_cache_bytes = 0
total_miss_bytes = 0
total_other_bytes = 0
host_requests = {}
host_total_bytes = {}
domain_requests = {}
denied_requests = {}
domain_bytes = {}
 
''' Strip back URL to what we will measure on '''
def striptodomain(url):
    stripped = url.replace("http://", "")
    #stripped = stripped.repace("www.")
    bits = stripped.split('/')
    hostname = bits[0]
    return hostname
 
 
''' Rip through the file and generate the stats '''
for line in file:
    bit = line.split()
    total_requests += 1
 
    ''' Add in the host request and bytes totals '''
    if bit[2] in host_requests:
        host_requests[bit[2]] += 1
        host_total_bytes[bit[2]] = int(host_total_bytes[bit[2]]) + int(bit[1])
    else:
        host_requests[bit[2]] = 1
        host_total_bytes[bit[2]] = int(bit[1])
         
                 
    ''' Add in the Domain request and bytes totals '''
    hostname = striptodomain(bit[6])
    if hostname in domain_requests:
        domain_requests[hostname] += 1
        domain_bytes[hostname] = int(domain_bytes[hostname]) + int(bit[1])
    else:
        domain_requests[hostname] = 1
        domain_bytes[hostname] = int(bit[1])
     
         
    if 'DENIED' in line or 'BLOCKED' in line:
        total_denied += 1
        denied_requests[hostname] = 1

    if 'TCP_HIT' in line or 'TCP_MEM_HIT' in line or 'TCP_NEGATIVE_HIT' in line or 'TCP_IMS_HIT' in line or 'TCP_REFRESH_HIT' in line:
        total_cache_hits += 1
        total_cache_bytes += int(bit[1])
        total_requested_bytes += int(bit[1])
         
    elif "TCP_MISS" in line or 'TCP_REFRESH_MISS' in line or 'TCP_CLIENT_REFRESH_MISS' in line:
        total_cache_misses += 1
        total_miss_bytes += int(bit[1])
        total_requested_bytes += int(bit[1])
         
    else:
        total_other_bytes += int(bit[1])
        total_requested_bytes += int(bit[1])
file.close()
 
     
''' Extra file stats '''       
total_other = (total_requests - total_cache_hits) - total_cache_misses
 
 
''' Calculate Percent values '''
total_cache_hits_pc = round((1.0 * total_cache_hits / total_requests) * 100,2)
total_cache_misses_pc = round((1.0 * total_cache_misses / total_requests) * 100,2)
total_other_pc = round((1.0 * total_other / total_requests) * 100,2)
 
total_cache_bytes_pc = round((1.0 * total_cache_bytes / total_requested_bytes) * 100,2)
total_miss_bytes_pc = round((1.0 * total_miss_bytes / total_requested_bytes) * 100,2)
total_other_bytes_pc = round((1.0 * total_other_bytes / total_requested_bytes) * 100,2)
    
 
''' File type counts'''
# print()
# print("Caching Performance")
# print("Total requests:  ", total_requests)
# print("Total Cache hits: ",total_cache_hits, total_cache_hits_pc, "%")
# print("Total Cache misses: " ,total_cache_misses, total_cache_misses_pc, "%")
# print("Total Other: " ,total_other, total_other_pc, "%")

# print("Total bytes: ", total_requested_bytes)
# print("Total Cache bytes: ",total_cache_bytes, total_cache_bytes_pc, "%")
# print("Total Miss bytes: ",total_miss_bytes, total_miss_bytes_pc, "%")
# print("Total Other bytes: ",total_other_bytes, total_other_bytes_pc, "%")
# print('\n')

 
''' Print Domain statistics '''
#sorted_domain_requests = sorted(domain_requests)
print("Most Requested Domains (hits)")
temp_list = domain_requests.keys()
temp_list.sort( key = domain_requests.__getitem__, reverse = True)
for a in range(10):
    print(domain_requests[temp_list[a]]  , ' ' , temp_list[a])
print('\n')

print("Most Requested Denied")
print("Total Requested Denied", total_denied)
temp_list = denied_requests.keys()
temp_list.sort( key = denied_requests.__getitem__, reverse = True)
for a in range(len(temp_list)):
    print(denied_requests[temp_list[a]]  , ' ' , temp_list[a])
print('\n') 
 
# print "Highest Data Transfer by Domain (bytes)"
# temp_list = domain_bytes.keys()
# temp_list.sort( key = domain_bytes.__getitem__, reverse = True)
# for a in range(25):
#     print domain_bytes[temp_list[a]]  , "\t" , temp_list[a]
# print ""
# print ""
 
# print("Most requesting hosts (hits)")
# temp_list = host_requests.keys()
# temp_list.sort( key = host_requests.__getitem__, reverse = True)
# if len(temp_list) < 10:
#     hosts = len(temp_list)
# else:
#     hosts = 10
# for a in range(hosts):
#     print(host_requests[temp_list[a]]  , " " , temp_list[a])
# print("\n\n")
 
# print "Highest Data Transfer by Host (bytes)"
# temp_list = host_total_bytes.keys()
# temp_list.sort( key = host_total_bytes.__getitem__, reverse = True)
# for a in range(hosts):
#     print host_total_bytes[temp_list[a]]  , "\t" , temp_list[a]
# print ""
# print ""