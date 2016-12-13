function init() {
	window.setInterval(function(){
	  /// call your function here
	  get_count().then(function(result) {
	  	update_counter(result);
	  }, function(err) {
	  	console.log(err);
	  })
	}, 1000);
}

function get_count() {
	return new Promise(function(resolve, reject) {
		$.ajax({
			type: "GET",
			url: '/get_count',
			success: function(data) {
				// console.log(data);
				resolve(data["result"]["count"]);
			},
			error: function(err) {
				reject(err);
			} // TODO: Reject
		});
	})
}

function increment() {
	$.ajax({
	  type: "POST",
	  url: '/increment',
	  success: function(data) {
	  	// update_counter(data["result"]["count"]);
	  }
	});
}

function decrement() {
	$.ajax({
	  type: "POST",
	  url: '/decrement',
	  success: function(data) {
	  	// update_counter(data["result"]["count"]);
	  }
	});
}

function update_counter(count) {
	// console.log($("#counter").html());
	$("#counter").text(count.toString());
}