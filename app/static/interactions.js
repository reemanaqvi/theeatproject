///JAVASCRIPTTT


// $(document).on('click', '.delete', function () {
// 		// $(this.parentNode.parentNode).remove();
// 		trip_name = $(this).parent().prev().prev().text();
// 		destination = $(this).parent().prev().text();
// 		// alert(destination);
// 		$(this).parent().parent().remove();
// 		$.post("http://0.0.0.0:8081/delete_trip",
// 			{
// 			trip_name: trip_name,
// 			destination: destination
// 			},
// 			function(data) {
// 				if (data == "ok") {
//                    alert("Trip deleted.")
//               } else {
//                    alert("dick.")
//               }
//               }
// 		);
// 	});

$(document).on('click', '.delete', function() {
	console.log("hello")
   console.log($(this).attr("id"));
	//  console.log($(this).attr("trip_name"));
	//  console.log($(this).attr("destination"));
   $.ajax({
     url: "/delete_trip",
     type: "post",
     data: { data:
       JSON.stringify({
         "value": $(this).attr("id")
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
