var f_name1 = document.getElementById("f_name1");
var l_name1 = document.getElementById("l_name1");
var dob1 = document.getElementById("dob1");
var resultField1 = document.getElementById("resultField1");
var form = document.getElementById("first_form");

form.addEventListener("submit", function(event) {
	if (!f_name1.value || !l_name1.value || !dob1.value){
		alert("Please enter a value");
	} else {
	 	var x = f_name1.value;
         var y = l_name1.value;
         var z = dob1.value;
	// 	var result = x / y;
	// 	var percent = result * 100;
		resultField1.innerHTML =  x + " " + " " + y + " " + " " + z;
		event.preventDefault();
	}
});