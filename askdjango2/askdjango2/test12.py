def print_param2(**kwargs):
    print kwargs
    print kwargs.keys()
    print kwargs.values()
 
    for name, value in kwargs.items():
        print "%s : %s" % (name, value)
 
print_param2(first = 'a', second = 'b', third = 'c', fourth = 'd')
 


