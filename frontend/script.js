// booking_platform/frontend/script.js

document.addEventListener('DOMContentLoaded', function() {
    fetchUsers();
    fetchVenues();
    fetchReservations();
});

function fetchUsers() {
    fetch('http://localhost:8000/users')
        .then(response => response.json())
        .then(data => {
            const userList = document.getElementById('user-list');
            userList.innerHTML = '';
            data.forEach(user => {
                const userDiv = document.createElement('div');
                userDiv.className = 'user';
                userDiv.innerHTML = `<strong>${user.name}</strong> - ${user.email}`;
                userList.appendChild(userDiv);
            });
        })
        .catch(error => console.error('Error fetching users:', error));
}

function fetchVenues() {
    fetch('http://localhost:8001/venues')
        .then(response => response.json())
        .then(data => {
            const venueList = document.getElementById('venue-list');
            venueList.innerHTML = '';
            data.forEach(venue => {
                const venueDiv = document.createElement('div');
                venueDiv.className = 'venue';
                venueDiv.innerHTML = `<strong>${venue.name}</strong> - ${venue.address}`;
                venueList.appendChild(venueDiv);
            });
        })
        .catch(error => console.error('Error fetching venues:', error));
}

function fetchReservations() {
    fetch('http://localhost:8002/reservations')
        .then(response => response.json())
        .then(data => {
            const reservationList = document.getElementById('reservation-list');
            reservationList.innerHTML = '';
            data.forEach(reservation => {
                const reservationDiv = document.createElement('div');
                reservationDiv.className = 'reservation';
                reservationDiv.innerHTML = `<strong>Reservation ID:</strong> ${reservation.id} <strong>User ID:</strong> ${reservation.user_id} <strong>Venue ID:</strong> ${reservation.venue_id} <strong>Date:</strong> ${reservation.date}`;
                reservationList.appendChild(reservationDiv);
            });
        })
        .catch(error => console.error('Error fetching reservations:', error));
}
