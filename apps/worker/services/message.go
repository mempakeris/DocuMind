package services

import (
	"fmt"

	utils "github.com/mempakeris/documind/worker/utils"
	amqp "github.com/rabbitmq/amqp091-go"
)

type MessageQueue struct {
	Channel *amqp.Channel
	Queue   amqp.Queue
}

func ConnectToMessageQueue() MessageQueue {
	config := utils.LoadConfig()
	path := fmt.Sprintf("amqp://%s:%s@%s:5672", config.MessageQueueUser, config.MessageQueuePass, config.MessageQueueVHost)
	conn, err := amqp.Dial(path)
	utils.FailOnError(err, "Failed to connect to RabbitMQ")
	ch, err := conn.Channel()
	utils.FailOnError(err, "Failed to open channel")

	const name = "knowledgeRequest"
	const isDurable = false
	const shouldDeleteWhenUnused = false
	const isExclusive = false
	const isNoWait = false
	queue, err := ch.QueueDeclare(
		name,
		isDurable,
		shouldDeleteWhenUnused,
		isExclusive,
		isNoWait,
		nil,
	)
	utils.FailOnError(err, "Failed to declare a queue")

	return MessageQueue{
		ch,
		queue,
	}
}

func ConsumeMessages(messageQueue *MessageQueue) <-chan amqp.Delivery {
	const consumerName = ""
	const shouldAutoAck = true
	const isExclusive = false
	const isNoLocal = false
	const isNoWait = false
	msgs, err := messageQueue.Channel.Consume(
		messageQueue.Queue.Name,
		consumerName,
		shouldAutoAck,
		isExclusive,
		isNoLocal,
		isNoWait,
		nil,
	)
	utils.FailOnError(err, "Failed to register a consumer")
	return msgs
}
