function add_to_cart(id){
    $.post('/add_to_cart', {id: id, from:window.location.toString()});
    //getElementById("number_of_items").innerHTML = + innerHTML + 1;
};

function remove_from_cart(id){
    $.post('/remove_from_cart', {id: id});
};