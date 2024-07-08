# booking_platform/services/notifications/Dockerfile

# Use the official Golang image from the Docker Hub
FROM golang:1.18

# Set the working directory
WORKDIR /app

# Copy go.mod and go.sum files
COPY go.mod go.sum ./

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download

# Copy the source from the current directory to the working Directory inside the container
COPY . .

# Build the Go app
RUN go build -o /notifications ./app/main.go

# Expose port 8004 to the outside world
EXPOSE 8004

# Command to run the executable
CMD ["/notifications"]
