#Consider mymodule.py to be fixed for the purpose of this question: i.e., I cannot change it in any way

from mymodule import myfunc

#Running this gives me "that's not what I want", as expected (see )
print(myfunc())

#My goal is to overwrite the default function [i.e. wrongfunc()] that is passed to returnfunc() with correctfunc() defined below
def correctfunc():
    return "that's what I'm talking about"

#Insert python magic here so that running myfunc() returns correctfunc()
#No cheating though, i.e., don't just set myfunc = correctfunc, you have to update what's passed to returnfunc() within myfunc()

print(myfunc.__dict__)