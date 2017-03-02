import os


class Hashtable(object):
    '''Hashtable implemention similar to the one used by CPython. Uses separate chaining as the collision strategy.
       Resizes once avg chain length exceeds 5. Implements basic use cases for a hashtable. Utilizes built in python hash function and 
       takes last bits of hash to index into hashtable array.
    '''
    NUM_CHAINS = 0 
    CHAIN_ELEMENTS = 0
    LOAD_FACTOR = 5
   
    def __init__(self, minsize,**initial_values):
        '''Constructor: initializes the contents of the hashtable of minsize'''
        self.MINSIZE = minsize   
        self._buckets = [[] for i in range(self.MINSIZE)]

        for k, v in initial_values.iteritems():
            self.insert(k,v)

    def get(self,key):
        '''return actual bucket value in hashtable'''
        return self.find(key)[0] 

    def find(self,key):
        '''locate a hash table item based on a passed in key'''
        h = hash(key) 
        idx = h & self.mask #bit mask initialized to the size of table. AND of mask and h taken to determine the index
        bucket = self._buckets[idx]

        # search for the key in the chain
        if bucket:
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    return (bucket[i][1],idx,i) #if found, return bucket item and position
        return None


    def insert(self, key, value):
        '''insert a key/value pair (tuple) into hashtable. Resolves collisions using separate chaining'''
        h = hash(key)
        idx = h & self.mask
        if(len(self._buckets[idx]) == 0 ):
            self.NUM_CHAINS += 1
     
        self.CHAIN_ELEMENTS +=1
        checkKey = self.find(key)
        if(checkKey==None):
            self._buckets[idx].append((key,value))
        else:
            self._buckets[checkKey[1]][checkKey[2]] = (key,value) #overwrite value in hashtable if key/value pair already exists
        if( self.CHAIN_ELEMENTS/self.NUM_CHAINS >= self.LOAD_FACTOR ):#resize hashtable
            self._resize(len(self._buckets) * 4)

    def delete(self, key):
        '''Delete method to delete buckets by key '''
        h = hash(key)
        idx = h & self.mask
        bucket = self._buckets[idx]
        for i in range(len(bucket)):
            if bucket:
                if bucket[i][0] == key:
                    del bucket[i]
                    self.CHAIN_ELEMENTS -=1
                    if len(bucket) <1:
                        self.NUM_CHAINS -=1
                    break
        
    def _resize(self, size):
        '''Resizes and rehashes old key value pairs when load factor exceeds set value'''
        old_buckets = self._buckets
        self._buckets = [[] for i in range(size)]
        self.NUM_CHAINS = 0
        self.CHAIN_ELEMENTS = 0
        
        #Rehash old tuples into buckets in new hashtable
        for i in range(len(old_buckets)):
            for j in range(len(old_buckets[i])):
                bucket = old_buckets[i][j]
                self.insert(bucket[0], bucket[1])
        

    @property
    def mask(self):
        return len(self._buckets) - 1

    def __setitem__(self, key, val):
        self.insert(key, val)

    def __finditem__(self, key):
        val = self.get(key)
        if val:
            return val
        else:
            raise KeyError

    def __delitem__(self, key):
        self.delete(key)

