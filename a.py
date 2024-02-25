import threading

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def a():
    print('hi')
    
setInterval(a, 10)
