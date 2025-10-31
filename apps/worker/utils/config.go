package utils

import (
	"os"
)

type Config struct {
	MessageQueueUser  string
	MessageQueuePass  string
	MessageQueueVHost string
}

func LoadConfig() Config {
	return Config{
		MessageQueueUser:  os.Getenv("RABBITMQ_DEFAULT_USER"),
		MessageQueuePass:  os.Getenv("RABBITMQ_DEFAULT_PASS"),
		MessageQueueVHost: os.Getenv("RABBITMQ_DEFAULT_VHOST"),
	}
}
