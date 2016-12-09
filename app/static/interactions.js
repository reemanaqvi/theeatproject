

function initAutocomplete() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.8, lng: -122.2},
    zoom: 14,
    mapTypeId: 'roadmap'
  });

  // Create the search box and link it to the UI element.
  var input = document.getElementById('pac-input');
  var searchBox = new google.maps.places.SearchBox(input);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

  // Bias the SearchBox results towards current map's viewport.
  map.addListener('bounds_changed', function() {
    searchBox.setBounds(map.getBounds());
  });

  var markers = [];
  var locations = [];


  $.ajax({
    type: "POST",
    url: "/get_lat_lng",
    // data: { data:
    //   JSON.stringify({
    //     "title": food_name,
    //     "lat": lat,
    //     "lng": lng,
    //   })
    // },
    success: function(locations) {
            console.log('meow')
            console.log(locations);
            console.log('meow')
            console.log(locations.response)
            var largeInfowindow = new google.maps.InfoWindow();
                    // var bounds = new google.maps.LatLngBounds();

                    // The following group uses the location array to create an array of markers on initialize.
                    for (var i = 0; i < locations.response.length; i++) {
                      // Get the position from the location array.
                      var position_lat = locations.response[i].lat;
                      var position_lng = locations.response[i].lng;

                      position = {}
                  		position['lat'] = position_lat
                  		position['lng'] = position_lng
                      console.log(position)
                      // {lat: 40.7281777, lng: -73.984377}

                      var title = locations.response[i].food_name;
                      console.log(position)
                      console.log(title)
                      // Create a marker per location, and put into markers array.
                      var marker = new google.maps.Marker({
                        map: map,
                        icon: 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
                        position: position,
                        title: title,
                        animation: google.maps.Animation.DROP,
                        id: i
                      });
                      // Push the marker to our array of markers.
                      markers.push(marker);
                      // Create an onclick event to open an infowindow at each marker.
                      marker.addListener('click', function() {
                        populateInfoWindow(this, largeInfowindow);
                      });
                      // bounds.extend(markers[i].position);
                    }
         }
   // do something
  });

//   $(document).on('click', 'button.remove_tr', function() {
//   console.log("hello")
//    var food_id = $(this).attr("id");
//    console.log(food_id)
//    $.ajax({
//      url: "/delete_food",
//      type: "post",
//      data: { data:
//        JSON.stringify({
//          "value": food_id,
//        })
//      },
//      success: function(response) {
//          response
//      }
//    });
//
//    $(this).parent().parent().remove();
//
//    // retrieve user input
//    // var user_input = $('#search-field').val();
//    // callAPI(user_input)
// })

  // for (var i = 0; i < query.length; i++){
  //   console.log(i[food_name]);
  //   // locations.append[{title: i[food_name], location:{i[lat], i[lng]}}];
  //   console.log(locations);
  // }


  // var locations = [
  //           {title: 'Food', price: '$8', location: {lat: 40.7444883, lng: -73.9949465}},
  //           {title: 'Street Food', price: '$8', location: {lat: 40.7281777, lng: -73.984377}},
  //           {title: 'Subway Food', price: '$8', location: {lat: 40.7195264, lng: -74.0089934}},
  //           {title: 'Pad Thai', price: '$8', location: {lat: 37.879594, lng: -122.268935}},
  //           {title: "Parv's Chicken", price: '$8',location: {lat: 37.849533, lng: -122.25196}},
  //           {title: "Mr. Bang's Surprise", price: '$8', location: {lat: 37.87149, lng: -122.275496}},
  //           {title: "Carlo's Street Spam",  price: '$8', location: {lat: 37.869797, lng: -122.267582}},
  //           {title: 'Pizza', price: '$8', location: {lat: 37.855387, lng: -122.263179}},
  //           {title: 'Burritos', price: '$8', location: {lat: 37.849274, lng: -122.271633}},
  //           {title: 'Chaat', price: '$8', location: {lat: 37.873575, lng: -122.25442}},
  //           {title: 'Mediterranean', price: '$8', location: {lat: 37.861346, lng: -122.250266}}
  //           ];




  // var locations = [
  //         {title: 'Food', location: {lat: 37.8744883, lng: -122.2749465}},
  //         {title: 'East Village Hip Studio', location: {lat: 37.8781777, lng: -122.2677}},
  //         {title: 'TriBeCa Artsy Bachelor Pad', location: {lat: 37.8695264, lng: -122.2789934}}
  //         ];
  // 
  // var largeInfowindow = new google.maps.InfoWindow();
  //         // var bounds = new google.maps.LatLngBounds();
  //
  //         // The following group uses the location array to create an array of markers on initialize.
  //         for (var i = 0; i < locations.length; i++) {
  //           // Get the position from the location array.
  //           var position = locations[i].location;
  //           var title = locations[i].title;
  //           // Create a marker per location, and put into markers array.
  //           var marker = new google.maps.Marker({
  //             map: map,
  //             icon: 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png',
  //             position: position,
  //             title: title,
  //             animation: google.maps.Animation.DROP,
  //             id: i
  //           });
  //           // Push the marker to our array of markers.
  //           markers.push(marker);
  //           // Create an onclick event to open an infowindow at each marker.
  //           marker.addListener('click', function() {
  //             populateInfoWindow(this, largeInfowindow);
  //           });
  //           // bounds.extend(markers[i].position);
  //         }
  // Listen for the event fired when the user selects a prediction and retrieve more details for that place.
  searchBox.addListener('places_changed', function() {
    var places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }

    // Clear out the old markers.
    // markers.forEach(function(marker) {
    //   marker.setMap(null);
    // });
    // markers = [];

    // For each place, get the icon, name and location.
    var bounds = new google.maps.LatLngBounds();
    places.forEach(function(place) {
      if (!place.geometry) {
        console.log("Returned place contains no geometry");
        return;
      }
      var icon = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25)
      };

      // Create a marker for each place.
      markers.push(new google.maps.Marker({
        map: map,
        icon: icon,
        title: place.name,
      }));

      if (place.geometry.viewport) {
        // Only geocodes have viewport.
        bounds.union(place.geometry.viewport);
      } else {
        bounds.extend(place.geometry.location);
      }
    });
    map.fitBounds(bounds);
  });
}

function populateInfoWindow(marker, infowindow) {
        // Check to make sure the infowindow is not already opened on this marker.
        if (infowindow.marker != marker) {
          infowindow.marker = marker;
          infowindow.setContent('<div>' + marker.title + '</div>');
          infowindow.open(map, marker);
          // Make sure the marker property is cleared if the infowindow is closed.
          infowindow.addListener('closeclick',function(){
            infowindow.setMarker(null);
          });
        }
      }

  $(document).on('click', 'button.remove_tr', function() {
      // console.log($(this).attr("id"));
      $.ajax({
        url: "/delete_food",
        type: "post",
        data: { data:
          JSON.stringify({
            "value": $(this).attr("food_id")
          })
        },
        success: function(response) {
            response
        }
      });

      $(this).parent().parent().remove();

      // retrieve user input
      // var user_input = $('#search-field').val();
      // callAPI(user_input)
  })


  $(document).on('click', 'button.remove_tr', function() {
	console.log("hello")
   var food_id = $(this).attr("id");
   console.log(food_id)
   $.ajax({
     url: "/delete_food",
     type: "post",
     data: { data:
       JSON.stringify({
         "value": food_id,
       })
     },
     success: function(response) {
         response
     }
   });

   $(this).parent().parent().remove();

   // retrieve user input
   // var user_input = $('#search-field').val();
   // callAPI(user_input)
})





function myFunction() {
  // Declare variables
  var input, filter, table, tr, td, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("food-offering");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

// GEOCODER ON ADD_ITEM PAGE
var geocoder;
var map;

  function initMap() {
    console.log("in initMap()");
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(-34.397, 150.644);
    var myOptions = {
      zoom: 8,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
  }

  function codeAddress() {
    console.log("in codeAddress()");
    var address = document.getElementById("address").value;
    var loc=[];
    var latlng = [];

    geocoder.geocode( { 'address': address}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        loc[0] = results[0].geometry.location.lat();
        loc[1] = results[0].geometry.location.lng();
        console.log("went in if in codeAddress");
        var lat = loc[0];
        var lng = loc[1];
        console.log(lat);
        console.log(lng);
        document.getElementById('lat').value = lat;
        document.getElementById('lng').value = lng;
        // return (coordinates);

      } else {
        alert("Geocode was not successful for the following reason: " + status);
        console.log("went in else in codeAddress");
      }
    });
  }
