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

function new_installment(adv_id) {
	hide_split();
	show_split('#new_ins_form');
	$('#request_div_ins').append('<input type="hidden" name="adv_id" id="adv_identifier" value="'+adv_id+'">')
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

function content_splitter(string) {
	$('.content_divs').hide();
	$(string).show();
}

$(document).keyup(function(e) {
  if (e.keyCode == 27 && is_dim == true) hide_split() 
});

$(document).ready(function() {
    	$('[name*="date_month"]').each(function() {
			$(this).css('width',120);
		});
    	$('[name*="date_day"]').each(function() {
			$(this).css('width',70);
		});
    	$('[name*="date_year"]').each(function() {
			$(this).css('width',80);
		});
    	$('[name*="is_app"]').each(function() {
			$(this).css('width',120);
		});
		$('[name*="comments"]').each(function() {
			$(this).css('width',300);
		});
		$('[type="number"]').each(function() {
			$(this).css('padding',0);
		});
		$('.data_tables').each( function() {
			a=$(this).find('tr').length;
			if(a==1) {
				$(this).parent().prepend('<h4 class="no_data_h4" style="text-align:center">No entries</h4>');
				$(this).parent().children().hide();
				$('.no_data_h4').show();
			}
		});

		$('.content_divs').hide();
		$('.first_con_div').show();
});