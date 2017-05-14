$(document).ready(function(){

    //enable the powerful data table sorting, pagination and searching controls
    var logs_table = $('#logs-list').DataTable({
    'ajax': {
        "type"   : "GET",
        "url"    : '/alarm/logs/get/today/',

        "dataSrc": ""
    },
        'columns': [
            {"mRender": function(data, type, row) {
                            return getFormattedDateAndTime(new Date(htmlEntities(row.fields.time_stamp)));
                        }
            },
            {"mRender": function(data, type, row) {
                            return doorState(htmlEntities(row.fields.door_state));
                        }
            },
            {"mRender": function(data, type, row) {
                            return alarmState(htmlEntities(row.fields.alarm_state));
                        }
            },
            {"mRender": function(data, type, row) {
                            return clientState(htmlEntities(row.fields.client_state));
                        }
            },

        ],

    });

    $('#select-date').datepicker()
        .on('changeDate', function(calendar){
            $('#select-date').datepicker('hide');

            if(calendar.date.valueOf() != "") {
                date = calendar.date.valueOf();
                date = moment(date).format('YYYY-MM-DD');
                var logs_url = '/alarm/logs/get?date='+date;
                logs_table.ajax.url(logs_url).load();
            }

    });

});