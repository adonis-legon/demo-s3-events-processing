from abc import ABC, abstractmethod


class EventProcessor(ABC):
    @abstractmethod
    def process(self, event_payload):
        pass


class PutEventProcessor(EventProcessor):
    def process(self, event_payload):
        bucket_name = event_payload['s3']['bucket']['name']
        object_key = event_payload['s3']['object']['key']

        print(
            f'Processed Put event for bucket: {bucket_name}, and key: {object_key}')


class DeleteEventProcessor(EventProcessor):
    def process(self, event_payload):
        bucket_name = event_payload['s3']['bucket']['name']
        object_key = event_payload['s3']['object']['key']

        print(
            f'Processed Delete event for bucket: {bucket_name}, and key: {object_key}')


class TransitionEventProcessor(EventProcessor):
    def process(self, event_payload):
        bucket_name = event_payload['s3']['bucket']['name']
        object_key = event_payload['s3']['object']['key']

        print(
            f'Processed Lifecycle Transition event for bucket: {bucket_name}, and key: {object_key}')
