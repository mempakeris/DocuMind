package utils

import (
	"log"
)

func FailOnError(err error, msg string) {
	if err == nil {
		return
	}
	log.Panicf("%s: %s", msg, err)
}
