#!/usr/bin/env python
# coding: utf-8


#-------------- generating random values START --------------#

def random_value(count=2):
    import random
    import string
    
    try:
        cn = int(count)
    except:
        cn = 2
    
    chars = string.letters + string.digits + "_"
    value = ''.join([random.choice(chars) for x in range(int(cn))])
    return (str(value))
    
#-------------- generating random values END ---------------#


#-------------- generating random values START --------------#

def random_number(count=2):
    import random
    import string
    
    try:
        cn = int(count)
    except:
        cn = 2
    
    chars = string.digits
    value = ''.join([random.choice(chars) for x in range(int(cn))])
    return (int(value))
    
#-------------- generating random values END ---------------#


#-------------- generating random values upto 6 START --------------#

def ran6():
    import random
    import string
    cn = 1
    chars = '23456'
    value = ''.join([random.choice(chars) for x in range(int(cn))])
    return (int(value))
    
#-------------- generating random values upto 6 END ---------------#


#----------- generating random dictionary words START -------#

def random_word():
    import random
    
    words = "red\ngreen\nblue\norange\nwhite\nchef\npink\nchip\ngrey\naqua\nbuzz\ncoral\ngold\nmark\nbit\nnet\nindigo\nivory\nlime\nbook\nkite\npico\nsite\nwall\ndesk\nplum\ncup\nshell\npoint\nsmith\nrice\nsnow\nnavy\nriver\nolive\napple\nfont\ncake\nmake\ncar\npaper\nuber\nlake\nrock\nwing\ncoffee\nstar\nmac\neros\nalpine\nmelon\ntofu\nrio\nberry\ncore\npen\nrobin\nlemon\ncoin\ncafe\nacer\ninter\nhub\nnote\nstock\nlock\nmint\nclover\nfish\nclick\ndrop\nbox\ncity\nblend\nmount\natlas\nruby\nswift\nship\ntitan\nprime\ncamp\nexcel\ncloud\nsquare\nspin\nwest\nkiwi\nplot\ntech\neuro\nfort\nsugar\nsouth\ncard\nboard\noffice\nfuse\ninfo\nzen"
    
    return (random.choice(words.split('\n')))
        
#----------- generating random dictionary words END ----------#

