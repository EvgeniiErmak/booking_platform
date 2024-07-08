// booking_platform/services/notifications/app/models/models.go

package models

type Notification struct {
    ID      int    `json:"id"`
    Message string `json:"message"`
    UserID  int    `json:"user_id"`
}
