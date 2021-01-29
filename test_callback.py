import registry
import events


class EventTest(object):
    def __init__(self):
        self.registry_event()

    def registry_event(self):
        registry.subscribe(self.create_network, 'network', events.CREATE)
        registry.subscribe(self.create_network1, 'network', events.CREATE)
        registry.subscribe(self.create_network2, 'network', events.CREATE)
        registry.subscribe(self.create_network3, 'network', events.CREATE)

        registry.subscribe(self.update_network, 'network', events.UPDATE)
        registry.subscribe(self.delete_network, 'network', events.DELETE)

    def create_network(self, resource, event, trigger, **kwargs):
        print("This is create_network")

    def update_network(self, resource, event, trigger, **kwargs):
        print("This is update_network")

    def delete_network(self, resource, event, trigger, **kwargs):
        print("This is delete_network")
    
    def create_network1(self, resource, event, trigger, **kwargs):
        print("This is create_network1")

    def create_network2(self, resource, event, trigger, **kwargs):
        print("This is create_network2")
    
    def create_network3(self, resource, event, trigger, **kwargs):
        print("This is create_network3")


def trigger():
    """In this function, you can trigger the callback"""
    while True:
        a = EventTest()
        action = input("Input your action <create, update, delete>: ")

        if action == 'create':
            registry.notify('network', events.CREATE, 'tigger')
        elif action == 'update':
            registry.notify('network', events.UPDATE, 'tigger')
        else:
            registry.notify('network', events.DELETE, 'tigger')


if __name__ == '__main__':
    trigger()
