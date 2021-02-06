x = "awesome"#1


def myfunc():
    global x
    print("Python is " + x)#awesome
    x = "fantastic" #2


myfunc()
print("Python is " + x)#fantastic