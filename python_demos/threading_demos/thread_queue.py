""" thread queue """

import threading
import queue
import time
from random import randint

nums: queue.Queue[int] = queue.Queue()
double_nums: queue.Queue[int] = queue.Queue()

generate_nums_done = threading.Event()


def generate_nums(number_of_nums: int, queue_nums: queue.Queue[int]) -> None:
    """ generate numbers """

    for _ in range(number_of_nums):
        print("generate number")
        num = randint(1,11)
        queue_nums.put(num)
        time.sleep(1)

    generate_nums_done.set()

def double_the_nums(
    queue_nums: queue.Queue[int],
    queue_double_nums: queue.Queue[int]) -> None:
    """ double numbers """

    while True:
        try:
            num = queue_nums.get(timeout=0.1)
            queue_double_nums.put(num * 2)
        except queue.Empty:
            if generate_nums_done.is_set():
                break
            else:
                continue

def output_nums(queue_double_nums: queue.Queue[int]) -> None:
    """ output numbers """

    while True:
        num = queue_double_nums.get()
        print(num)



generate_nums_thread = threading.Thread(target=generate_nums, args=(10, nums))
double_the_nums_thread = threading.Thread(
    target=double_the_nums, args=(nums,double_nums))
output_nums_thread = threading.Thread(target=output_nums, args=(double_nums,))

generate_nums_thread.start()
double_the_nums_thread.start()
output_nums_thread.start()
