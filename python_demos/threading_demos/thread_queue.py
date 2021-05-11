""" thread queue """

import threading
import queue
import time
from random import randint

nums: queue.Queue[int] = queue.Queue()
double_nums: queue.Queue[int] = queue.Queue()


def generate_nums(queue_nums: queue.Queue[int]) -> None:
    """ generate numbers """

    while True:
        num = randint(1,11)
        queue_nums.put(num)
        time.sleep(1)

def double_the_nums(
    queue_nums: queue.Queue[int],
    queue_double_nums: queue.Queue[int]) -> None:
    """ double numbers """

    while True:
        num = queue_nums.get()
        queue_double_nums.put(num * 2)

def output_nums(queue_double_nums: queue.Queue[int]) -> None:
    """ output numbers """

    while True:
        num = queue_double_nums.get()
        print(num)



generate_nums_thread = threading.Thread(target=generate_nums, args=(nums,))
double_the_nums_thread = threading.Thread(
    target=double_the_nums, args=(nums,double_nums))
output_nums_thread = threading.Thread(target=output_nums, args=(double_nums,))

generate_nums_thread.start()
double_the_nums_thread.start()
output_nums_thread.start()
