#!/usr/bin/python3
if _name_ == "_main_":
    from calculator_1 import add, sub, mu1, div
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}" .format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}" .format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}" .format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}" .format(a, b, div(a, b)))
    
    
