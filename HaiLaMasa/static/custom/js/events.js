 var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
       }
    });
$(".dropdown-menu a").click(function() {

  var menu_pk = $(this).context.dataset.pk;
  var send_data = {
    "pk_menu" : menu_pk
  };

  $.get( window.location.href+"/menu/",send_data, function( data ) {
      var menu = JSON.parse(data);
      $("#menu_name").val(menu.name);
      $("#menu_description").val(menu.description);
      $("#menu_date").val(menu.date);
      $("#menu_price").val(menu.price);
      $("#selected_menu").val(menu_pk);

  });
});

$(".xremove").click(function() {

  var formData = new FormData();
  formData.append('pk', $(this).context.dataset.pk);
   $.ajax({
       url : window.location.href+'/delete',
       type : 'POST',
       data : formData,
       processData: false,  // tell jQuery not to process the data
       contentType: false,  // tell jQuery not to set contentType
       success : function(data) {
          
       }
    });
  console.log($(this).parent().hide());
});

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
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
$("#picture").change(function() {
    var formData = new FormData();
    formData.append('file', $(this).context.files[0]);



    $.ajax({
       url : window.location.href+'/upload',
       type : 'POST',
       data : formData,
       processData: false,  // tell jQuery not to process the data
       contentType: false,  // tell jQuery not to set contentType
       success : function(data) {
           location.reload()
       }
    });


});