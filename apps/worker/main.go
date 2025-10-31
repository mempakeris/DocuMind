package main

import (
	"runtime"

	services "github.com/mempakeris/documind/worker/services"
)

func main() {
	numWorkers := runtime.NumCPU()
	messageQueue := services.ConnectToMessageQueue()
	defer messageQueue.Channel.Close()
	forever := make(chan bool)
	messages := services.ConsumeMessages(&messageQueue)
	for workerId := range numWorkers {
		go services.SendRequestsToAIService(workerId, messages)
	}
	<-forever
}
