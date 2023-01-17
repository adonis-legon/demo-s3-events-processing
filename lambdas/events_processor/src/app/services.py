from .processors import PutEventProcessor, DeleteEventProcessor, TransitionEventProcessor
from .exceptions import EventProcessorNotSupportedException


class EventProcessorFactory():
    @staticmethod
    def get_processors():
        return {
            'ObjectCreated:Put': PutEventProcessor(),
            'ObjectRemoved:Delete': DeleteEventProcessor(),
            'LifecycleTransition': TransitionEventProcessor(),
        }


class EventProcessService():
    def __init__(self):
        self.processors = EventProcessorFactory.get_processors()

    def process(self, event_payload):
        if 'eventName' in event_payload:
            self.processors[event_payload['eventName']].process(event_payload)
        else:
            raise EventProcessorNotSupportedException(event_payload)
