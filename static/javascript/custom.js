$(document).ready(function(){
	$('#menu .menuCollapse').on('show.bs.collapse', function()
	{
		$(this).parents('.hasSubmenu:first').addClass('active');
	})
	.on('hidden.bs.collapse', function()
	{
		$(this).parents('.hasSubmenu:first').removeClass('active');
	});

	$('.preview').popover({
		'trigger':'hover',
		'html':true,
		'content':function(){
			return $(this).find('p').html();
		}
	});

});

function serializeJSON( a ){
	b = {}
	for(var x=0;x<a.length;x++){
		b[a['name']] = a['value']
	}
	return b
}
$.fn.serializeObject = function()
{
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};