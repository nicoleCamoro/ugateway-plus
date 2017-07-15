function upload_to_server(url) {
    $.ajax({
        type: "POST",
        url: "https://ugatewayplus.appspot.com/api/v1/upload",
        data: { 
            imgBase64: url
        }
    }).done(function(o) {
        console.log('saved'); 

    });
};