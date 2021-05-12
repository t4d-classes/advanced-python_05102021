""" rates orchestrator module """

from typing import Any
import threading
import queue

process_rates_queue: queue.Queue[str] = queue.Queue()
save_rates_queue: queue.Queue[dict[str, Any]] = queue.Queue()

get_rates_done = threading.Event()
process_rates_done = threading.Event()
