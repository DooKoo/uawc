function add_to_cart(id){
    $.post('/add_to_cart', {id: id, from:window.location.toString()});
    $.post('/in_cart').done(function(num){$('span.number_of_items').text(num)});
};

function proceed_to_item(id){
    document.location.href = "/product="+id;
};

function to_page(id){
    document.location.href = "/catalog="+id;
};

function remove_from_cart(id){
    $.get('/remove_from_cart/id='+id);
};