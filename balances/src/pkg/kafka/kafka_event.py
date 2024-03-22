from typing import Any, Callable, List



class Event:
    def __init__(self):
        self._callbacks = []

    def subscribe(self, callback: Callable[..., Any]):
        self._callbacks.append(callback)

    def fire(self, *args, **kwargs):
        for callback in self._callbacks:
            callback(*args, **kwargs)