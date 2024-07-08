// booking_platform/services/notifications/app/models.go

package main

type Notification struct {
    ID      int    `json:"id"`
    Message string `json:"message"`
    UserID  int    `json:"user_id"`
}
