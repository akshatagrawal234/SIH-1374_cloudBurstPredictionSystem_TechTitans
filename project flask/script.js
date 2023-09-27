document.getElementById("openPageButton").addEventListener("click", function () {
    const conditionSelect = document.getElementById("conditionSelect");
    const selectedCondition = conditionSelect.value;

    // Create an object with the input data
    const inputData = { input_data: selectedCondition };

    // Make an AJAX request to the Flask server to get the prediction
    fetch("/predict", {
        method: "POST",
        body: JSON.stringify(inputData),  // Send input data as JSON
        headers: {
            "Content-Type": "application/json", // Set content type to JSON
        },
    })
    .then(response => response.json())
    .then(data => {
        const prediction = data.prediction;

        // Open different pages based on the prediction value
        switch (prediction) {
            case "0":
                window.open("output1.html", "_blank");
                break;
            case "1":
                window.open("output3.html", "_blank");
                break;
            default:
                alert("No specific condition selected.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while fetching the prediction.");
    });
});
