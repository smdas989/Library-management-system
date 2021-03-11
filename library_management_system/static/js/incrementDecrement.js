
$("#increment").click(function(e) {
e.preventDefault();
    $.ajax({
        method:'POST',
        url: '/increment_book/',
        data: { 
            id: templateVariable.id,
            csrfmiddlewaretoken: templateVariable.csrf_token,
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
        url: '/decrement_book/',
        data: { 
            id: templateVariable.id,
            csrfmiddlewaretoken:templateVariable.csrf_token,
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
