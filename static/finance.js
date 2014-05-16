function show_split(string) {
	$('#dimmer').show();
	var body = $('body').css('width');
	body = body.replace('px', '');
	body = parseInt(body);
	var div = $(string).css('width');
	div = div.replace('px', '');
	div = parseInt(div);
	var left = body/2 - div/2;
	$(string).css('left', left)
	$(string).show();
	window.is_dim = true
}

function hide_split() {
	$('#dimmer').hide();
	$('.split_up_div').hide();	
	window.is_dim = false
}

function ta_to_table() {
  $('#id_split_up').hide();
  $('#request_div').append('<br><table class="table table-striped table-bordered table-condensed" id="split_table"><tr><th>Item</th><th>Amount</th></tr><tr><td contenteditable></td><td contenteditable></td></tr></table>');
  $('#request_div').append('<h5 style="margin:0px;margin-bottom:10px;text-align:center"><a href="#" onclick="add_row()">+Add Row</a></h5>');
}

function add_row() {
  $('#split_table').append('<tr><td contenteditable></td><td contenteditable></td></tr>');
}

function table_to_ta() {
  data=$('#split_table').prop('innerHTML');
  data=data.replace(/contenteditable=""/g,'');
  data='<table class="table table-striped table-bordered table-condensed table-hover">'+data+'</table>';
  data=data.replace(/&nbsp;/g,'').replace(/  /g,'').replace(/\<td \> \<\/td\>/g,'').replace(/\<tr\>\<td \>\<\/td\>\<td \>\<\/td\>\<\/tr\>/g,'');
  $('#id_split_up').val(data);
  return true;
}

$(document).keyup(function(e) {
  if (e.keyCode == 27 && is_dim == true) hide_split() 
});

$(document).ready(function() {
  	if(typeof(is_bill) != "undefined" && is_bill !== null) {
    	$('#id_date_month').css('width',120);
    	$('#id_date_day').css('width',70);
    	$('#id_date_year').css('width',80);
	}  
});