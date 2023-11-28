from abc import ABCMeta

class I_model_changer(metaclass=ABCMeta):
    def notify_change(self, sender):
        return sender