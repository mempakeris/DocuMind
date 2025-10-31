package services

import (
	"encoding/json"
	"log"

	utils "github.com/mempakeris/documind/worker/utils"
	amqp "github.com/rabbitmq/amqp091-go"
)

type QueueTask struct {
	DocumentID    int      `json:"document_id"`
	FileStorePath string   `json:"file_store_path"`
	TaskTypes     []string `json:"task_types"`
	UserID        int      `json:"user_id"`
}

func SendRequestsToAIService(workerId int, jobs <-chan amqp.Delivery) {
	log.Printf("Worker %d preparing task", workerId)
	for job := range jobs {
		task := unmarshalTask(job.Body)
		log.Printf("Placeholder: %x", task)
	}
}

func unmarshalTask(serialized []byte) QueueTask {
	var task QueueTask
	err := json.Unmarshal(serialized, &task)
	utils.FailOnError(err, "Failed to unmarshal JSON")
	return task
}
