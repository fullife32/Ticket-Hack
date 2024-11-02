document.getElementById('ticketForm').addEventListener('submit', async (e) => {
    e.preventDefault(); // Empêche le rechargement de la page lors de l'envoi du formulaire

    // Récupère les valeurs du formulaire
    const eventName = document.getElementById('eventName').value;
	const eventDate = document.getElementById('eventDate').value;
    const ticketQuantity = document.getElementById('ticketQuantity').value;
    const ticketPrice = document.getElementById('ticketPrice').value;

    // Prépare les données pour l'envoi
    const ticketData = {
        ticket_numbers: parseInt(ticketQuantity),
        event_name: eventName,
        unary_price: parseFloat(ticketPrice),
		event_date: eventDate
    };

    try {
        // Envoie les données à l'API
        const response = await fetch('http://localhost:5000/tickets', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(ticketData)
        });

        // Vérifie la réponse de l'API
        if (response.ok) {
            alert('Tickets successfully created !');
			fetchTickets();
        } else {
            alert('Error creating tickets.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occured. Try again');
    }
});

// Fonction pour récupérer les tickets depuis l'API
async function fetchTickets() {
    try {
        const response = await fetch('http://localhost:5000/tickets', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            const tickets = await response.json();
            const ticketSection = document.getElementById('ticketSection');
            const ticketList = document.getElementById('ticketList');
            ticketList.innerHTML = ''; // Efface tout contenu existant

            if (tickets.length > 0) {
                // Affiche la section uniquement s'il y a des tickets
                ticketSection.style.display = 'block';

                tickets.forEach(ticket => {
                    const listItem = document.createElement('li');
                    listItem.textContent = `Ticket for ${ticket.event_name} at ${ticket.price} algo (${ticket.id}) ${ticket.event_date}`;
                    ticketList.appendChild(listItem);
                });
            } else {
                // Masque la section si aucun ticket n'est disponible
                ticketSection.style.display = 'none';
            }
        } else {
            console.error('Error retrieving tickets');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}


// Appel initial pour charger les tickets au chargement de la page
document.addEventListener('DOMContentLoaded', fetchTickets);

// "consumed": false,
//             "event_date": "Tue, 05 Nov 2024 00:00:00 GMT",
//             "event_name": "La fête du slip",
//             "id": "0e5fff3f-c93e-4b1f-820c-eee101b73ad5",
//             "price": 1.0