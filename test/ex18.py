# def print_two(*args):
#     arg1,arg2=args
#     print("arg1:%r,arg2:%r"%(arg1,arg2))
#
# def print_two_again(arg1,arg2):
#     print("arg1:%r,arg2:%r" % (arg1, arg2))
#
# def print_one(arg1):
#     print("arg1:%r" % arg1)
#
# def print_none():
#     print("I got nothing")
#
#
# print_two("zz","zed")
# print_two_again("sam","shaw")
# print_one("lock")
# print_none()

def cheese_and_crackers(cheese_count,boxes_of_cracker):
    print("%d"%cheese_count)
    print("%d"%boxes_of_cracker)

cheese_and_crackers(20,30)

amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

cheese_and_crackers(10+20,5+6)