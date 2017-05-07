$(document).ready(function(){

    $('#users-error').hide();

    getUsers();

    $('#add-user-button').click(function() {
        clearUserFields();
        $('#user-modal-label').html("Add a new user");
        $('#required-fields-alert').hide();
        $('#user-modal').modal('show');
    });

});


function getUsers() {



}

function clearUserFields() {

    $('#user-name').val("");
    $('#user-email').val("");
    $('#user-mobile').val("");

}