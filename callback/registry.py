from callback.manager import manager

_CALLBACK_MANAGER = None


def _get_callback_manger():
    global _CALLBACK_MANAGER
    if _CALLBACK_MANAGER is None:
        _CALLBACK_MANAGER = manager.CallbacksManager()
    return _CALLBACK_MANAGER


def subscribe(callback, resource, event):
    return _get_callback_manger().subscribe(callback, resource, event)


def unsubscribe(callback, resource, event):
    return _get_callback_manger().unsubscribe(callback, resource, event)


def unsubscribe_all(callback):
    return _get_callback_manger().unsubscribe_all(callback)


def clear():
    return _get_callback_manger().clear()


def publish(self, resource, event, trigger, payload=None):
    return _get_callback_manger().publish(resource, event, trigger, payload)


def notify(resource, event, trigger, **kwargs):
    return _get_callback_manger().notify(resource, event, trigger, **kwargs)
