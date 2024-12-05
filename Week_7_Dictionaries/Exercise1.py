"""Print Ulster Uni from below dictionary"""

Dom={True:[1234,1121], False:{'s':[12,22,12,9]}, 'colleges':['BelfastMet','QUB','Ulster Uni'], 0.245:'This is a float'}

print(Dom['colleges'])

print(Dom['colleges'][2])

"""print 22 from above dictionary"""

print(Dom[False]['s'][1])

"""Print all keys and values"""

print(Dom.keys())
print(Dom.values())