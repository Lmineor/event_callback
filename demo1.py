import time

from callback import events, registry


class EventTest(object):
    def __init__(self):
        self.registry_event()

    def registry_event(self):
        registry.subscribe(self.create_database, 'database', events.CREATE)
        
        registry.subscribe(self.create_table_student, 'database', events.AFTER_CREATE)
        registry.subscribe(self.create_table_class, 'database', events.AFTER_CREATE)
        registry.subscribe(self.create_table_teacher, 'database', events.AFTER_CREATE)

        registry.subscribe(self.update_database, 'database', events.UPDATE)
        registry.subscribe(self.delete_database, 'database', events.DELETE)

    def create_database(self, resource, event, trigger, **kwargs):
        print("*****starting create database*****")
        for i in range(3):
            time.sleep(1)
            print(".")
        print("*****create database finish*****")
        registry.notify('database', events.AFTER_CREATE, 'tigger')

    def update_database(self, resource, event, trigger, **kwargs):
        print("This is update_network")

    def delete_database(self, resource, event, trigger, **kwargs):
        print("This is delete_network")
    
    def create_table_student(self, resource, event, trigger, **kwargs):
        print("*****starting create student table*****")
        for i in range(3):
            time.sleep(1)
            print(".")
        print("*****create database finish*****")

    def create_table_class(self, resource, event, trigger, **kwargs):
        print("*****starting create class table*****")
        for i in range(3):
            time.sleep(1)
            print(".")
        print("*****create database finish*****")
    
    def create_table_teacher(self, resource, event, trigger, **kwargs):
        print("*****starting create teacher table*****")
        for i in range(3):
            time.sleep(1)
            print(".")
        print("*****create database finish*****")


def trigger():
    """In this function, you can trigger the callback"""
    while True:
        a = EventTest()
        action = input("Input your action <create, update, delete>: ")

        if action == 'create':
            registry.notify('database', events.CREATE, 'tigger')
        elif action == 'update':
            registry.notify('database', events.UPDATE, 'tigger')
        else:
            registry.notify('database', events.DELETE, 'tigger')

# 
if __name__ == '__main__':
    trigger()
