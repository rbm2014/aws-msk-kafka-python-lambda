# aws-msk-kafka-python-lambda

# AWS Lambda Functions for Kafka Consumer and Producer

### Note
> **Disclaimer:** Please note that while using any AWS service, you may incur costs associated with data usage, network charges, or other expenses. We want to emphasize that we are not responsible for any costs that may arise from your use of this service. It is your responsibility to be aware of and manage any associated costs.
> These are NOT production codes, it is a way to test the functionality of MSK using AWS Lambda

## Overview

This repository contains two AWS Lambda functions designed to interact with an Amazon Managed Streaming for Apache Kafka (MSK) cluster. These functions serve as a Kafka consumer and producer, respectively. 

- **Consumer Function:** This Lambda function consumes messages from a specified Kafka topic.
- **Producer Function:** This Lambda function produces messages to a specified Kafka topic.

## Functions

### Consumer Lambda Function

The consumer function connects to a Kafka cluster, retrieves messages from a specified topic, and processes these messages. It is designed to handle various Kafka partitions and offsets to ensure all messages are consumed.

**Key Features:**
- Connects to a Kafka cluster using provided bootstrap servers.
- Consumes messages from a specified topic.
- Handles partitions and offsets to ensure message consistency.
- Logs detailed information for debugging and monitoring.

### Producer Lambda Function

The producer function connects to a Kafka cluster and sends a specified message to a designated Kafka topic. It ensures the message is successfully delivered by flushing and closing the producer connection after sending the message.

**Key Features:**
- Connects to a Kafka cluster using provided bootstrap servers.
- Sends messages to a specified topic.
- Ensures delivery by flushing and closing the producer connection.
- Logs detailed information for debugging and monitoring.

## Deployment

To deploy these Lambda functions, follow these steps:

### Prerequisites

1. **AWS Account:** Ensure you have an active AWS account.
2. **IAM Role:** Create an IAM role with the necessary permissions for Lambda and MSK access.
3. **MSK Cluster:** Ensure you have an MSK cluster running and accessible.

### Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-repo-name.git
    cd your-repo-name
    ```

2. **Modify Placeholders:**
   
   Open the Lambda function scripts and replace the placeholders with your actual Kafka bootstrap servers, topic names, and any other necessary information.
   
   ```python
   bootstrap_servers = ['<YOUR_BOOTSTRAP_SERVER_1>', '<YOUR_BOOTSTRAP_SERVER_2>']
   topic_name = '<YOUR_TOPIC_NAME>'
   message = '<YOUR_MESSAGE>'  # For the producer function
