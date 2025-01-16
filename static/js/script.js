
document.addEventListener("DOMContentLoaded", () => {
  // Elements
  const form = document.querySelector("form");
  const firstName = document.getElementById("first_name");
  const lastName = document.getElementById("last_name");
  const username = document.getElementById("username");
  const email = document.getElementById("email");
  const password1 = document.getElementById("password1");
  const password2 = document.getElementById("password2");

  // Error Display Helper
  const showError = (input, message) => {
    let error = input.nextElementSibling;
    if (!error) {
      error = document.createElement("small");
      error.className = "text-danger";
      input.parentNode.appendChild(error);
    }
    error.textContent = message;
  };

  const clearError = (input) => {
    let error = input.nextElementSibling;
    if (error) {
      error.textContent = "";
    }
  };

  // Validation Functions
  const validateNotEmpty = (input, fieldName) => {
    if (input.value.trim() === "") {
      showError(input, `${fieldName} cannot be empty.`);
      return false;
    }
    clearError(input);
    return true;
  };

  const validateEmail = (input) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(input.value)) {
      showError(input, "Please enter a valid email.");
      return false;
    }
    clearError(input);
    return true;
  };

  const validatePasswordMatch = () => {
    if (password1.value !== password2.value) {
      showError(password2, "Passwords do not match.");
      return false;
    }
    clearError(password2);
    return true;
  };

  const validatePasswordStrength = () => {
    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!passwordRegex.test(password1.value)) {
      showError(password1, "Password must be at least 8 characters long and include letters and numbers.");
      return false;
    }
    clearError(password1);
    return true;
  };



  // Form Submission Handler
  form.addEventListener("submit", (e) => {
    e.preventDefault(); // Prevent form submission

    // Validate Fields
    const isValid =
      validateNotEmpty(firstName, "First Name") &&
      validateNotEmpty(lastName, "Last Name") &&
      validateNotEmpty(username, "Username") &&
      validateEmail(email) &&
      validatePasswordStrength() &&
      validatePasswordMatch();

    if (isValid) {
      form.submit(); // Submit the form if all validations pass
    }
  });
});

