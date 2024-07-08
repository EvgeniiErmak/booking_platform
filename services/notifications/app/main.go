// booking_platform/services/notifications/app/main.go

package main

import (
    "log"
    "net/http"

    "github.com/gorilla/mux"
    "booking_platform/services/notifications/app/handlers"
    "booking_platform/services/notifications/app/routers"
)

func main() {
    r := mux.NewRouter()
    r.HandleFunc("/", handlers.HomeHandler)
    r.HandleFunc("/notifications", routers.CreateNotificationHandler).Methods("POST")
    r.HandleFunc("/notifications/{id}", routers.GetNotificationHandler).Methods("GET")

    log.Println("Server started at :8004")
    log.Fatal(http.ListenAndServe(":8004", r))
}
