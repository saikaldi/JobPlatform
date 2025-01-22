
document.addEventListener("DOMContentLoaded", () => {
  // Shared Functions
  const showError = (input, message) => {
    console.log(`Error on field "${input?.name}": ${message}`);
    let error = input.nextElementSibling;
    if (!error) {
      error = document.createElement("small");
      error.className = "text-danger";
      input.parentNode.appendChild(error);
    }
    error.textContent = message;
  };

  const clearError = (input) => {
    let error = input?.nextElementSibling;
    if (error) error.textContent = "";
  };

  const validateNotEmpty = (input, fieldName) => {
    if (!input) {
      console.error(`Missing input field: ${fieldName}`);
      return false;
    }

    if (input.value.trim() === "") {
      showError(input, `${fieldName} cannot be empty.`);
      input.classList.add("is-invalid");
      return false;
    }
    clearError(input);
    input.classList.remove("is-invalid");
    input.classList.add("is-valid");
    console.log(`"${fieldName}" passed validation.`);
    return true;
  };

  const validateEmail = (input) => {
    if (!input) {
      console.error("Missing email input field");
      return false;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(input.value.trim())) {
      showError(input, "Invalid email format.");
      input.classList.add("is-invalid");
      return false;
    }
    clearError(input);
    input.classList.remove("is-invalid");
    input.classList.add("is-valid");
    console.log("Email passed validation.");
    return true;
  };

  const validatePasswordStrength = (input) => {
    if (!input) {
      console.error("Missing password input field");
      return false;
    }

    if (input.value.length < 8) {
      showError(input, "Password must be at least 8 characters long.");
      input.classList.add("is-invalid");
      return false;
    }
    clearError(input);
    input.classList.remove("is-invalid");
    input.classList.add("is-valid");
    console.log("Password strength passed validation.");
    return true;
  };

  const validatePasswordMatch = (password1, password2) => {
    if (!password1 || !password2) {
      console.error("Missing password fields for match validation");
      return false;
    }

    if (password1.value !== password2.value) {
      showError(password2, "Passwords do not match.");
      password2.classList.add("is-invalid");
      return false;
    }
    clearError(password2);
    password2.classList.remove("is-invalid");
    password2.classList.add("is-valid");
    console.log("Passwords match.");
    return true;
  };

  // Real-Time Validation for Registration Form
  const registrationForm = document.getElementById("registrationForm");
  if (registrationForm) {
    console.log("Registration form detected.");
    const firstName = document.getElementById("first_name");
    const lastName = document.getElementById("last_name");
    const username = document.getElementById("username");
    const email = document.getElementById("email");
    const password1 = document.getElementById("password1");
    const password2 = document.getElementById("password2");

    // Add real-time validation listeners
    [firstName, lastName, username].forEach((field) => {
      if (field) {
        field.addEventListener("input", () =>
          validateNotEmpty(field, field.placeholder || field.name)
        );
      }
    });

    email?.addEventListener("input", () => validateEmail(email));
    password1?.addEventListener("input", () => validatePasswordStrength(password1));
    password2?.addEventListener("input", () => validatePasswordMatch(password1, password2));

    registrationForm.addEventListener("submit", (e) => {
      e.preventDefault();
      console.log("Submitting registration form...");

      const isValid =
        validateNotEmpty(firstName, "First Name") &&
        validateNotEmpty(lastName, "Last Name") &&
        validateNotEmpty(username, "Username") &&
        validateEmail(email) &&
        validatePasswordStrength(password1) &&
        validatePasswordMatch(password1, password2);

      console.log("Validation result for registration form:", isValid);

      if (isValid) {
        console.log("Form is valid. Submitting...");
        registrationForm.submit();
      } else {
        console.log("Form is invalid. Please correct the errors.");
      }
    });
  } else {
    console.warn("Registration form not found.");
  }

  // Real-Time Validation for Login Form
  const loginForm = document.getElementById("loginForm");
  if (loginForm) {
    console.log("Login form detected.");
    const usernameField = document.getElementById("username");
    const passwordField = document.getElementById("password");

    // Add real-time validation listeners
    usernameField?.addEventListener("input", () =>
      validateNotEmpty(usernameField, "Username")
    );
    passwordField?.addEventListener("input", () =>
      validateNotEmpty(passwordField, "Password")
    );

    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();
      console.log("Submitting login form...");

      const isUsernameValid = validateNotEmpty(usernameField, "Username");
      const isPasswordValid = validateNotEmpty(passwordField, "Password");

      console.log("Validation result for login form:", isUsernameValid && isPasswordValid);

      if (isUsernameValid && isPasswordValid) {
        console.log("Form is valid. Submitting...");
        loginForm.submit();
      } else {
        console.log("Form is invalid. Please correct.");
      }
    });
  } else {
    console.warn("Login form not found.");
  }
});

// jQuery for Notification Handling
$(document).ready(function () {
  var notification = $('#notification');
  // After 2 seconds, close the notification if it exists
  if (notification.length > 0) {
    setTimeout(function () {
      notification.fadeOut('slow', function () {
        $(this).remove(); // Remove the element from the DOM
        console.log("Notification script faded out.");
      });
    }, 2000); // 2 seconds
  }
});
