// Basic code to handle the "Try Grammar App" button in /about

function button_link(id)
    button_try = document.getElementById("try")

    button_try.addEventListener("click", function() {
        window.location.href = "/";
    });
  
