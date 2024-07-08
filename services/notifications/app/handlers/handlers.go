// booking_platform/services/notifications/app/handlers/handlers.go

package handlers

import (
    "net/http"
)

func HomeHandler(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
    w.Write([]byte(`{"message": "Welcome to the Notification Service"}`))
}
