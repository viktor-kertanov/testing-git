def multiply(a,b):
    return a*b

def power(a,power):
    return a**power

def reverse_eng(string):
    return string[::-1]

def unique_elements_of_list(my_list):
    my_set = set(my_list)
    return list(my_set)

def have_fun():
    my_input = input('Type your name please!\n')
    print(f'{my_input} - you, have fun!')

if __name__ == '__main__':
    my_str = 'Hello, World!'
    rev_str = reverse_eng(my_str)

    a = ['cat', 'dog', 'bog', 'sog', 'sog', 'rog', 'clog', 'dog', 'dog', 'cat']
    print(f'Our list with no dupe check: {a}.')
    print(f'No dupes: {unique_elements_of_list(a)}.')
    print('-'*100)
    print(rev_str)

    have_fun()