import collections

def get_callback_id(callback):
    """return a unique identifier for the callback"""
    parts = (callback.__name__, str(hash(callback)))
    return '-'.join(parts)


class CallbacksManager(object):
    """A callback system that allows objects to cooperate in a loose manner"""
    def __init__(self):
        self.clear()
    
    def clear(self):
        self._callbacks = collections.defaultdict(dict)
        self._index = collections.defaultdict(dict)
        
    def subscribe(self, callback, resource, event):
        """Subscribe callback for a resource event
        The same callback may register for more than one event.
        :param callback: the callback. It must raise or return a boolean
        :param resource: the resource. It must be a valid resource
        :param event: the event. It must be a valid event
        """
        callback_id = get_callback_id(callback)
        callback_list = self._callbacks[resource].setdefault(event, [])
        
        callbacks = {}
        callbacks[callback_id] = callback
        callback_list.append(callbacks)
        
        # We keep a copy of callbacks to speed the unsubscribe operation
        if callback_id not in self._index:
            self._index[callback_id] = collections.defaultdict(set)
        
        self._index[callback_id][resource].add(event)
        
    def unsubscribe(self, callback, resource, event):
        """Unsubscibe callback from the registry
        
        """
        callback_id = self._find(callback)
        if not callback_id:
            print("callback %s not found" % callback_id)
            return
        if resource and event:
            self._del_callback(self._callbacks[resource][event], callback_id)
            self._index[callback_id][resource].discard(event)
            if not self._index[callback_id][resource]:
                del self._index[callback_id][resource]
                if not self._index[callback_id]:
                    del self._index[callback_id]
            else:
                value = "%s,%s" %(resource, event)
                print("wrong", value)
                
    def unsubscribe_by_resource(self, callback, resource):
        """
        Unsubscribe callback for any evnet associated to the resource
        """
        callback_id = self._find(callback)
        if callback_id:
            if resource in self._index[callback_id]:
                for event in self._index[callback_id][resource]:
                    self._del_callback(self._callbacks[resource][event], callback_id)
                del self._index[callback_id][resource]
                
                if not self._index[callback_id]:
                    del self._index[callback_id]
        
    def unsubscribe_all(self, callback):
        """Unsubscribe callback for all events and all resource"""
        callback_id = self._find(callback)
        if callback_id:
            for resource, resource_events in self._index[callback_id].items():
                for event in resource_events:
                    self._del_callback(self._callbacks[resource][event], callback_id)
            del self._index[callback_id]
        
                
    def _del_callback(self, callback_list, callback_id):
        for id_callback_pairs in callback_list:
            if callback_id in id_callback_pairs:
                callback_list.remove(id_callback_pairs)
                break


    def publish(self, resource, event, trigger, payload=None):
        """
        Notify all subscribed callback(s) with a payload
        """
        #TODO verify the format of payload
        return self.notify(resource, event, trigger, payload=payload)
    
    def notify(self, resource, event, trigger, **kwargs):
        errors = self._notify_loop(resource, event, trigger, **kwargs)
        if errors:
            print(errors)
            # do something about the errors
        
    def _notify_loop(self, resource, event, trigger, **kwargs):
        errors = []
        callbacks = [callback.items() for callback in self._callbacks[resource].get(event, [])]
        for callback_dict in callbacks:
            for callback_id, callback in callback_dict:
                try:
                    callback(resource, event, trigger, **kwargs)
                except Exception as e:
                    print(e)
                    errors.append(e)
                    
        return errors
                    
    def _find(self, callback):
        callback_id = get_callback_id(callback)
        return callback_id if callback_id in self._index else None