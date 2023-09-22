//ticket close
    $('.card-link.close-btn').click(function(){
    var tid = $(this).attr("data-tid");
    $.ajax(
    {
     type:"GET",
        url: "/close/" +tid,
        data:{
                 ticket_id: tid
        },
        success: function( data )
        {
            $('#status'+tid).text(data);
        }
    })
    });
//raise priority
    $('.card-link.raise-btn').click(function(){
    var tid = $(this).attr("data-tid");
    $.ajax(
    {
     type:"GET",
        url: "/raise/" +tid,
        data:{
                 ticket_id: tid
        },
        success: function( data )
        {
            $('#priority'+tid).text(data);
        }
    })
    });

//lower priority
    $('.card-link.lower-btn').click(function(){
    var tid = $(this).attr("data-tid");
    $.ajax(
    {
     type:"GET",
        url: "/lower/" +tid,
        data:{
                 ticket_id: tid
        },
        success: function( data )
        {
            $('#priority'+tid).text(data);
        }
    })
    });

//Show ticket
    $('.card-title').click(function(){
    var tid = $(this).attr("data-tid");
    $.ajax(
    {
     type:"GET",
        url: "/detail/" +tid,
        data:{
                 ticket_id: tid
        },
        success: function( data )
        {alert(text(data));
            $('.detail').text(data);
        }
    })
    });

