document.addEventListener("DOMContentLoaded", () => {
  // Registration Form Logic
  const registrationForm = document.getElementById("registrationForm");

  if (registrationForm) {
    const firstName = document.getElementById("first_name");
    const lastName = document.getElementById("last_name");
    const username = document.getElementById("username");
    const email = document.getElementById("email");
    const password1 = document.getElementById("password1");
    const password2 = document.getElementById("password2");

    registrationForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const isValid =
        validateNotEmpty(firstName, "First Name") &&
        validateNotEmpty(lastName, "Last Name") &&
        validateNotEmpty(username, "Username") &&
        validateEmail(email) &&
        validatePasswordStrength() &&
        validatePasswordMatch();

      if (isValid) registrationForm.submit();
    });
  }

  // Target the login form
  const loginForm = document.getElementById("loginForm");

  // Proceed only if the form exists
  if (loginForm) {
    // Select fields
    const usernameField = document.getElementById("username");
    const passwordField = document.getElementById("password");

    // Function to show error messages
    const showError = (input, message) => {
      let error = input.nextElementSibling;
      if (!error) {
        error = document.createElement("small");
        error.className = "text-danger";
        input.parentNode.appendChild(error);
      }
      error.textContent = message;
    };

    // Function to clear error messages
    const clearError = (input) => {
      let error = input.nextElementSibling;
      if (error) error.textContent = "";
    };

    // Validate that a field is not empty
    const validateNotEmpty = (input, fieldName) => {
      if (input.value.trim() === "") {
        showError(input, `${fieldName} cannot be empty.`);
        return false;
      }
      clearError(input);
      return true;
    };

    // Add form submission handler
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault(); // Prevent default form submission

      // Validate username and password fields
      const isUsernameValid = validateNotEmpty(usernameField, "Username");
      const isPasswordValid = validateNotEmpty(passwordField, "Password");

      if (isUsernameValid && isPasswordValid) {
        loginForm.submit(); // Submit the form if both fields are valid
      }
    });
  }
});
