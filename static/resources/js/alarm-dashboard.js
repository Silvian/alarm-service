$(document).ready(function() {

    // get the alarm status first to set the toggle switch.
    getAlarmStatus();

    $('#alarm-switch').change(function() {
        var alarm_status = 0;

        if(this.checked) {
            alarm_status = 1;
            //$(this).prop("checked", true);
        }
        else {
            alarm_status = 0;
            //$(this).prop("checked", false);
        }

        setAlarmStatus(alarm_status);

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

                var alarm_val = data[0].fields.alarm_status;

                if(alarm_val == 1) {
                    toggleOn();
                }
                else {
                    toggleOff();
                }
            }

        }
    });

}

function setAlarmStatus(alarm_status) {

    /* Send the data using post */
    var posting = $.post( '/alarm/config/status/update/', {
                      alarm_name             : $("#alarm-switch").attr("name"),
                      alarm_status           : alarm_status,
                      client_connected_state : $("#client-state").attr("name"),
                      csrfmiddlewaretoken    : getCookie('csrftoken')
    });

    /* Alerts the results */
    posting.done(function(data) {
        if(data.success) {
        }

    });

}

function toggleOn() {
    $('#alarm-switch').bootstrapToggle('on');
}
function toggleOff() {
    $('#alarm-switch').bootstrapToggle('off');
}

function getClientStatus() {



}

