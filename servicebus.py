import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage
from azure.identity.aio import DefaultAzureCredential

FULLY_QUALIFIED_NAMESPACE = "market.servicebus.windows.net"
QUEUE_NAME = "portfolio_req_queue"

credential = DefaultAzureCredential()

async def send_single_message(sender):
    # Create a Service Bus message and send it to the queue
    message = ServiceBusMessage("quit")
    await sender.send_messages(message)
    print("Sent a single message")

async def run():
    # create a Service Bus client using the credential
    async with ServiceBusClient(
        fully_qualified_namespace=FULLY_QUALIFIED_NAMESPACE,
        credential=credential,
        logging_enable=True) as servicebus_client:
        # get a Queue Sender object to send messages to the queue
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
        async with sender:
            # send one message
            await send_single_message(sender)
        # Close credential when no longer needed.
        await credential.close()


asyncio.run(run())
print("Done sending messages")
print("-----------------------")

