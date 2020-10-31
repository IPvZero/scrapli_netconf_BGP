---
title: "Deploying iBGP over OSPF via NETCONF"
date: "29th Oct 2020"
tags: ["nornir", "scrapli", "netconf"]
---

### Dependencies

```
python3 -m pip install scrapli-netconf
python3 -m pip install nornir
python3 -m pip install nornir-scrapli
python3 -m pip install nornir-utils
python3 -m pip install nornir-jinja2
```
### Tutorial Workflow & Overview

Build the topology using three CSR1000v routers and one out-of-band switch. Copy the start-up configurations into each device. Then simply deploy the script by typing ```python3 run1.py```

You should now have an iBGP over OSPF network, with CSR2 acting as a Route Reflector, and CSR3 advertising 2 prefixes into BGP! 

### Connectivity 
The MGMT IP address range I use in my lab is ```192.168.31.0/24```. This is the IP address range used on the GigabitEthernet1 interface of each router, and the IP range used in my Nornir hosts.yaml inventory file. Change these addresses to suit your own lab requirements.

### Device Version (Running vs Candidate)
This lab was tested using the following CSR1000v image taken from my Personal CML-P account:

```Cisco IOS XE Software, Version 16.11.01b```

```Cisco IOS Software [Gibraltar], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.11.1b, RELEASE SOFTWARE (fc2)```


Be aware that newer versions of the CSR1000v support the option for a Candidate configuration. When “candidate” data store is enabled, the Running data store isn't writable through NETCONF sessions. Instead all configurations get committed only through Candidate. In this case, users should modify the target data store in the ```run1.py``` script from ```target="running"``` to ```target="candidate"``` - and then commit the configuration to transfer it into the live running configuration.




### TOPOLOGY

![alt text](https://github.com/IPvZero/scrapli_netconf_BGP/blob/main/images/ibgp.png?raw=true)

### About Me
My name's John McGovern, I maintain a Youtube channel called IPvZero and I am trainer for CBT Nuggets. 
I create instructional videos on Python Network Automation.

### Contact

[Twitter](https://twitter.com/IPvZero)

[Youtube](https://youtube.com/c/IPvZero)

[LinkedIn](https://www.linkedin.com/in/ipvzero)

### CBT Nuggets 

[Advanced Network Automation with Cisco and Python](http://learn.gg/adv-net)

