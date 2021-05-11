""" create thread demo """

import threading
import time

def do_it(sleep_time: int) -> None:
    """ do it function """
    time.sleep(sleep_time)
    print("".join([
        "did it: thread id -> ",
        str(threading.get_ident()),
        ", thread name -> ",
        threading.current_thread().name
    ]))

thread1 = threading.Thread(target=do_it, name="thread1", args=(2,))
thread1.start()

thread2 = threading.Thread(target=do_it, name="thread2", args=(1,))
thread2.start()

print("made it here")
