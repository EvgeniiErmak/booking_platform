// booking_platform/notifications/main.go

package main

import (
    "log"
    "net/http"
    "github.com/gorilla/mux"
    "booking_platform/notifications/routers"
)

func main() {
    r := mux.NewRouter()
    routers.RegisterNotificationRoutes(r)
    http.Handle("/", r)
    log.Println("Starting notification service on port 8080...")
    log.Fatal(http.ListenAndServe(":8080", r))
}
