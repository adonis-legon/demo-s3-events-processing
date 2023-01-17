class EventProcessorNotSupportedException(Exception):
    def __init__(self, event_payload):
        self.event_payload = event_payload
