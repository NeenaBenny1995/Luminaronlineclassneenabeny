def account_det(func):
    def wrapper(user,pin):
        if user!="admin":
            raise Exception("error")
        else:
            return func(user,pin)
    return wrapper

def change_pin(user,pin):
    mypin=pin
    return mypin
@account_det
def delete_account(user,acno):
    return str(acno)+"deleted"
print(delete_account("admin",1000))