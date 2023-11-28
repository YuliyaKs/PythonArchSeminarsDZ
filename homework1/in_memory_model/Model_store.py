from I_model_changer import I_model_changer
from I_model_changed_observer import I_model_changed_observer
from homework1.model_elements.Camera import Camera
from homework1.model_elements.Scene import Scene
from homework1.model_elements.Flash import Flash
from homework1.model_elements.Poligonal_model import Poligonal_model


class Model_store(I_model_changer):
    sender = I_model_changer
    models = [Poligonal_model]
    scenes = [Scene]
    flashes = [Flash]
    cameras = [Camera]
    __change_observes = I_model_changed_observer
    __n = int

    def __init__(self, models, scenes, flashes, cameras, __changes_observes):
        self.__changes_observes = __changes_observes
        self.models = models
        self.scenes = scenes
        self.models = flashes
        self.models = cameras

    def Get_scene(self, scene_id: int):
        return self.scenes.get(scene_id)

    def Notify_changer(self, sender):
        pass
