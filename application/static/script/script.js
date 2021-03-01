$(function(){
	$(".del_user").click(function(id){
		let url = "/"+this.id;
		$.post(url,this.id,function(data){
			if (data == 307)
				document.location.reload(true);
		});
	}); $(".add_user").click(function(){
		let nome = $("#nome").val();
		let datad = $("#datad").val();
		let url = "/"+nome+"/"+datad;
		$.post(url,{nome,datad},function(data){
			if (data == 307)
				document.location.reload(true);
		});
	});
});