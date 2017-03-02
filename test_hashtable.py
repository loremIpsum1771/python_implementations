import hashtable

def test_resize():
    h = hashtable.Hashtable(one="one", two="two", three="three", four="four", five="five", six="six", seven="seven", eight="eight", nine="nine")
    h.MINSIZE = 3
    h['ten'] = 10
    #After resize, the number of (active) chains in the table should be 4 and total chain elements should be 10
    assert h.CHAIN_ELEMENTS == 10 and h.NUM_CHAINS == 4
