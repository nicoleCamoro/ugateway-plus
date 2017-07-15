function upload_to_server(url) {
    $.ajax({
        type: "POST",
        url: "localhost:8080/api/v1/upload",
        data: { 
            imgBase64: url
        }
    }).done(function(o) {
        console.log('saved'); 
    });
};