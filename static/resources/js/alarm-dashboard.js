$(document).ready(function() {

    var alarm_status = 0;

    getAlarmStatus();

    if($('#alarm-switch').prop("checked") == true){
        alarm_status = 1;
    }

    $('#alarm-switch').change(function() {

        if(this.checked) {
            alarm_status = 1;
            $(this).prop("checked", alarm_status);
        }
        else {
            alarm_status = 0;
            $(this).prop("checked", alarm_status);
        }

        /* Send the data using post */
        var posting = $.post( '/alarm/config/status/update/', {
                          alarm_name             : $("#alarm-switch").attr("name"),
                          alarm_status           : alarm_status,
                          client_connected_state : $("#client-state").attr("name"),
                          csrfmiddlewaretoken    : getCookie('csrftoken')
        });

        /* Alerts the results */
        posting.done(function( data ) {
            if(data.success) {

            }

        });

    });

});

function getAlarmStatus() {

    $.ajax({
        type: 'GET',
        url: '/alarm/config/status/get/',
        dataType: 'json',
        success: function (data) {
            if(data && data.length > 0) {
                $('#alarm-switch').attr('name', data[0].pk);
                $('#client-state').attr('name', data[0].fields.client_connected_state)
                setCheckbox('#alarm-switch', data[0].fields.alarm_status);
            }

        }
    });

}

function getClientStatus() {



}

