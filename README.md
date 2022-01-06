# Unix Firewall Manager
![](https://github.com/ER-hamed/iptable-manager/raw/main/Screenshot.png)
## Opening Port:

```
Command: open 80
```


## Closing Port:
```
Command: close 80
```


## Remove Rule:
```
Command: remove 80
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
Command: unset
```

##### Open 22, 80, 443 And Open All Other Traffic.
#
 
### Use args:
```
# ./UFM.py open 21
```
```
# ./UFM.py close 21
```
```
# ./UFM.py remove 21
```
```
# ./UFM.py flush
```
