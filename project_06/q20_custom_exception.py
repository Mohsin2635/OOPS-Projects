class InvalidAgeError(Exception):  #yaha hui inheritence
    pass
def check_age(age):
    if age < 18:
        raise InvalidAgeError
    else:
        print("You varified!✅")
try:
    check_age(22)
except InvalidAgeError:
    print("You are not varified!❌")