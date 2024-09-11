def print_params(a = 1, b = 'String', c = True):
    print(a, b, c)

values_list = [1, 'a', True]
values_dict = {'a':5, 'b':42 ,'c':56}
print_params(*values_list)
print_params(**values_dict)
print_params(1, 'String', True)
print_params(b=25)
print_params(c=[1,2,3])
values_list2 = [54.32, 'a']
print_params(*values_list2, 42)