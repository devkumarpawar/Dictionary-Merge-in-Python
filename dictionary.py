##FIRST METHOD##

# merge two dictionaries in python

def Merge(dict1,dict2):
    return(dict2.update(dict1))

# Driver code

dict1 = {'a':10,'b':20,'c':30}
dict2 = {'d':40,'e':50,'f':60}

# This return None
print(Merge(dict1,dict2))
#changes made in dict2
print(dict2)

##SECOND METHOD##

# merge two dictionaries in python

def Merge(dict1,dict2):

    result = {**dict1,**dict2}
    return result

# Driver Code

dict1 = {'a':10,'b':20,'c':30}
dict2 = {'d':40,'e':50,'f':60}
dict3 = Merge(dict1,dict2)
print(dict3)
