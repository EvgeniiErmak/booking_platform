// booking_platform/services/notifications/app/utils.go

package main

import (
    "encoding/json"
    "net/http"
)

func JSONResponse(w http.ResponseWriter, data interface{}, status int) {
    w.WriteHeader(status)
    if err := json.NewEncoder(w).Encode(data); err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
    }
}
