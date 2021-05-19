##to add extra feature to a function without rewrite on functions
def shuffle_values(func):
    def wrapper(nu1,nu2):
        if nu1<nu2:
            (nu1,nu2)=(nu2,nu1)
        return func(nu1,nu2)
    return wrapper
@shuffle_values
def sub(num1,num2):
    return num1-num2
print(sub(2,5))