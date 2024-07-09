// booking_platform/notifications/tests/test_notification.go

package tests

import (
    "bytes"
    "encoding/json"
    "net/http"
    "net/http/httptest"
    "testing"
    "booking_platform/notifications/models"
    "booking_platform/notifications/routers"
    "github.com/gorilla/mux"
)

func TestGetNotifications(t *testing.T) {
    req, err := http.NewRequest("GET", "/notifications", nil)
    if err != nil {
        t.Fatal(err)
    }
    rr := httptest.NewRecorder()
    router := mux.NewRouter()
    routers.RegisterNotificationRoutes(router)
    router.ServeHTTP(rr, req)

    if status := rr.Code; status != http.StatusOK {
        t.Errorf("handler returned wrong status code: got %v want %v", status, http.StatusOK)
    }
}

func TestCreateNotification(t *testing.T) {
    notification := models.Notification{
        UserID:  1,
        Message: "Test notification",
        Status:  "pending",
    }
    body, _ := json.Marshal(notification)
    req, err := http.NewRequest("POST", "/notifications", bytes.NewBuffer(body))
    if err != nil {
        t.Fatal(err)
    }
    rr := httptest.NewRecorder()
    router := mux.NewRouter()
    routers.RegisterNotificationRoutes(router)
    router.ServeHTTP(rr, req)

    if status := rr.Code; status != http.StatusOK {
        t.Errorf("handler returned wrong status code: got %v want %v", status, http.StatusOK)
    }

    var createdNotification models.Notification
    json.NewDecoder(rr.Body).Decode(&createdNotification)
    if createdNotification.Message != notification.Message {
        t.Errorf("handler returned unexpected body: got %v want %v", createdNotification.Message, notification.Message)
    }
}
