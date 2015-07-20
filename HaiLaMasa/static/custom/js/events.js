$(".dropdown-menu a").click(function() {

var menu_pk = $(this).context.dataset.pk;
console.log(window.location.href);
$.get( window.location.href+"/menu/"+menu_pk, function( data ) {
  console.log(data);
});
});