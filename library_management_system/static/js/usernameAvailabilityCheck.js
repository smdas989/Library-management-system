$("#id_username").keyup(function(){
  var username=$(this).val();
  if(username!=""){
    $.ajax({
      url:"/validate_username",
      type:'GET',
      data:{username:username},
    })
    .done(function(response){
      if(response=="True"){
        $(".username_error").remove();
        $("<span class='username_error' style='font-family: Arial Unicode MS, Lucida Grande; color:red; font-size:13px'> &#10060; Not available</span>").insertAfter("#id_username");
}
      else{
        $(".username_error").remove();
        $("<span class='username_error' style='font-family: Arial Unicode MS, Lucida Grande; color:green; font-size:15px'> &#10004; Available</span>").insertAfter("#id_username");
}
    })
    .fail(function(){
      console.log("failed");
    })
  }
  else{
    $(".username_error").remove();
  }
});
