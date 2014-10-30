function add_to_cart(id){
    $.post('/add_to_cart', {id: id, from:window.location.toString()} );
}
function proceed_to_checkout(user_id){
    $.post('/checkout', {user_id: user_id}
}
function proceed_to_buy(user_id){
    $.post('/buy', {user_id: user_id}
}