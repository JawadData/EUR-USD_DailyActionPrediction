document.getElementById('predictForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent page reload
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '<p>Loading...</p>'; // Show loading message

    fetch('/predict', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerHTML = ''; // Reset previous content
        
        if (data.error) {
            resultDiv.innerHTML = `<p>${data.error}</p>`; // Show error if exists
        } else {
            // Display the results in styled boxes
            const actionClass = data.action === "Sell" ? "" : "buy"; // Determine action class for styling
            for (const key in data) {
                if (data.hasOwnProperty(key) && key !== "action") {
                    const value = data[key];
                    resultDiv.innerHTML += `
                        <div class="result-box">
                            <h3>${key}</h3>
                            <p>${value}</p>
                        </div>
                    `;
                }
            }
            // Add action box at the end
            resultDiv.innerHTML += `
                <div class="action-box ${actionClass}">
                    <h3>Action</h3>
                    <p>${data.action}</p>
                </div>
            `;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
