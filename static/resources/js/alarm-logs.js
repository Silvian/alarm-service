$(document).ready(function(){

    //enable the powerful data table sorting, pagination and searching controls
    var logs_table = $('#logs-list').DataTable({
    'ajax': {
        "type"   : "GET",
        "url"    : '/api/log/',

        "dataSrc": ""
    },
        'columns': [
            {"mRender": function(data, type, row) {
                            return getFormattedDate(new Date(htmlEntities(row.time_stamp)));
                        }
            },
            {"mRender": function(data, type, row) {
                            return doorState(htmlEntities(row.door_state));
                        }
            },
            {"mRender": function(data, type, row) {
                            return alarmState(htmlEntities(row.alarm_state));
                        }
            },
            {"mRender": function(data, type, row) {
                            return clientState(htmlEntities(row.client_state));
                        }
            },

        ],

    });

});