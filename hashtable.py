import os




class Hashtable(object):
   NUM_CHAINS = 0 
   CHAIN_ELEMENTS = 0
   MINSIZE = 3
   def __init__(self, **initial_values):
       # self._buckets = [None] * self.MINSIZE
       
       self._buckets = [[] for i in range(self.MINSIZE)]

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
       #print "self._buckets[idx][1]: " + self._buckets[idx][0][1] + " self._buckets[idx][0]: " +self._buckets[idx][0][0]
       return bucket[0][1] if bucket[0] else None

   def insert(self, key, value):
       # If the buckets seem over-utilized, grow and re-index
       # if self.utilization >= 0.75:
       #     self._resize(len(self._buckets) * 4)
       h = hash(key)
       idx = h & self.mask
       if(len(self._buckets[idx]) == 0 ):
           self.NUM_CHAINS += 1
     
       self.CHAIN_ELEMENTS +=1
           
       
       
       print "num chains: " + str(self.NUM_CHAINS) + " num chain elements: " + str(self.CHAIN_ELEMENTS)
       #print key
       self._buckets[idx].append((key,value))
       if( self.CHAIN_ELEMENTS/self.NUM_CHAINS >= 5 ):
           self._resize(len(self._buckets) * 4)

   def delete(self, key):
       '''Simple delete method to delete buckets by key '''

       h = hash(key)
       idx = h & self.mask

       bucket = self._buckets[idx]
       if bucket and bucket[0][0] != key:
           for i in range(len(bucket)):
               if bucket[i] != None:
                   if bucket[i][0] == key:
                       if len(bucket[i]) <2:
                           self.NUM_CHAINS -=1
                       bucket[i] = None
                       self.CHAIN_ELEMENTS -=1
                       

       #self._buckets[idx] = self.TOMBSTONE

       # If the buckets seem under-utilized, shrink and re-index
       # if 0 < self.utilization <= 0.16 and len(self._buckets) > self.MINSIZE:
       #     self._resize(len(self._buckets) / 4)


   def _resize(self, size):
       old_buckets = self._buckets
       self._buckets = [[] for i in range(size)]
       print "before resize: \n num chains: " + str(self.NUM_CHAINS) + " num chain elements: " + str(self.CHAIN_ELEMENTS) + " total chains possible: " + str(len(old_buckets))
       print(old_buckets)
       self.NUM_CHAINS = 0
       self.CHAIN_ELEMENTS = 0
       print "after reset: \n num chains: " + str(self.NUM_CHAINS) + " num chain elements: " + str(self.CHAIN_ELEMENTS)
       #Make sure the old data gets re-indexed into the new store
       #for bucket in [b for b in old_buckets if b]:
       for i in range(len(old_buckets)):
           for j in range(len(old_buckets[i])):
               if old_buckets[i][j] != None:
                   bucket = old_buckets[i][j]
                   self.insert(bucket[0], bucket[1])
       print "after rehash: \n num chains: " + str(self.NUM_CHAINS) + " num chain elements: " + str(self.CHAIN_ELEMENTS) + " total chains possible: " + str(len(self._buckets))
       print "after resize: \n"
       print(self._buckets)
   @property
   def mask(self):
       return len(self._buckets) - 1

   
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

h = Hashtable(one="one", two="two", three="three", four="four", five="five", six="six", seven="seven", eight="eight", nine="nine")
print "before delete: \n"
#print(h._buckets)  # 32 - buckets have grown to accomodate items

## Remove a bunch of the keys
#del h['one']
#del h['two']
#del h['three']
#del h['four']
#del h['five']
#del h['six']
#del h['seven']
#del h['eight']
#print "after delete: \n"
#print(h._buckets)

#print(len(h._buckets))  # 8 - buckets has now shrunk due to utilization
h['ten'] = 10
h['eleven'] = 11
h['twelve'] = 12
h['thirteen'] = 13
h['fourteen'] = 14
h['fifteen'] = 15
print(h.get('one'))  # None -

print(h._buckets)
print(h.get('ten'))  # 10

