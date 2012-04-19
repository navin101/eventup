function setTime(which){

    var currentTime = new Date();
    var hours = currentTime.getHours();
    var minutes = currentTime.getMinutes();

    // set hour
    var id = "#hour_" + which;
    $(id).val(hours);
    $(id).selectmenu('refresh', true);

    // set minutes
    var id = "#minute_" + which;
    $(id).val(round5(minutes));
    $(id).selectmenu('refresh', true);
}

function clearTime(which){

    // set hour
    var id = "#hour_" + which;
    $(id).val('x');
    $(id).selectmenu('refresh', true);

    // set minutes
    var id = "#minute_" + which;
    $(id).val('x');
    $(id).selectmenu('refresh', true);

}

function deletePotty(id){
    var id = "#" + id;
    $(id).fadeOut();
}

function round5(x) {
    var num = (x % 5) >= 2.5 ? parseInt(x / 5) * 5 + 5 : parseInt(x / 5) * 5;
    if (num < 10) {
        num = "0" + num;
    }
    return num;
}

function here(el){

    var id = el.id;

    var el = $("#count");
    var count = el.html();
    count++;
    el.html(count);
    
    el = "#" + id + "_grid";
    el = $(el);
    if (el && confirm("Confirm that " +id+ " is here?")){
        el.fadeOut();
    }
    
}