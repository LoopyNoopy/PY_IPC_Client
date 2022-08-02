import UI
import multiprocessing
from multiprocessing.connection import Client
from multiprocessing.connection import Listener

def IPCSend(value):
    IPCAddress = ('localhost',6000)
    global connection
    connection = Client(IPCAddress,authkey=b'blah')
    connection.send(value)
    connection.send("close")
    connection.close()
    return()

if __name__ == "__main__":
    # creating processes
    UIProcess = multiprocessing.Process(target=UI.App)
    UIProcess.start()
    UIProcess.join()

