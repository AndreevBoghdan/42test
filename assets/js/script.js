jQuery(function() {
    var options = {
        beforeSubmit: function(form, options) {
            jQuery("#sendbutton").attr('disabled', true);
            $('textarea').attr('disabled', 'disabled');
            $('input').attr('disabled', 'disabled');
            $("#loading").show();      
        },
        success: function(responseText) {
            $(".error").remove()
            jQuery("#sendbutton").attr('disabled', false);
            $('textarea').removeAttr('disabled');
            $('input').removeAttr('disabled');
            $('#loading').hide();
            $("#fail").hide();
            if (responseText == 'OK'){
                    $("#success").show();
                    setTimeout(function () {
                    $("#success").hide();
                    }, 5000);
                }
            },
        error:  function(resp){
                $(".error").remove()
                var errors = JSON.parse(resp.responseText);
                for (error in errors) {
                    id="#id_"+error;
                    $(id).after("<p class='error'>"+errors[error]+"</p>");                   
                }
                $("#success").hide();
                $('#loading').hide();
                $("#fail").show();
                jQuery("#sendbutton").attr('disabled', false);
                $('textarea').removeAttr('disabled');
                $('input').removeAttr('disabled');
            },


        };
    
    jQuery('#ajaxform').ajaxForm(options);

});

function readURL() {
        var input = this;
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $(".image").attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);}}

    $(function () {
        $("#id_photo").change(readURL)})

$(document).ready(function () {

$("textarea").attr('rows', '8');
$("textarea").attr('cols', '30');
$('#ui-datepicker-div').hide();

});
