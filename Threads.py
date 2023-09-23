import threading
from time import sleep
import concurrent.futures
# def myFunc(name):
#     for count in range(5):
#         print(f"{name}: {count}")
#         sleep(1)
#     print("all done")

# print("main thread")
# a = threading.Thread(target = myFunc, args = ("Alice",), daemon = True)
# print("starting Alice thread")
# a.start()
# sleep(2)
# print("end")

class MYDB:
    def __init__(self) -> None:
        self.value = 0
        self.lock = threading.Lock()
    def update(self, updateName):
        print(f'thread {updateName} started updating')
        with self.lock:
            local_var = self.value
            local_var+=1
            sleep(0.1)
            self.value = local_var
            print("release lock")
        print(f'thread {updateName} finish to update')

db = MYDB()
t1 = threading.Thread(target=db.update,args=['t1'])
t2 = threading.Thread(target=db.update, args=['t2'])
t1.start()
t2.start()
print(threading.active_count())
t1.join()
t2.join()
print(f'db value {db.value}')

def demoTask() ->int:
    sleep(5)
    return 24
 
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
f1 = executor.submit(demoTask)

print(f'task done status {f1.done}')
print(f'waiting for result')
print(f'result {f1.result()}')

executor.shutdown