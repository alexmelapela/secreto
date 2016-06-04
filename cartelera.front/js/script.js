
$.get( _BASE_URL +  "/films/", function( data ) {
    $('body').append( data );
  console.log(data)
});