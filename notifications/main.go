// booking_platform/notifications/main.go

package main

import (
    "log"
    "net/http"

    "github.com/gorilla/mux"
    "github.com/EvgeniiErmak/booking_platform/notifications/routers"
)

func main() {
    router := mux.NewRouter()
    routers.RegisterNotificationRoutes(router)
    log.Fatal(http.ListenAndServe(":8080", router))
}
