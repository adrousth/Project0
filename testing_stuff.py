
my_dict = {
    "hello": 's',
    "bye": 0
}
account_types = ("savings", "checking", "money market", "certificate of deposit")
try:
    print(float("1000a.01"))
except ValueError as e:
    print(e)

try:
    float(my_dict["hello"])
except ValueError as e:
    print(("account_type must be one of the following " + str(account_types)))



