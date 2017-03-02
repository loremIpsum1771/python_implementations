import hashtable

def test_init():
	'''test initialization of hashtable'''
	h = hashtable.Hashtable(one="one", two="two", three="three", four="four", five="five", six="six", seven="seven", eight="eight", nine="nine")
	assert len(h._buckets)  ==  32 # 32 - buckets have grown to accomodate items



def test_find():
	'''test location of keys'''
	h = hashtable.Hashtable(one="one", two="two", three="three", four="four", five="five", six="six", seven="seven", eight="eight", nine="nine")
	assert h.get('four') == 'four'

def test_delete():
	''' test deletion of keys'''
	# Remove a bunch of the keys
	h = hashtable.Hashtable(one="one", two="two", three="three", four="four", five="five", six="six", seven="seven", eight="eight", nine="nine")
	del h['one']
	del h['two']
	del h['three']
	del h['four']
	del h['five']
	del h['six']
	del h['seven']
	del h['eight']

	assert len(h._buckets) == 8 # 8 - buckets has now shrunk due to utilization

def test_insert_after_del():
	'''test insertion of keys after deletion'''
	# Remove a bunch of the keys
	h = hashtable.Hashtable(one="one", two="two", three="three", four="four", five="five", six="six", seven="seven", eight="eight", nine="nine")
	del h['one']
	del h['two']
	del h['three']
	del h['four']
	del h['five']
	del h['six']
	del h['seven']
	del h['eight']

	#print(len(h._buckets))  # 8 - buckets has now shrunk due to utilization
	h['ten'] = 10
	assert h.get('ten') == 10  # 10
    
    
   
def test_resize():
    h = hashtable.Hashtable(one="one", two="two", three="three", four="four", five="five", six="six", seven="seven", eight="eight", nine="nine")
    h.MINSIZE = 3
    h['ten'] = 10
    #After resize, the number of (active) chains in the table should be 4 and total chain elements should be 10
    assert h.CHAIN_ELEMENTS == 10 and h.NUM_CHAINS == 4
