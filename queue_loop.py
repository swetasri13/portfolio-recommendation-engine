import logging
import os
import sys

from azure.servicebus import ServiceBusClient, ServiceBusMessage


def receive_messages(test_queue, validation_queue):

    conn_str = 'Endpoint=sb://market.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=T4zNlsMxNEQw+5B923N2Ej1JUZ91ITkz4+ASbCHOjws='
    if not conn_str:
        print("connection string not provided!")
        return

    servicebus_client = ServiceBusClient.from_connection_string(conn_str)
    receiver = servicebus_client.get_queue_receiver(queue_name=test_queue)
    

    receive_loop = True
    while receive_loop:
        received_msgs = receiver.receive_messages(max_message_count=1, max_wait_time=5)
        for msg in received_msgs:
            print('received message', msg)
    

            receiver.complete_message(msg)
            print('message completed')

            if str(msg) == "quit":
                receive_loop = False
                print("ending the loop...")

    receiver.close()
    servicebus_client.close()


if __name__ == '__main__':
    receive_messages("portfolio_req_queue", "test-validation")
    