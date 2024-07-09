// booking_platform/frontend/script.js

document.addEventListener('DOMContentLoaded', function() {
    fetchUsers();
    fetchVenues();
    fetchReservations();

    document.getElementById('user-form').addEventListener('submit', function(event) {
        event.preventDefault();
        addUser();
    });

    document.getElementById('venue-form').addEventListener('submit', function(event) {
        event.preventDefault();
        addVenue();
    });

    document.getElementById('reservation-form').addEventListener('submit', function(event) {
        event.preventDefault();
        addReservation();
    });
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

function addUser() {
    const name = document.getElementById('user-name').value;
    const email = document.getElementById('user-email').value;

    fetch('http://localhost:8000/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email }),
    })
    .then(response => response.json())
    .then(data => {
        fetchUsers();
    })
    .catch(error => console.error('Error adding user:', error));
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

function addVenue() {
    const name = document.getElementById('venue-name').value;
    const address = document.getElementById('venue-address').value;

    fetch('http://localhost:8001/venues', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, address }),
    })
    .then(response => response.json())
    .then(data => {
        fetchVenues();
    })
    .catch(error => console.error('Error adding venue:', error));
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

function addReservation() {
    const user_id = document.getElementById('reservation-user-id').value;
    const venue_id = document.getElementById('reservation-venue-id').value;
    const date = document.getElementById('reservation-date').value;

    fetch('http://localhost:8002/reservations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id, venue_id, date }),
    })
    .then(response => response.json())
    .then(data => {
        fetchReservations();
    })
    .catch(error => console.error('Error adding reservation:', error));
}
