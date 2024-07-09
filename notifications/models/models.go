// booking_platform/notifications/models/models.go

package models

type Notification struct {
    ID      int    `json:"id"`
    UserID  int    `json:"user_id"`
    Message string `json:"message"`
    Status  string `json:"status"`
}

func GetAllNotifications() []Notification {
    // Здесь должна быть логика получения уведомлений
    return []Notification{}
}
