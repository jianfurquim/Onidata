document.addEventListener('DOMContentLoaded', function() {
    let token = localStorage.getItem('token');

    if (token) {
        console.log("estou na home");
    } else {
        window.location.href = '/login/';
    }
});
