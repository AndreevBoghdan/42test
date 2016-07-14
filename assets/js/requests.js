$(document).ready(function () {  
    
    post=false
    
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

    var csrftoken = getCookie('csrftoken');

    function makeRead() {
        $.ajax({
                url: '/requests/',
                type: "POST",
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                },
                
    
            });
    }
    function renew() {
        $(document).attr('title','0 new request paths')
        makeRead();
    }
    
    function getInfo() {
        var leftHeader =''
        var titleCount = 0;
        var reqList =''
        var date = new Date();

        
        $.ajax({
            url: '/requests/',
            success: function (response) {
                _.each(JSON.parse(response), function (item) {
                        if (!item.fields.is_read) {
                            titleCount+=1
                            newClass='new'
                        } else{
                            newClass=''
                        }   
                            seconds = Date.parse(item.fields.date);
                            date.setTime(seconds);
                            dateFormat(date, "dddd, mmmm dS, yyyy, h:MM:ss TT");
                            reqList=reqList+
                            '<p class="request-simple ' + newClass +'" data-id="' + item.pk + '" id="request-' + 
                            item.pk + '"' +'>' +
                            item.pk + 
                            '. ' + dateFormat(date, "[d/mmm/yyyy, HH:MM:ss] ") + 
                            '"' + item.fields.meth + " " + item.fields.path + '" ' +
                            item.fields.status_code + '</p>'
                         
                        
                });
                if (titleCount !=0){
                        $("p.request-simple").remove()
                        $("#request-count").remove()
                        leftHeader='<h2 id="request-count">You have got '+
                        titleCount+
                        ' new requests: </h2>'
                        $('#right').prepend(leftHeader+reqList);
                        $(document).attr('title', titleCount + ' new request paths')
                        reqList=''
                        }
                
                
            },
        });
        
        
    }
    
    getInfo();
    renew()
    $(window).focus(function () {
                            $(document).attr('title','0 new request paths')
                            post=true
                    }).blur(function () {});

    setInterval(function () {

        
        $(window).focus(function () {
                            post=true
                    }).blur(function () {});
        if (post){
            renew()
            post=false
        }
        setTimeout(function () {
        getInfo();
        }, 100);
        
    }, 1000);
});