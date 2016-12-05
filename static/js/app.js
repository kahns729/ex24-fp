function increment() {
	$.ajax({
	  type: "POST",
	  url: '/increment',
	  success: function() {
	  	location.reload();
	  }
	});
}

function decrement() {
	$.ajax({
	  type: "POST",
	  url: '/decrement',
	  success: function() {
	  	location.reload();
	  }
	});
}