!/bin/bash

while read -r i; do
    echo
    echo "Processing: $i"

    # Run SysInfo once and store output
    sysinfo=$(SysInfo "$i")

    # Extract fields from stored output
    hostname=$(echo "$sysinfo" | grep -i hostname | awk -F':' '{print $2}')
    manager=$(echo "$sysinfo" | grep -i manager | awk -F':' '{print $2}')
    hp_agent_status=$(echo "$sysinfo" | grep -i HP_agent_status | awk -F':' '{print $2}')

    echo "Server Info: $i"
    echo "hostname: $hostname - manager: $manager - Agent_status: $hp_agent_status"
    echo "##############################################################################"
done < raghutest.txt