""" thread queue """

import threading
import queue
import time
from random import randint

nums: queue.Queue[int] = queue.Queue()


def generate_nums(queue_nums: queue.Queue[int]) -> None:
    """ generate numbers """

    while True:
        num = randint(1,11)
        queue_nums.put(num)
        time.sleep(1)

def output_nums(queue_nums: queue.Queue[int]) -> None:
    """ output numbers """

    while True:
        num = queue_nums.get()
        print(num)



generate_nums_thread = threading.Thread(target=generate_nums, args=(nums,))
output_nums_thread = threading.Thread(target=output_nums, args=(nums,))

generate_nums_thread.start()
output_nums_thread.start()
