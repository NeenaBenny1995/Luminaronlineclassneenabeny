def vccine_apply(func):
    def wrapper(**kwargs):
        if kwargs["age"]<65 or kwargs["healthissue"]==False:

            print("not allowed")
        else:
            return func(**kwargs)
    return wrapper
@vccine_apply
def vaccination(**kwargs):
    print("allow location in ekm")
vaccination(name="anju",age=66,address="address",healthissue=True)