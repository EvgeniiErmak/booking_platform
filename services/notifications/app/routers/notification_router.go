// booking_platform/services/notifications/app/routers/notification_router.go

package routers

import (
    "encoding/json"
    "net/http"
    "strconv"

    "github.com/gorilla/mux"
    "booking_platform/services/notifications/app/models"
)

var notifications = make(map[int]models.Notification)
var idCounter = 1

func CreateNotificationHandler(w http.ResponseWriter, r *http.Request) {
    var notification models.Notification
    if err := json.NewDecoder(r.Body).Decode(&notification); err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    notification.ID = idCounter
    idCounter++
    notifications[notification.ID] = notification
    w.WriteHeader(http.StatusCreated)
    json.NewEncoder(w).Encode(notification)
}

func GetNotificationHandler(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    id, err := strconv.Atoi(vars["id"])
    if err != nil {
        http.Error(w, "Invalid ID", http.StatusBadRequest)
        return
    }
    notification, ok := notifications[id]
    if !ok {
        http.Error(w, "Notification not found", http.StatusNotFound)
        return
    }
    w.WriteHeader(http.StatusOK)
    json.NewEncoder(w).Encode(notification)
}
