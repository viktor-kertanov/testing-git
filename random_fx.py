import random

def random_generator(upper_bound):
    return random.randint(1, upper_bound)
    

if __name__ == '__main__':
    print(f'Our random number is: {random_generator(10000)}.')