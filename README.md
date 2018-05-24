# sponge
An elegent  cache library for python

# How to use

### Install
```bash
pip install sponge
```

### Usage

```python
import time
from sponge import CacheManager

# config cache manager
manager = CacheManager({
    'default': 'redis',
    'redis': {
        'host': 'localhost',
        'port': 3306,
        'db': 0
    },
    'memory': {}
})

# get cache instance
cache = manager.store('redis')

# set cache
cache.put('mykey', 'myvalue', 30) # 30 seconds
cache.get('mykey')                # myvalue

# remove cache
cache.forget('mykey')

# cache fover
cache.fover('mykey', 1)

# increase
cache.increase('mykey')     # the value will be 2

# decrease
cache.decrease('mykey', 2)  # the value will be -1


# clear all
cache.flush()

```

