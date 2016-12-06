// This example adds a search box to a map, using the Google Place Autocomplete
// feature. People can enter geographical searches. The search box will return a
// pick list containing a mix of places and predicted search terms.

// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">


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

  var locations = [
            {title: 'Chelsea Loft', location: {lat: 40.7444883, lng: -73.9949465}},
            {title: 'East Village Hip Studio', location: {lat: 40.7281777, lng: -73.984377}},
            {title: 'TriBeCa Artsy Bachelor Pad', location: {lat: 40.7195264, lng: -74.0089934}}
            ];

  var largeInfowindow = new google.maps.InfoWindow();
          // var bounds = new google.maps.LatLngBounds();

          // The following group uses the location array to create an array of markers on initialize.
          for (var i = 0; i < locations.length; i++) {
            // Get the position from the location array.
            var position = locations[i].location;
            var title = locations[i].title;
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
        position: place.geometry.location
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
        url: "/delete_trip",
        type: "post",
        data: { data:
          JSON.stringify({
            "id": $(this).attr("id")
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
