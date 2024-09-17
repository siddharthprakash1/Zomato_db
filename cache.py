class SimpleCache:
    def __init__(self):
        self.cahce={}
        self.timeout= {} #store expiration times 
def get(self,key):
    """this is for retrieving"""
    if key in self.cache:
        if self._is_expired(key):
            self.delete(key)
            return None
        return self.cache[key]
    return None

def set(self,key,value,timeout):
    self.cache[key]=value
    self.timeout[key]=self._current_time()+timeout
    

def delete(self,key):
    if key in self.cache:
        del self.cache[key]
        del self.timeout[key]

def _is_expired(self,key):
    return self._current_time()>self.timeout.get(key,0)

def _current_time(self):
    import time
    return int(time.time())


    