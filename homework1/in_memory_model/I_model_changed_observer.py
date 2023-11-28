from abc import ABCMeta

class I_model_changed_observer(metaclass=ABCMeta):
    def apply_update_model(self):
        return None
