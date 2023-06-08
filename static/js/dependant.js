$(document).ready(function() {
    $("#country").change(function() {
        var country_id = $(this).val();
        var url = "/depend/get-states/?country_id="+country_id;
        $.get(url, function(data, status){
            $("#state").html(data);
        });
    });
});

$(document).ready(function() {
    $("#state").change(function() {
        var state_id = $(this).val();
        var url = "/depend/get-cities/?state_id="+state_id;
        $.get(url, function(data, status){
            $("#city").html(data);
        });
    });
});

$(document).ready(function() {
    $("#city").change(function() {
        var city_id = $(this).val();
        var url = "/depend/get-business/?city_id="+city_id;
        $.get(url, function(data, status){
            $("#business").html(data);
        });
    });
});

$(document).ready(function() {
    $("#business").change(function() {
        var business_id = $(this).val();
        var url = "/depend/get-packages/?business_id="+business_id;
        $.get(url, function(data, status){
            $("#packages").html(data);
        });
    });
});