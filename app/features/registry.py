from typing import Any, Callable

_REGISTRY: dict[str, Callable[..., Any]] = {}


def register(name: str, fn: Callable[..., Any]) -> None:
    _REGISTRY[name] = fn


def get(name: str) -> Callable[..., Any]:
    return _REGISTRY[name]


def all_features() -> dict[str, Callable[..., Any]]:
    return dict(_REGISTRY)
