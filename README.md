# Iptables Manager
![](https://github.com/ER-hamed/iptable-manager/raw/main/Screenshot.png)
## Opening Port:

```
Command: open <port-number>
```


## Closing Port:
```
Command: close <port-number>
```


## Remove Rule:
```
Command: remove <port-number>
```


## Remove All Rules:
```
Command: flush
```



## Features:
### Dropping All Other Traffic:
```
Command: set
```

##### Open 22, 80, 443 And Close All Traffic.
#
 
### Accepting All Other Traffic:
```
Command: set
```

##### Open 22, 80, 443 And Open All Other Traffic.






#
 
### Use args:
### Example
```
$ UFM open 21
```
```
$ UFM close 21
```
```
$ UFM remove 21
```
```
$ UFM flush
```

##### Open 22, 80, 443 And Open All Other Traffic.
