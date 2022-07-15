import UI
import multiprocessing
from multiprocessing.connection import Client

def IPCSetup(value):
    IPCAddress = ('localhost',6000)
    connection = Client(IPCAddress,authkey=b'blah')
    connection.send(value)
    print(value)
    return()

if __name__ == "__main__":
    # creating processes
    multiprocessing.Process(target=UI.App).start()