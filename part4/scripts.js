/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

      if (loginForm) {
          loginForm.addEventListener('submit', async (event) => {
              event.preventDefault();
              // Your code to handle form submission
          });
      }

    async function loginUser(email, password) {
    const response = await fetch('https://your-api-url/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });
    // Handle the response
    }
    
    if (response.ok) {
        const data = await response.json();
        document.cookie = `token=${data.access_token}; path=/`;
        window.location.href = 'index.html';
    } else {
        alert('Login failed: ' + response.statusText);
    }

    function checkAuthentication() {
        const token = getCookie('token');
        const loginLink = document.getElementById('login-link');

        if (!token) {
            loginLink.style.display = 'block';
        } else {
            loginLink.style.display = 'none';
            // Fetch places data if the user is authenticated
            fetchPlaces(token);
        }
    }
    function getCookie(name) {
        // Function to get a cookie value by its name
        // Your code here
    }

      const placesContainer = document.getElementById('places-list');

    if (placesContainer) {
        fetch("YOUR_API/places")
        .then(res => res.json())
        .then(data => {
            data.forEach(place => {
                placesContainer.innerHTML += `
                <div class="place-card">
                    <h2>${place.name}</h2>
                    <p>${place.price} per night</p>
                    <a href="place.html?id=${place.id}" class="details-button">
                        View Details
                    </a>
                </div>
                `;
            });
        });
    }
});