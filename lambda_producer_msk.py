import json
import logging
from kafka import KafkaProducer

def lambda_handler(event, context):
    
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the desired logging level (INFO, ERROR, DEBUG, etc.)

    # Replace with your Kafka broker's bootstrap server(s)
    bootstrap_servers = ['<YOUR_BOOTSTRAP_SERVER_1>', '<YOUR_BOOTSTRAP_SERVER_2>']
    topic_name = '<YOUR_TOPIC_NAME>'
    message = '<YOUR_MESSAGE>'
    
    logger.info('Lambda function started')
    
    try:

        logger.info('Starting Lambda function - Kafka producer')
        logger.info('Done')
        
        # Create Kafka producer
        logger.info('Creating Kafka producer...')
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        logger.info('Kafka producer created')
        
        # Produce message to topic
        logger.info('Sending message to topic...')
        producer.send(topic_name, message.encode('utf-8'))
        logger.info('Message sent to topic')
        
        # Flush and close producer
        logger.info('Flushing and closing producer...')
        producer.flush()
        logger.info('Producer flushed')
        producer.close()
        logger.info('Producer closed')
        logger.info('------------------------')

        logger.info('Message sent successfully!')
        logger.info('Lambda function completed')
        
    except Exception as e:
        logger.error(f'Error processing Lambda function: {e}', exc_info=True)
        raise  # Rethrow the exception if needed or handle it appropriately
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent successfully!')
    }
