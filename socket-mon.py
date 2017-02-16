import psutil

net_cons = psutil.net_connections(kind="tcp")

# Empty list to store TCP processes
connections_list = []

for i in net_cons:

    # Check if laddr and raddr fields exist
    if i.raddr and i.laddr:
    
        # Add the process into a list in the expected format.
        connections_list.append((i.pid, str(i.laddr[0]) + "@" + str(i.laddr[1]), str(i.raddr[0]) + "@" + str(i.raddr[1]),i.status))

# Print the headers
print "\"pid\",\"laddr\",\"raddr\",\"status\""

sorted_connections_list = sorted(connections_list,key= lambda x: x[0])

# Iterate over the list of processes
for cons in sorted_connections_list:

    # Print the values in expected format.
    print "\"" + "\",\"".join(str(s) for s in cons) + "\""
