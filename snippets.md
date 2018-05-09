# Snippets

## Connect

```
screen /dev/ttyUSB0 115200
```

## Get free space

```
import uos
fs_stat = uos.statvfs('/')
fs_size = fs_stat[0] * fs_stat[2]
fs_free = fs_stat[0] * fs_stat[3]
print("File System Size {:,} - Free Space {:,}".format(fs_size, fs_free))
```

## Code management

```
ampy -p /dev/ttyUSB0 <get,put,ls> [<target>]
```