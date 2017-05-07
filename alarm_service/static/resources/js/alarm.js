function getEmailLink(email) {
    return '<a href="mailto:'+email+'">'+email+'</a>';
}

// function to protect against cross site scripting by escaping html entities
function htmlEntities(str) {
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}

function ecblockui() {

    $.blockUI({ message: '', baseZ: 2000});
    $.fancybox.showLoading();

}

function ecunblockui() {

    $.unblockUI();
    $.fancybox.hideLoading();

}

function setCheckbox(checkboxId, value) {

     if(value) {
        $(checkboxId).prop('checked', true);
     }

     else {
        $(checkboxId).prop('checked', false);
     }

}

// function to retrieve any parameter directly from URL, simply call function and specify parameter name you wish to retrieve.
function getURLParameter(sParam){

	var sPageURL = window.location.search.substring(1);
	var sURLVariables = sPageURL.split('&');

	for(var i = 0; i < sURLVariables.length; i++){

		var sParameterName = sURLVariables[i].split('=');

		if(sParameterName[0] == sParam){

			return sParameterName[1];
		}
	}
}
