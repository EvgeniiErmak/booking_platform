# booking_platform/notifications/Dockerfile

# Используем базовый образ golang
FROM golang:1.20

# Создаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY ./notifications /app

# Устанавливаем зависимости
RUN go mod init booking_platform
RUN go get -d -v ./...
RUN go install -v ./...

# Компилируем приложение
RUN go build -o /notification_service

# Открываем порт для сервиса
EXPOSE 8080

# Запускаем приложение
CMD ["/notification_service"]
