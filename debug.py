import ptvsd
import time

def attach_port():
    address = ('0.0.0.0', 2500)
    ptvsd.enable_attach(address)
    ptvsd.wait_for_attach()
    time.sleep(2)
    print("Waiting to attach")