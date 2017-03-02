import hashtable

def test_init():
    '''test initialization of hashtable'''
    minsize = 8
    h = hashtable.Hashtable(minsize,one="one", two="two", three="three", four="four", five="five", six="six", seven="seven", eight="eight", nine="nine")
    assert len(h._buckets)  ==  8 and  h.CHAIN_ELEMENTS == 9



def test_get():
    '''test location of keys'''
    minsize = 8
    h = hashtable.Hashtable(minsize,one="one", two="two", three="three", four="four", five="five", six="six", seven="seven", eight="eight", nine="nine")
    assert h.get('four') == 'four'

def test_delete():
    ''' test deletion of keys'''
    minsize = 8
    # Remove a bunch of the keys
    h = hashtable.Hashtable(minsize,one="one", two="two", three="three", four="four", five="five", six="six", seven="seven", eight="eight", nine="nine")
    del h['one']
    del h['two']
    del h['three']
    del h['four']
    del h['five']
    del h['six']
    del h['seven']
    del h['eight']
    assert h.CHAIN_ELEMENTS == 1 

def test_insert_after_del():
    '''test insertion of keys after deletion'''
    minsize = 8
    # Remove some of the keys
    h = hashtable.Hashtable(minsize,one="one", two="two", three="three", four="four", five="five", six="six", seven="seven", eight="eight", nine="nine")
    del h['one']
    del h['two']
    del h['three']
    del h['four']
    del h['five']
    del h['six']
    del h['seven']
    del h['eight']
    h['ten'] = 10
    assert h.get('ten') == 10  
    
    
   
def test_resize():
    '''test resizing of hashtable once load factor is reached'''
    minsize = 3
    h = hashtable.Hashtable(minsize)
    h['one'] = "one"
    h['two'] = "two"
    h['three'] = "three"
    h['four'] = "four"
    h['five'] = "five"
    h['six'] = "six"
    h['seven'] = "seven"
    h['eight'] = "eight"
    h['nine'] = "nine"
    h['ten'] = 10
    #After resize, the number of (active) chains in the table should be 4 and total chain elements should be 10
    assert h.CHAIN_ELEMENTS == 10 and h.NUM_CHAINS == 4

def test_add_duplicate():
    '''test if the hashtable handles duplicates'''
    minsize = 8
    h  = hashtable.Hashtable(minsize,one="one", two="two", three="three", four="four", five="five", six="six", seven="seven", eight="eight", nine="nine")
    h["one"] = 17
    assert h.get("one") == 17

