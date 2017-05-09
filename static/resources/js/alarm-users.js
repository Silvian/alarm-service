$(document).ready(function(){

    $('#users-error').hide();

    getUsers();

    $('#add-user-button').click(function() {
        clearUserFields();
        $('#user-modal-label').html("Add a new user");
        $('#required-fields-alert').hide();
        $('#user-modal').modal('show');
    });

    $('#save-user').click(function() {
        saveUser();
    });

    $('#users-list').on("click", '[id^="view-"]', function() {
        var id = this.id.split('view-');
        editUser(id[1]);
    });

    $('#users-list').on("click", '[id^="remove-"]', function() {
        var id = this.id.split('remove-');
        $('#delete-id').val(id[1]);
        $('#delete-modal-label').html("Delete user?");
        $('#delete-modal').modal('show');
    });

    $('#delete-confirm').click(function() {
        deleteUser($('#delete-id').val());
    });

});


function getUsers() {

    ecblockui();
    $('#users-empty').hide();
    $('#users-list tbody').html("");

    $.ajax({
        type: 'GET',
        url: '/alarm/users/all/',
        dataType: 'json',
        success: function (data) {
            ecunblockui();
            if(data && data.length > 0) {
                $('#users-list tbody').html("");

                $.each(data, function(i, item) {
                    var user = item.fields;
                    $('#users-list tbody').append('<tr>' +
                        '<td><a id="view-'+ htmlEntities(item.pk) +'" href="#">' + htmlEntities(user.name) + '</a></td>' +
                        '<td>' + getEmailLink(htmlEntities(user.email)) + '</td>' +
                        '<td>' + htmlEntities(user.mobile) + '</td>' +
                        '<td><button type="button" class="btn btn-danger btn-sm" id="remove-'+ htmlEntities(item.pk) +'"><i class="fa fa-trash fa-fw"></i></td>' +
                    '</tr>');
                });

            }

            else {
                $('#users-empty').show();
            }

        }
    });

}


function saveUser() {

    $('#required-fields-alert').hide();

    if($('#user-name').val()!="" &&
       $('#user-email').val()!="" &&
       $('#user-mobile').val()!="") {

        var id = null;
        if($('#user-id').val()!="") {
            id = $('#user-id').val();
            url = '/alarm/users/update/';
        }
        else {
            url = '/alarm/users/add/';
        }

        ecblockui();
        $.ajax({
            type: 'POST',
            url: url,
            dataType: 'json',
            data: {    id : id,
                       name : $('#user-name').val(),
                       email : $('#user-email').val(),
                       mobile : $('#user-mobile').val(),
                       csrfmiddlewaretoken : getCookie('csrftoken')
                    },
            success: function (data) {
                ecunblockui();
                $("#user-modal").modal('hide');
                getUsers();
            }
        });

    }

    else {
       $('#required-fields-alert').show();
    }

}


function editUser(id) {

    clearUserFields();
    $('#user-modal-label').html("Edit User");
    $('#user-modal').modal('show');
    ecblockui();
    $.ajax({
        type: 'GET',
        url: '/alarm/users/get/',
        dataType: 'json',
        data: { id : id },
        success: function (data) {
            ecunblockui();
            var user = data[0];
            $('#user-id').val(user.pk);
            $('#user-name').val(user.fields.name);
            $('#user-email').val(user.fields.email);
            $('#user-mobile').val(user.fields.mobile);
        }
    });

}


function deleteUser(id) {

    $('#delete-modal').modal('hide');

    ecblockui();
    $.ajax({
        type: 'POST',
        url: '/alarm/users/delete/',
        dataType: 'json',
        data: {    id : id,
                   csrfmiddlewaretoken : getCookie('csrftoken')
                },
        success: function (data) {
            ecunblockui();
            if(data.success) {
                getUsers();
            }
            else {
                $('#error-msg').html(data.error);
                $('#users-error').show();
                setTimeout(function () {
                    $('#users-error').hide();
                }, 3000);
            }
        }
    });

}

function clearUserFields() {

    $('#user-id').val("");
    $('#user-name').val("");
    $('#user-email').val("");
    $('#user-mobile').val("");

}