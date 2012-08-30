

class EventMount(type):
    """ metaclass to register events
    """
    def __init__(cls,name,bases,attrs):
        if not hasattr(cls,"script_events"):
            cls.event_handlers=[]
        else:
            cls.event_handlers.append(cls)
class TransitionHandler(object):
    """ classes subclassing this will be used to handle script step transitions
    and must provide the transition method
    """
    def transition(self,progress):
        """
        """
    __metaclass__=EventMount



def handle_transitions(**kwargs):
    connection = kwargs['connection']
    progress = kwargs['sender']
    for handler in TransitionHandler.event_handlers:
        handler().transition(progress)
