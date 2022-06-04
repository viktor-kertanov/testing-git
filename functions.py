def multiply(a,b):
    return a*b

def power(a,power):
    return a**power

def reverse_eng(string):
    return string[::-1]

if __name__ == '__main__':
    my_str = 'Витя, привет дорогой!'
    rev_str = reverse_eng(my_str)
    
    print(rev_str)