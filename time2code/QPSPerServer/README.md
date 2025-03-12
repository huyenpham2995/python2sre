### Question

You are given a query log for a service run by several servers. below is the log content:
```
Time Date Server_ID Query_ID 
5:05:03 09/09/2020 server1 123213213
5:05:03 09/09/2020 server2 123213214
5:05:03 09/09/2020 server3 123213215
5:05:03 09/09/2020 server2 123213216
5:05:03 09/09/2020 server3 123213217
5:05:03 09/09/2020 server1 123213218
5:05:04 09/09/2020 server1 123213219
5:05:04 09/09/2020 server2 123213220
5:05:04 09/09/2020 server3 123213221
5:05:04 09/09/2020 server2 123213222
5:05:04 09/09/2020 server1 123213223
5:05:04 09/09/2020 server3 123213224
5:05:04 09/09/2020 server3 123213225
5:05:04 09/09/2020 server2 123213226
5:05:04 09/09/2020 server2 123213227
5:05:04 09/09/2020 server3 123213228
5:05:05 09/09/2020 server2 123213229
5:05:05 09/09/2020 server3 123213230
5:05:05 09/09/2020 server1 123213231
5:05:05 09/09/2020 server2 123213232
5:05:05 09/09/2020 server1 123213233
```

Assume you only need to calculate the QPS per server for the three seconds given. Output should be like:
```
Server_ID QPS
server1 x.x
server2 x.x
server3 x.x
```

### Thoughts

### Pseudocode

### BigO
