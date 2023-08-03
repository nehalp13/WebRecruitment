// Get the form element and listen for form submission
const jobForm = document.getElementById('job-form');

jobForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get the input values from the form
    const jobTitle = document.getElementById('job-title').value;
    const jobLocation = document.getElementById('job-location').value;
    const jobExperience = document.getElementById('job-experience').value;

    // You can perform client-side validation here before submitting the data to the backend

    // For this example, we'll log the form data to the console
    console.log('Job Title:', jobTitle);
    console.log('Job Location:', jobLocation);
    console.log('Job Experience:', jobExperience);

    // You can use fetch or AJAX to send the form data to the backend for processing
    // For this example, we'll assume the data is sent successfully to the server
    // and show a success message to the user
    alert('Job posted successfully!');

    
});
