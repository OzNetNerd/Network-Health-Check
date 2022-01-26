# Network Health Check

[![Git](https://app.soluble.cloud/api/v1/public/badges/6cf6e9cf-e451-4fee-b86f-416f6f8bdf0b.svg?orgId=401166500955)](https://app.soluble.cloud/repos/details/github.com/oznetnerd/network-health-check?orgId=401166500955)  

Concurrently pings and traceroutes a list of hosts. Outputs are put in individual files for easy analysis.

## Example

1. Create an `ips.txt` file and add the following lines:

```
aws.com
dns.google
1.1.1.1
```

2. Run the following command:

```python3 net-hc.py ips.txt```

Each host will output a file. Below is an example of what `1.1.1.1.txt` looks like: 

```
****************************************************************************************************
Ping Results
****************************************************************************************************
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.

--- 1.1.1.1 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 10.165/11.043/12.695/1.168 ms

****************************************************************************************************
Trace Results
****************************************************************************************************
traceroute to 1.1.1.1 (1.1.1.1), 30 hops max, 60 byte packets
 1  _gateway (192.168.20.1)  1.398 ms  4.752 ms  4.696 ms
 2  1.2.3.4 (1.2.3.4)  10.265 ms  11.023 ms  11.229 ms
 3  5.6.7.8 (5.6.7.8)  12.595 ms  17.532 ms  17.479 ms
 4  10.1.31.141 (10.1.31.141)  12.415 ms  12.358 ms  17.286 ms
 5  10.1.31.142 (10.1.31.142)  17.243 ms  17.187 ms  17.138 ms
 6  10.1.31.195 (10.1.31.195)  16.721 ms  12.358 ms  17.138 ms
 7  as13335.melbourne.megaport.com (103.26.71.38)  11.290 ms  11.685 ms  12.149 ms
 8  one.one.one.one (1.1.1.1)  11.860 ms  12.673 ms  12.618 ms
```

# Contact

* Blog: [oznetnerd.com](https://oznetnerd.com)
* Email: will@oznetnerd.com