//$(document).ready(function() {
//    $("#id_team").on('click', function(e){
//        e.preventDefault();
//        console.log("HI")
//        var csrf = $("input[name='csrfmiddlewaretoken']").val();
//        if ($("#id_team").val() == "") {
//            debugger;
//            $('#id_players').hide();
//        }
//        else {
//              $('#id_players').show();
//            }
//            debugger;
//            {
//            var serializedData = $(this).serialize();
//            $.ajax({
//                url: "/squad/create/",
//                type: "POST",
//                headers: { "X-CSRFToken": csrf },
//                data: serializedData,
//                success: function(data) {
//                console.log("Hello")
//            }
//            })
//        };
//    });
//});

$("#id_team").on('change', function(e){
    e.preventDefault();
    var data = $("#id_team").val()
    if ($("#id_team").val() == "") {
        $("#id_players").hide()
    }
    $.ajax({
            url: "/squad/create/",
            type: "GET",
            data: data,
            success: function(data) {
            console.log("Hello")
        }
    })
});

//function player(){
//    var data = $("#id_team").val()
//    console.log(data)
//}
