import os
from enum import Enum

def calc_total(a,b):
    return a+b

def calc_multiply(a,b):
    return a*b




##Generate a hash given the word 'foo'
#key = 'foo'
#value = 'hello world'
#hash(key) 

##convert to binary, slice last 3 bits 
#bits = bin(hash(key))[-3]

#idx = int(bits,2)

##Create 3 bits worth of buckets
#buckets = [None] * 8
#buckets[idx] = 'hello world'

##load back data
#buckets[int(bin(hash('foo'))[-3],2)]



#class Hashtable(object):
#    TOMBSTONE = '<Tombstone>'
#    MINSIZE = 8
#    def __init__(self, **initial_values):
#        self._buckets = [None] * self.MINSIZE

#        for k, v in initial_values.iteritems():
#            self.insert(k,v)
    
#    def get(self,key):
#        h = hash(key)
#        idx = h & self.mask

#        bucket = self._bukcets[idx]

#        # start naive probe, if the bucket is existant but not correct key
#        if bucket and bucket[1] != key:
#            idx = self._locate(key, h)
#        return self._buckets[idx][2] if self._bukcets[idx] else None

#    def insert(self, key, value):
#        # If the buckets seem over-utilized, grow and re-index
#        if self.utilization >= 0.75:
#            self._resize(len(self._buckets) * 4)

#        h = hash(key)
#        idx = h & self.mask

#        #If the initial probe returned a bucket (is occupied), probe randomly for the next slot

#        if self._buckets[idx]:
#            idx = self._locate(key, h)
        
#        self._buckets[idx] = (h, key, value)

#    def delete(self, key):
#        '''Simple delete method to delete buckets by key '''

#        h = hash(key)
#        idx = h & self.mask

#        bucket = self._buckets[idx]
#        if bucket and bucket[1] != key:
#            idx = self._locate(key, h)

#        self._buckets[idx] = self.TOMBSTONE

#        # If the buckets seem under-utilized, shrink and re-index
#        if 0 < self.utilization <= 0.16 and len(self._buckets) > self.MINSIZE:
#            self._resize(len(self._buckets) / 4)


#    def _locate(self, key, h):
#        idx = h & self.mask
#        bucket = self.mask

#        perturb = h 
#        while True:
#            idx = ((idx >> 2) + idx + perturb + 1)& self.mask
#            bucket = self._buckets[idx]

#            if not bucket or bucket[1] == key:
#                return idx

#            perturb >>= 5
    

#    def _resize(self, size):
#        old_buckets = self._buckets
#        self._buckets = [None] * size

#        #Make sure the old data gets re-indexed into the new store
#        for bucket in [b for b in old_buckets if b]:
#            self.inesrt(bucket[1], bucket[2])

#    @property
#    def mask(self):
#        return len(self._buckets) - 1

#    @property
#    def utilitzation(self):
#        '''Calculate the number of buckets that are actually populated '''
#        try:
#            return float(len(self))/float(len(self._buckets))
#        except ZeroDivisionError:
#            return 0
#    def __len__(self):
#        '''Len should return the number of non-tombstoned and populated records'''
#        return len([b for b in self._buckets if b and b != self.TOMBSTONE])

#    def __setitem__(self, key, val):
#        self.insert(key, val)

#    def __getitem__(self, key):
#        val = self.get(key)
#        if val:
#            return val
#        else:
#            raise KeyError

#    def __delitem__(self, key):
#        self.delete(key)

#h = HashTable(one="one", two="two", three="three", four="four", five="five",
#              six="six", seven="seven", eight="eight", nine="nine")

#print(len(h._buckets))  # 32 - buckets have grown to accomodate items

## Remove a bunch of the keys
#del h['one']
#del h['two']
#del h['three']
#del h['four']
#del h['five']
#del h['six']
#del h['seven']
#del h['eight']

#print(len(h._buckets))  # 8 - buckets has now shrunk due to utilization
#h['ten'] = 10
#print(h.get('one'))  # None -
#print(h.get('ten'))  # 10




#EntryType = Enum('EntryType' ,'ACTIVE EMPTY DELETED')
#class Hashtable2:
    
#    def __init__(self, capacity = 101):
#        self.array = []
#        self.currentSize = 0
#        self.capacity = capacity
#        for i in range(0,size):
#            array.append(hashEntry)

    
    
    

#    def find(self, obj):
#        i = hash(obj) % len(array)
#        while True:
#            if array[i].info == 
#    def insert(self, obj):

#    def delete(self, obj):
