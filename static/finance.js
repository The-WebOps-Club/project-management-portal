function show_split(string) {
	$('#dimmer').show();
	$(string).show();
}

function hide_split() {
	$('#dimmer').hide();
	$('.split_up_div').hide();	
}

function ta_to_table() {
  $('#id_split_up').hide();
  $('#request_div').append('<br><table class="table table-striped table-bordered table-condensed" id="split_table"><tr><th>Item</th><th>Amount</th></tr><tr><td contenteditable></td><td contenteditable></td></tr></table>');
  $('#request_div').append('<h5><a href="#" onclick="add_row()">+Add Row</a></h5>');
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