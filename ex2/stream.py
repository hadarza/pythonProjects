import queue
import threading
from time import sleep


class Stream:
    def __init__(self):
        self.queue = queue.Queue()
        self.threading = threading.Thread(target=self.activation)
        self.threading.start()
        self.function = None

    def add(self, x):
        self.queue.put(x)

    def stop(self):
       self.threading.join()

    def activation(self):
        while True:
            try:
                x = self.queue.get(timeout=0.5)
                self.function(x)
            except queue.Empty:
                break
            
        if queue.Empty:
            sleep(0.1)

    def forEach(self, f):
        self.function = f

    def apply(self, f):
        s = Stream()
        def g(x):
            if f(x) is True:
                s.add(x)
            else:
                y = f(x)
                if type(y) is int:
                    s.add(y)
        self.forEach(g)
        return s




