
function like(pk) {



	

 var xhttp = new XMLHttpRequest();
 xhttp.open("GET", `/like/${pk}/`, true);
 xhttp.send();

	$('#likes').text(parseInt($('#likes').text())+1);
	
	$("#bntunlike").off('click');



}


function deslike(pk) {



	

 var xhttp = new XMLHttpRequest();
 xhttp.open("GET", `/deslike/${pk}/`, true);
 xhttp.send();

	$('#unlike').text(parseInt($('#unlike').text())+1);
	$('#unlike').attr("disabled", true);
	$('#bntunlike').off('click');




}