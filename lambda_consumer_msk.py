import json
import logging
import boto3
import botocore
from kafka import KafkaConsumer, TopicPartition

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    # Replace with your Kafka broker's bootstrap server(s)
    bootstrap_servers = ['<YOUR_BOOTSTRAP_SERVER_1>', '<YOUR_BOOTSTRAP_SERVER_2>']
    topic_name = '<YOUR_TOPIC_NAME>'
    
    try:
        print('Starting Lambda function - Kafka consumer...')
        logger.info('LOG INFO - starting consumer function...')
        
        # Create Kafka consumer
        logger.info('Creating Kafka consumer...')
        consumer = KafkaConsumer(
            topic_name,
            #group_id='<YOUR_CONSUMER_GROUP>',
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=False,
        )
        logger.info('Kafka consumer created')
    
        PARTITIONS = []
        for partition in consumer.partitions_for_topic(topic_name):
            logger.info('Looping through partitions')
            PARTITIONS.append(TopicPartition(topic_name, partition))
            
        end_offsets = consumer.end_offsets(PARTITIONS)
        print('Offsets:')
        print(end_offsets)
        
        # Create the key
        partition = TopicPartition(topic_name, 0)
        
        # Extract the value using the key
        offset_value = end_offsets[partition]
        
        # Print the variable
        print(f"Extracted Offset Value: {offset_value}")
        
        # Get partitions for the topic
        partitions = [TopicPartition(topic_name, p) for p in consumer.partitions_for_topic(topic_name)]
        # Get earliest and latest offsets
        earliest_offsets = consumer.beginning_offsets(partitions)
        latest_offsets = consumer.end_offsets(partitions)
        
        print(f"Earliest Offset: {earliest_offsets}")
        print(f"Latest Offset: {latest_offsets}")
        
        # Calculate total number of messages in the topic
        total_messages = 0
        for partition in partitions:
            start_offset = earliest_offsets[partition]
            end_offset = latest_offsets[partition]
            partition_message_count = end_offset - start_offset
            total_messages += partition_message_count
            logger.info(f"Partition {partition.partition} has {partition_message_count} messages (offset {start_offset} to {end_offset})")
        
        logger.info(f"Total number of messages in topic '{topic_name}': {total_messages}")
        print(f"Total number of messages in topic '{topic_name}': {total_messages}")
        
        # Consume messages
        logger.info('Consuming messages...')
        i = 0 
        messages = []
        for message in consumer:
            print(f"Message index: {i}")
            logger.info(f"Message found: {message.value.decode('utf-8')}")
            print(f"Topic: {message.topic}, Partition: {message.partition}, Offset: {message.offset}, "
                  f"Key: {message.key}, Value: {message.value.decode('utf-8')}")
            messages.append(message.value.decode('utf-8'))
            
            i += 1

            if len(messages) >= total_messages:
                break
        
        consumer.close()
        logger.info('Kafka consumer closed')
        logger.info('------------------------')
        print('Lambda function - Kafka consumer done')

        return {
            'statusCode': 200,
            'body': json.dumps(messages)
        }

    except Exception as e:
        logger.error(f"Failed to consume messages: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Failed to consume messages: {str(e)}")
        }
