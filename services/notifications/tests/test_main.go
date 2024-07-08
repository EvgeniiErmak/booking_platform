// booking_platform/services/notifications/tests/test_main.go

package main

import (
    "bytes"
    "encoding/json"
    "net/http"
    "net/http/httptest"
    "testing"

    "booking_platform/services/notifications/app/models"
    "booking_platform/services/notifications/app/routers"
    "booking_platform/services/notifications/app/handlers"
)

func TestHomeHandler(t *testing.T) {
    req, err := http.NewRequest("GET", "/", nil)
    if err != nil {
        t.Fatal(err)
    }
    rr := httptest.NewRecorder()
    handler := http.HandlerFunc(handlers.HomeHandler)
    handler.ServeHTTP(rr, req)

    if status := rr.Code; status != http.StatusOK {
        t.Errorf("handler returned wrong status code: got %v want %v",
            status, http.StatusOK)
    }

    expected := `{"message": "Welcome to the Notification Service"}`
    if rr.Body.String() != expected {
        t.Errorf("handler returned unexpected body: got %v want %v",
            rr.Body.String(), expected)
    }
}

func TestCreateNotificationHandler(t *testing.T) {
    notification := &models.Notification{Message: "Test message", UserID: 1}
    body, _ := json.Marshal(notification)
    req, err := http.NewRequest("POST", "/notifications", bytes.NewBuffer(body))
    if err != nil {
        t.Fatal(err)
    }
    rr := httptest.NewRecorder()
    handler := http.HandlerFunc(routers.CreateNotificationHandler)
    handler.ServeHTTP(rr, req)

    if status := rr.Code; status != http.StatusCreated {
        t.Errorf("handler returned wrong status code: got %v want %v",
            status, http.StatusCreated)
    }

    var createdNotification models.Notification
    json.NewDecoder(rr.Body).Decode(&createdNotification)
    if createdNotification.Message != notification.Message || createdNotification.UserID != notification.UserID {
        t.Errorf("handler returned unexpected body: got %v want %v",
            createdNotification, notification)
    }
}

func TestGetNotificationHandler(t *testing.T) {
    notification := &models.Notification{Message: "Test message", UserID: 1}
    routers.notifications[1] = *notification

    req, err := http.NewRequest("GET", "/notifications/1", nil)
    if err != nil {
        t.Fatal(err)
    }
    rr := httptest.NewRecorder()
    handler := http.HandlerFunc(routers.GetNotificationHandler)
    handler.ServeHTTP(rr, req)

    if status := rr.Code; status != http.StatusOK {
        t.Errorf("handler returned wrong status code: got %v want %v",
            status, http.StatusOK)
    }

    var retrievedNotification models.Notification
    json.NewDecoder(rr.Body).Decode(&retrievedNotification)
    if retrievedNotification.Message != notification.Message || retrievedNotification.UserID != notification.UserID {
        t.Errorf("handler returned unexpected body: got %v want %v",
            retrievedNotification, notification)
    }
}
