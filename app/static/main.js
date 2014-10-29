function add_to_cart(id){
    $.post('/add_to_cart', {id: id, from:window.location.toString()});
}