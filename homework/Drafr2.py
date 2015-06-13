'''
d = dict(p1=1, p2=2)
def f2(p1,p2):
    print p1, p2
f2(**d)
'''
given_parameter = {'b': 'given value'}
def parameters(given_parameter):
    list_of_all_parameters = ['a', 'b', 'c', 'd', 'e']
    list_of_values = []
    for key in list_of_all_parameters:
        list_of_values.append(given_parameter.get(key, "default value"))
    return(list_of_values)
