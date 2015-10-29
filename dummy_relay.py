

class Relay(object):
    """Dummy class for developing on Windows without import Raspberry Pi GPIO modules"""
    def __init__(self, pins=None):
        if pins:
            pass

    def on(self, pin):
        pass

    def off(self, pin):
        pass

    def reset(self):
        pass

    def pulse(self, pin, duration=0.2):
        pass

    def toggle(self, pin):
        pass

    def state(self, pin):
        """Returns pin state 0 or 1"""
        return 0
