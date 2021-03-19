
$("#increment").click(function(e) {
e.preventDefault();
    $.ajax({
        method:'POST',
        url: '/increment_decrement_book/',
        data: { 
            func:'increment',
            id: templateVariable.id,
            csrfmiddlewaretoken:templateVariable.csrf_token
        },
        success: function(data) {
          
          $("#no_of_copies").html( data.no_of_copies );
          $("#no_of_available_copies").html( data.no_of_available_copies );
            
        },
        error: function(data) {
            alert('error');
        }
    });
});

$("#decrement").click(function(e) {
    e.preventDefault();
    $.ajax({
        method:'POST',
        url: '/increment_decrement_book/',
        data: { 
            func:'decrement',
            id: templateVariable.id,
            csrfmiddlewaretoken:templateVariable.csrf_token

        },
        success: function(data) {
          
          $("#no_of_copies").html( data.no_of_copies );
          $("#no_of_available_copies").html( data.no_of_available_copies );
            
        },
        error: function(data) {
            alert('Total no of books can\'t be negative');
        }
    });
});
