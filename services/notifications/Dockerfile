# booking_platform/services/notifications/Dockerfile

# Используем базовый образ с Go
FROM golang:1.18

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем go.mod и go.sum в рабочую директорию
COPY go.mod go.sum ./

# Загружаем зависимости
RUN go mod download

# Копируем исходный код в рабочую директорию
COPY . .

# Собираем бинарный файл
RUN go build -o /notifications ./app/main.go

# Экспонируем порт
EXPOSE 8003

# Команда запуска контейнера
CMD ["/notifications"]
