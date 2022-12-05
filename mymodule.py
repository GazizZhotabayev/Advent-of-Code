def wrongfunc(): 
    return "that's not what I want"

def myfunc(): 

    def returnfunc(f = wrongfunc):
        return f()
    
    return returnfunc()