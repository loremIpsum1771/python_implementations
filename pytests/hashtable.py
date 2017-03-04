import os


def calc_total(a,b):
    return a+b

def calc_multiply(a,b):
    return a*b


class Hashtable(object):
   COUNT = 0 
   MINSIZE = 8
   def __init__(self, **initial_values):
       # self._buckets = [None] * self.MINSIZE
       self._buckets = [[None] for i in range(self.MINSIZE)]

       for k, v in initial_values.iteritems():
           self.insert(k,v)
    
   def get(self,key):
       h = hash(key)
       idx = h & self.mask

       bucket = self._buckets[idx]

       # search for the key in the chain
       if bucket and bucket[0][0] != key:
           for i in range(len(bucket)):
           		if bucket[i][0] == key:
           			return bucket[i][1]
       return self._buckets[idx][1] if self._buckets[idx][0] else None

   def insert(self, key, value):
       # If the buckets seem over-utilized, grow and re-index
       # if self.utilization >= 0.75:
       #     self._resize(len(self._buckets) * 4)
       if(self.get(key) == None):
           COUNT += 1
           self._buckets[idx] = (key,value)	
       if( COUNT/len(self._buckets) >= 0.75 ):
           self._resize(len(self._buckets) * 4)
       h = hash(key)
       idx = h & self.mask
       self._buckets[idx].append((key,value))

   def delete(self, key):
       '''Simple delete method to delete buckets by key '''

       h = hash(key)
       idx = h & self.mask

       bucket = self._buckets[idx]
       if bucket and bucket[0][0] != key:
           for i in range(len(bucket)):
           		if bucket[i][0] == key:
           			bucket[i] = None

       #self._buckets[idx] = self.TOMBSTONE

       # If the buckets seem under-utilized, shrink and re-index
       # if 0 < self.utilization <= 0.16 and len(self._buckets) > self.MINSIZE:
       #     self._resize(len(self._buckets) / 4)


   def _locate(self, key, h):
       idx = h & self.mask
       bucket = self.mask

       self._buckets[idx].append()


       # perturb = h 
       # while True:
       #     idx = ((idx >> 2) + idx + perturb + 1)& self.mask
       #     bucket = self._buckets[idx]

       #     if not bucket or bucket[1] == key:
       #         return idx

       #     perturb >>= 5
    

   def _resize(self, size):
       old_buckets = self._buckets
       self._buckets = [[None] for i in range(size)]

       #Make sure the old data gets re-indexed into the new store
       #for bucket in [b for b in old_buckets if b]:
       for i in range(len(old_buckets)):
       		for j in range(len(old_buckets[i])):
       			bucket = old_buckets[i][j]
           		self.insert(bucket[0], bucket[1])

   @property
   def mask(self):
       return len(self._buckets) - 1

   @property
   def utilization(self):
       '''Calculate the number of buckets that are actually populated '''
       try:
           return float(len(self))/float(len(self._buckets))
       except ZeroDivisionError:
           return 0
   def __len__(self):
       '''Len should return the number of non-tombstoned and populated records'''
       chainSum = 0
       for i in self._buckets:
       		chainSum += len(i)
       return chainSum

   def __setitem__(self, key, val):
       self.insert(key, val)

   def __getitem__(self, key):
       val = self.get(key)
       if val:
           return val
       else:
           raise KeyError

   def __delitem__(self, key):
       self.delete(key)


