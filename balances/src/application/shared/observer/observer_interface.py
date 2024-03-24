from abc import ABC, ABCMeta, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class Subject(ABC):
    @abstractmethod
    def register(self, observer: Observer):
        pass

    @abstractmethod
    def unregister(self, observer: Observer):
        pass

    @abstractmethod
    def get_observers(self):
        pass

    @abstractmethod
    def notifyObservers(self, *args, **kwargs):
        pass