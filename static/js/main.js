function gmailAuthenticate(){
    $.ajax({
        type: "GET",
        url: "ajax/gmailAuthenticate",
        // data: '',
        success: function (data) {
            console.log('Done')
        }
    });
};