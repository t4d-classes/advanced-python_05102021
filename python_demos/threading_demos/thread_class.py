""" thread class module """

import threading

class DoItThread(threading.Thread):
    """ do it thread class """

    def __init__(self, msg: str) -> None:
        threading.Thread.__init__(self)
        self.msg = msg

    def run(self) -> None:
        print("do it thread id: ", threading.get_ident())
        self.whoami()
        print(self.msg)


    def whoami(self) -> None:
        """ who am i """
        print("who am id: ", threading.get_ident())

print("main thread id: ", threading.get_ident())


some_thread = DoItThread("This is fun!")

some_thread.start()

some_thread.whoami()

some_thread.join()
