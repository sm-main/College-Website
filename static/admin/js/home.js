$(document).ready(function(){
	//Defining pop and shift functions...................................
	(function( $ ) {
    $.fn.pop = function() {
        var top = this.get(-1);
        this.splice(this.length-1,1);
        return top;
    };

    $.fn.shift = function() {
        var bottom = this.get(0);
        this.splice(0,1);
        return bottom;
    };
})( jQuery );
    // Header background image change......................................
	var header=$("#head_box");
	var classes=["bg1","bg2"];
	var index=0;
	var num=0;
	function nextBg()
	{
		if(index==0)
		{
			header.addClass(classes[0]);
			header.removeClass(classes[1]);
			index=1;
		}
		else
		{
			header.addClass(classes[1]);
			header.removeClass(classes[0]);
			index=0;
		}
		
	};	
	setInterval(nextBg,5000);
	// Toggling Vission and mission on header of home page............................
	function hideH2()
	{
		$("#vis").toggle(500);
			//$("#mis").removeClass("hide");
	    $("#mis").toggle(500);
	};
	// Department area viewport stuff ................................................
	$('.viewport').mouseenter(function(e) {
        $(this).children('a').children('img').animate({
            height: '299', left: '0', top: '0', width: '450'}, 100);
            $(this).children('a').children('span').fadeIn(200);
        }).mouseleave(function(e) {
        $(this).children('a').children('img').animate({ height: '332', left: '-20', top: '-20', width: '500'}, 100);
        $(this).children('a').children('span').fadeOut(200);
    });
	setInterval(hideH2,5000);
	// Notice manager clicking next will show next notice.................................
	$("#show_next").click(function(eve)
	{

		var top3=$("#nav2 li:lt(3)");
		var bottom3=$("#nav2 li:lt(6)").slice(3);
		eve.preventDefault();
		top3.toggle(300);
		bottom3.toggle(300);
	});
	
		var show_list=$(".notice_n");
		var hide_list=$(".hide_n");
		var next_butt=$("#next_butt");
		var prev_butt=$("#prev_butt");
		var first_item;
		var last_item;
		next_butt.click(function(eve)
		{
			eve.preventDefault();
			first_item=show_list.shift();
			$(first_item).removeClass('notice_n').addClass('hide_n');
			last_item=hide_list.shift();
			$(last_item).removeClass('hide_n').addClass('notice_n');
		});
		prev_butt.click(function(eve)
		{
			eve.preventDefault();
			$(show_list.last()).removeClass('notice_n').addClass('hide_n');
			$(hide_list.last()).removeClass('hide_n').addClass('notice_n');


		});
		// Mega Menu stuff.................................................
		/*
		var megalia=$('.mega_links a');
		var megamenu=$('.aboutDiv');
		megalia.hover(function(){
			if (megamenu.is(':hidden'))
			{
				megamenu.slideDown();
				megamenu.addClass('afterHover');
			}
		},function(){
			megamenu.fadeOut('slow');
		}); 
		megamenu.mouseleave(function(){
			$(this).fadeOut('slow');
		});
		megamenu.hover(function(){
			megamenu.css('display','block');

		},function(){
			megamenu.fadeOut('slow');
		});*/
        var megalia=$('.mega_links');
        var megamenu=$('.aboutDiv');
        megalia.hover(function(){
        	megamenu.slideDown();
        	//megamenu.addClass('afterHover');


        },function()
        {
        	megamenu.slideUp();
        	//megamenu.removeClass('afterHover');
        });
		// Latest Events Stuff ..............................................
		var eventBox=$(".event_box");
		var eventContent=$("#event_content");
		eventBox.hover(function(){
			eventContent.addClass('event_class');
			eventContent.slideDown();

		},function(){
			eventContent.removeClass('event_class');
			eventContent.fadeOut();
		});
});