import usb.core
import usb.util

class MySamplePyUsb:
    def __init__(self):
        self.inputs = []
        self.dev = None
        self.find_device()

    def find_device(self):
        # vendor: logitech, product: h390 headset
        vid = 0x046d
        pid = 0x0390

        # find our device
        self.dev = usb.core.find(idVendor=vid, idProduct=pid)

        # was it found?
        if self.dev is None:
            raise ValueError('Device not found')

if __name__ == '__main__':
    test = MySamplePyUsb()
