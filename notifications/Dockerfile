# booking_platform/notifications/Dockerfile
FROM golang:1.16-alpine

WORKDIR /app

COPY . .

RUN go mod tidy
RUN go build -o notification_service .

CMD ["/app/notification_service"]
