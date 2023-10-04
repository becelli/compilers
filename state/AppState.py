from typing import Any, Callable


class AppState:
    def __init__(self):
        self.__state = {}
        self.__bindings = {}

    def get(self, key: str) -> Any:
        return self.__state.get(key)

    def bind(self, key: str, fn: Callable):
        if key not in self.__bindings:
            self.__bindings[key] = []
        self.__bindings[key].append(fn)
    
    def set(self, key: str, value: Any):
        print(f"Setting {key} to {value}")
        self.__state[key] = value
        if key in self.__bindings:
            for fn in self.__bindings[key]:
                fn(value)

    