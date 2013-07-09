$('#newAddressForm').submit(function() {
    $.ajax({
        data: $(this).serialize(),
        type: $(this).attr('method'),
        url: $(this).attr('action'),
        dataType: 'json',
        success: function(data) {
            results = data;
            $('#results').empty();
            if (results.length == 0) {
                $('#results').append('None Found');
            } else {
                $('#results').append('<div>' + results[0] + '</div>'); 
                //for (var i = 0; i < results.length; i++ ) {
                //    $('#results').append('<div>' + results[i][0] + 
                //    ' ' +
                //    results[i][1] +
                //    ' ' +
                //    results[i][2] +
                //    '</div>');
                //}
            }
        }
    });
    return false;
});
