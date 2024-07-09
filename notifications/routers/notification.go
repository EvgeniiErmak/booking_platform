// booking_platform/notifications/routers/notification.go

package routers

import (
    "net/http"
    "encoding/json"
    "github.com/gorilla/mux"
    "github.com/EvgeniiErmak/booking_platform/notifications/models"
)

func RegisterNotificationRoutes(router *mux.Router) {
    router.HandleFunc("/notifications", GetNotifications).Methods("GET")
}

func GetNotifications(w http.ResponseWriter, r *http.Request) {
    notifications := models.GetAllNotifications()

    response := map[string]interface{}{
        "message": "Сервер уведомлений работает корректно!",
        "notifications": notifications,
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(response)
}
