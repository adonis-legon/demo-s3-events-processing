import json
from .services import EventProcessService
from .exceptions import EventProcessorNotSupportedException

event_procesor_servive = EventProcessService()


def lambda_handler(event, context):
    fail_response = None
    try:
        events_count = 0

        for sqs_event_payload in event['Records']:
            sqs_event_payload_body = json.loads(sqs_event_payload['body'])
            for s3_event_payload in sqs_event_payload_body['Records']:
                event_procesor_servive.process(s3_event_payload)
                events_count += 1

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"Successfully processed {events_count} event(s)",
            }),
        }
    except EventProcessorNotSupportedException as event_error:
        fail_response = {
            "statusCode": 400,
            "body": json.dumps({
                "message": f"Unsupported event. Payload: {event_error.event_payload}"
            }),
        }
    except Exception as error:
        fail_response = {
            "statusCode": 500,
            "body": json.dumps({
                "message": f"Error processing events. Message: {str(error)}",
            }),
        }

    print(json.dumps(fail_response))
    return fail_response
