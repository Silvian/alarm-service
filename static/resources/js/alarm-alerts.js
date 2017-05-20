$(document).ready(function() {

    $('#alerts-empty').hide();
    $('#alerts tbody').html("");

    $.ajax({
        type: 'GET',
        url: '/alarm/alerts/latest/',
        dataType: 'json',
        success: function (data) {
            if(data && data.length > 0) {
                $('#users-list tbody').html("");

                $.each(data, function(i, item) {
                    var alert = item.fields;
                    $('#alerts tbody').append('<tr>' +
                        '<td>' + getFormattedDateAndTime(new Date (htmlEntities(alert.time))) + '</td>' +
                        '<td>' + htmlEntities(alert.type) + '</td>' +
                        '<td>' + htmlEntities(alert.sent) + '</td>' +
                        '<td>' + htmlEntities(alert.remaining) + '</td>' +
                    '</tr>');
                });

            }

            else {
                $('#alerts-empty').show();
            }

        }
    });

});