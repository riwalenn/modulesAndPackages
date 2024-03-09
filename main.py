# from shopping.more_shopping.shopping_cart import buy # be more explicit when you import packages, prefer this one
from shopping.more_shopping import shopping_cart
from utility import multiply, divide
from random import choice, shuffle

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(choice(my_list))
shuffle(my_list)
print(my_list)
# print(buy('apple'))
print(shopping_cart.buy('apple'))
print(divide(10, 5))
print(multiply(10, 5))
if __name__ == '__main__':
    print('please run this')
