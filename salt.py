#!/usr/bin/env python
# coding: utf-8

#--------------- saltmine START -------------------------#

def saltmine(word=None):
    
    import random
    from ran import ran6
        
    salt = False
    
    if (word):
        spliter = (lambda x, d: [x[i:i+d] for i in range(0, len(x), d)])
		
        hword = word.encode('hex')
    
        hls = spliter(hword, ran6())
    
        puncs = ['!', '@', '$', '%', '&', '*', '-', '_', '=', '~', '?', '.']
        
        random.shuffle(puncs)        
        
        zx = [h+random.choice(puncs) for h in hls]
        
        salt = "".join(zx)
    
    return (str(salt))
    
#-------------- saltmine END ----------------------------#

#-------------- saltrefine START ------------------------#

def saltrefine(salt=None):
    
    import string
    
    value = False    
    
    if (salt):
        hexval = salt.translate(None, string.punctuation)
        
        value = hexval.decode('hex')
        
    return (str(value))

#-------------- saltrefine END --------------------------#




