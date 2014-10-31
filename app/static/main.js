function add_to_cart(id){
    $.post('/add_to_cart', {id: id, from:window.location.toString()});
    //getElementById("number_of_items").innerHTML = + innerHTML + 1;
};
function proceed_to_item(id){
    document.location.href = "/product="+id;
};

function to_page(id){
    document.location.href = "/catalog="+id;
};

function remove_from_cart(id){
    $.post('/remove_from_cart', {id: id});
};