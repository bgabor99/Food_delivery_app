/* used in usersignappage.html and in userlogin.html pages */

function togglePasswordAndConfirm() {
    var passwordInput = document.getElementById("typePasswordX-2");
    var confirmInput = document.getElementById("typePasswordX-3");
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      confirmInput.type = "text";
    } else {
      passwordInput.type = "password";
      confirmInput.type = "password";
    }
}


function togglePassword() {
    var passwordInput = document.getElementById("passwordInp");
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
    } else {
      passwordInput.type = "password";
    }
}
