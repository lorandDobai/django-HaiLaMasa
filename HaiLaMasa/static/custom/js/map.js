(function(){
  var myCenter=new google.maps.LatLng(45.6593638,25.6201972);
  console.log('hello');
  function initialize()
  {
  var mapProp = {
    center:new google.maps.LatLng(45.8369377,24.9987621),
    zoom:7,
    maxZoom:8,
    minZoom:6,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    mapTypeControl:false,
    zoomControl:false,
    scrollwheel: false
    };

  var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);

  var marker = new google.maps.Marker({
    position: myCenter,
    title:'brasov'
    });

  marker.setMap(map);

  google.maps.event.addListener(marker,'click',function() {
    //alert(marker.title);
    var str1 = window.location.href+"oras/";
    var str2 = marker.title;
    var res = str1.concat(str2);
    window.location.replace(res);
    //alert("AAA");
    });
  }
  google.maps.event.addDomListener(window, 'load', initialize);
})();