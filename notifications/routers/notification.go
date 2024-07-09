// booking_platform/notifications/routers/notification.go

package routers

import (
    "encoding/json"
    "net/http"
    "strconv"
    "github.com/gorilla/mux"
    "booking_platform/notifications/models"
)

var notifications []models.Notification

func RegisterNotificationRoutes(router *mux.Router) {
    router.HandleFunc("/notifications", getNotifications).Methods("GET")
    router.HandleFunc("/notifications/{id}", getNotification).Methods("GET")
    router.HandleFunc("/notifications", createNotification).Methods("POST")
    router.HandleFunc("/notifications/{id}", updateNotification).Methods("PUT")
    router.HandleFunc("/notifications/{id}", deleteNotification).Methods("DELETE")
}

func getNotifications(w http.ResponseWriter, r *http.Request) {
    json.NewEncoder(w).Encode(notifications)
}

func getNotification(w http.ResponseWriter, r *http.Request) {
    params := mux.Vars(r)
    id, _ := strconv.Atoi(params["id"])
    for _, item := range notifications {
        if item.ID == id {
            json.NewEncoder(w).Encode(item)
            return
        }
    }
    w.WriteHeader(http.StatusNotFound)
    json.NewEncoder(w).Encode("Notification not found")
}

func createNotification(w http.ResponseWriter, r *http.Request) {
    var notification models.Notification
    _ = json.NewDecoder(r.Body).Decode(&notification)
    notification.ID = len(notifications) + 1
    notifications = append(notifications, notification)
    json.NewEncoder(w).Encode(notification)
}

func updateNotification(w http.ResponseWriter, r *http.Request) {
    params := mux.Vars(r)
    id, _ := strconv.Atoi(params["id"])
    for index, item := range notifications {
        if item.ID == id {
            notifications = append(notifications[:index], notifications[index+1:]...)
            var notification models.Notification
            _ = json.NewDecoder(r.Body).Decode(&notification)
            notification.ID = id
            notifications = append(notifications, notification)
            json.NewEncoder(w).Encode(notification)
            return
        }
    }
    w.WriteHeader(http.StatusNotFound)
    json.NewEncoder(w).Encode("Notification not found")
}

func deleteNotification(w http.ResponseWriter, r *http.Request) {
    params := mux.Vars(r)
    id, _ := strconv.Atoi(params["id"])
    for index, item := range notifications {
        if item.ID == id {
            notifications = append(notifications[:index], notifications[index+1:]...)
            json.NewEncoder(w).Encode("Notification deleted")
            return
        }
    }
    w.WriteHeader(http.StatusNotFound)
    json.NewEncoder(w).Encode("Notification not found")
}
