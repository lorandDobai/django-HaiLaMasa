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