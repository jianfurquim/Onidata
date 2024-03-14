$(document).ready(function() {
    $('#login-form').submit(function(event) {
        event.preventDefault();
        let formData = {
            'username': $('#username').val(),
            'password': $('#password').val()
        };
        $.ajax({
            type: 'POST',
            url: '/token/',
            data: formData,
            success: function(response) {
                localStorage.setItem('token', response.access);
                window.location.href = '/home/';
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseJSON.error);
            }
        });
    });
});