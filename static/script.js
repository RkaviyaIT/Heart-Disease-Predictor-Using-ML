document.getElementById("predict-form").onsubmit = async function (event) {
    event.preventDefault(); // Prevent default form submission

    const button = document.getElementById("submit-btn");
    button.textContent = 'Submitting...';
    button.disabled = true;

    const formData = new FormData(event.target); // Get form data

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        // Check if the response is OK (status code 200)
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json(); // Parse the JSON response
        alert('Prediction: ' + data.result); // Display prediction result
    } catch (error) {
        console.error('Error:', error); // Log error to console
        alert('An error occurred. Please try again.'); // Show error message
    } finally {
        button.textContent = 'Predict'; // Reset button text
        button.disabled = false; // Enable button again
    }
};
