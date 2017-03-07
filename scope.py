""" A Simple exercise to experiment the scope
"""

def change(a_passed):
    a_passed = "in change"


def main():

    a = "a in main"
    def suba(aa):
        aa += " then sub"
    suba(a)
    print a         # a is a string (immutable) therefore isnot modified by the fucntion even if passed by address 

    b = {"str": "b in main"}
    def subb(aa):
        aa["str"] += " then subb"
    subb(b)
    print b["str"]  # a dict is mutable and thus is modified when passed to the fuction


    def subbb():
        b["str"] += " then subbb without any parameter"
    subbb()
    print b["str"]  # b is defined at a higher level and is modified by the function



main()

# output
# a in main
# b in main then subb
# b in main then subb then subbb without any parameter
