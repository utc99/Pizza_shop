//Global variables
let shopping_cart = new Array;
let remove_img = '/static/orders/images/remove4.png';
let counter;
let total_price = 0;
let toppings_limit = 1;
let selected_toppings = new Array;
let last_pick = 'None';

get_cart();

//Get a shopping cart from a session
function get_cart() {
    
    let session_cart = sessionStorage.getItem('Session_cart');
    counter = 0;
    
    if (session_cart !== undefined){
        session_cart = JSON.parse(sessionStorage.getItem('Session_cart'));
        
        if (session_cart != null){
            
            counter = session_cart.length;
            shopping_cart = session_cart;
        }
    }
}

//Update counter retrieved from session cart
$(window).on('load', function() {
    $('#shopping_cart_btn_counter').html(counter);
});

//Show registration form
$(function (){
    $('#goto_reg_btn').on('click', function(event) {
        $('#index-register-form').show();
    });
});

//Close purchase dialog
$(function (){
    $('#close_payment_btn').on('click', function(event) {
        $('#payment').hide();
    });
});

//Remove item from a shopping cart and session cart
$(function (){
    $('#shopping_cart_content').on("click", "tr .remove_img", function(){
    let remove_this = this.id;
        $(this).parent().parent().fadeOut(600, function(){
            shopping_cart.splice(remove_this, 1);
            sessionStorage.setItem('Session_cart', JSON.stringify(shopping_cart));
            show_shopping_cart();
        });
        
        counter--;
        $('#shopping_cart_btn_counter').html(counter);
        $('#shopping_cart_btn_counter').addClass('shrink');
    });
});

//Close modal when clicked outside and clear topping selections if any
$(function (){
  $('.modal').on('click', function(event) {
    let className = event.target.className;
    if(className === 'modal' ){
        
        $(this).closest('.modal').hide();
        clear_checkbox();
        toppings_selection_menu();
    }
  });
});

//Close modal when clicked X
$(function (){
  $('#close_toppings_modal_btn').on('click', function(event) {

    $(this).closest('.modal').hide();
    clear_checkbox();
    toppings_selection_menu();
  });
});

//Hide shopping cart and continue shopping
$(function (){
  $('.cancelbtn').on('click', function(event) {
      $("#shopping-cart").hide();
  });
});

//Payment - Pay button with payment animations
$(function (){
    
  $('.pay_btn').on('click', function(event) {
    payment = buy();
    
    if (payment == "Success"){

        $('#success').text("Your credit card's data was stolen successfuly.");
        $('.circle-loader').addClass('load-complete');
        clean_cart();  
    }
    else{

        $('#success').text(payment);
        $('.circle-loader').addClass('load-error');
        $('.checkmark').removeClass('draw').addClass('error').toggle();
    }
    
    $("#shopping-cart").hide();
    $("#payment").show();
    $(".loader").show();
    $('.circle-loader').show(); 
    $('.checkmark').show();
    $('#success').fadeIn(3000);
    
    $('.loader').fadeOut(3000);
    $('.checkmark').fadeOut(3000);
    $('.circle-loader').fadeOut(3000);
  });
});

//Main shopping cart button
$(function (){
    $('#shopping_cart_btn').click(function () {
        $('#shopping_cart_btn').addClass('shrink');
        $('#shopping_cart_btn_counter').addClass('shrink');
        show_shopping_cart();
    });
  
    $('#shopping_cart_btn').on("animationend", function(){
        $(this).removeClass('shrink');
    });
});

//Item counter of the shopping cart
$(function (){
    $('#shopping_cart_btn_counter').click(function () {
        $('#shopping_cart_btn').addClass('shrink');
        $('#shopping_cart_btn_counter').addClass('shrink');
        show_shopping_cart();
    });
  
    $('#shopping_cart_btn_counter').on("animationend", function(){
        $(this).removeClass('shrink');
        $(this).removeClass('pop');
    });
});

// Add item to shopping cart
$(function (){
    $('.items_for_cart').on('click', function(event) {

        let id = $(this).attr('id');
        let data = $(this).attr('data-name');
        let toppings = $(this).attr('data-toppings');
        let price = $(this).attr('data-price');
        let is_special = $(this).attr('data-is_special');
        
        if(typeof id !== 'undefined'){
            last_pick = {
                id: id,
                name: data,
                price: price
            };
            
            if(toppings == 0){

                counter++;
                $('#shopping_cart_btn_counter').html(counter);
                $('#shopping_cart_btn_counter').addClass('pop');
                
                toppingsdata = 'None';
                push_to_cart(id, data, price, toppingsdata);
            }
            if(toppings > 0){
                
                $('.nogroup').show();
                $('.steak_cheese').show();
                $('.extra').hide();
                $('#toppings_comment').hide();
                
                if(is_special == 1){
                    
                    $('#toppings_comment').show();
                    $('.nogroup').hide();
                    $('.extra').show();
                    $('#pizza-topping-selection').show();
                }
                if(is_special == 2){
                    
                    $('#toppings_comment').show();
                    $('.nogroup').hide();
                    $('.steak_cheese').hide();
                    $('.extra').show();
                    $('#pizza-topping-selection').show();
                }
                
                toppings_limit = toppings;
                $('#pizza-topping-selection').show();
            }
        }
    });
});

//Display shopping cart
function show_shopping_cart(){
    $('#shopping-cart').show();
    $('#shopping_cart_content').empty();
    if (shopping_cart === undefined || shopping_cart.length == 0) {
        
        $('#shopping_cart_content').html('There are no items in the shopping cart');
        $(".pay_btn").prop('disabled', true);
    }
    else {
        
        $(".pay_btn").prop("disabled", false);
        let count = 0;
        total_price = 0;
        
        for (let item of shopping_cart) {
            
            shopping_cart_content = '';
            
            if ((item.toppings) == 'None'){
                item.toppings = '';
            }
            
            let show_counter = count + 1;
            shopping_cart_content   = '<tr class=single_item>'
                                    + '<td id="cart_col_1">' + show_counter + '.</td>'
                                    + '<td id="cart_col_2">' + item.name + '<br> <p class="show_toppings">' + item.toppings + ' </p></td>'
                                    + '<td id="cart_col_3">' + '<img class="remove_img" id=' + count + ' src=' + remove_img + ' alt="remove item"/>'; + '</td>';
            
            $('#shopping_cart_content').append(shopping_cart_content); 
            total_price += parseFloat(item.price);
            count++;
        }
        
        shopping_cart_content = '<div id=total_price>Total price: ' + total_price.toFixed(2) + '  USD </div>';
        $('#shopping_cart_content').append(shopping_cart_content); 
    }
}

// Push selected item to the cart
function push_to_cart(id,data,price,toppings){
    const item = {
        id: id,
        name: data,
        price: price,
        toppings: toppings
    };

    // If Item is in Subs, it's 0.50 per topping, update price and full name of an item
    if (item.name.includes("Subs")){
        
        for (let topping of toppings) {
            temp = parseFloat(item.price) + 0.50;
            item.price = temp.toFixed(2) + '';
        }
        
        item.name = item.name.split('for')[0];
        item.name = item.name + 'for ' + item.price + ' USD.';
    }

    shopping_cart.push(item);
    sessionStorage.setItem('Session_cart', JSON.stringify(shopping_cart));
}

//Bold Topping on selection
$(function (){
    $( ".single_topping input[type=checkbox]" ).on( "click", function(){
        $( this ).parent().toggleClass( "bold_it" );
        toppings_selection_menu(this);
    });
});

//Selct toppings btn
$(function (){
    $('.select_topping_btn').click(function () {
        
        selected_toppings = [];
        
        $('.single_topping input[type=checkbox]:checked').each(function(){
            selected_toppings.push($(this).val());
        });
        
        counter++;
        $('#shopping_cart_btn_counter').html(counter);
        $('#shopping_cart_btn_counter').addClass('pop');
        
        push_to_cart(last_pick.id, last_pick.name, last_pick.price, selected_toppings);
        $('#pizza-topping-selection').hide();
        
        clear_checkbox();
        toppings_selection_menu();
        
    });
});

//Remove checkboxex from selected toppings
function clear_checkbox() {
    $('.single_topping input[type=checkbox]:checked').each(function(){
        this.checked = false;
        $( this ).parent().toggleClass( "bold_it" );
    });
    selected_toppings = [];
}

// Select toppins. Only as much as the item is limited to.
function toppings_selection_menu (selection) {
    if($('.single_topping input[type=checkbox]:checked').length > toppings_limit) {
        
        $( selection ).parent().toggleClass( "bold_it" );
        selection.checked = false;
    }
    else if($('.single_topping input[type=checkbox]:checked').length == toppings_limit){
        
        $(".single_topping input[type=checkbox]:not(:checked)").parent().addClass("disabled");
    }
    else{
        $(".single_topping input[type=checkbox]:not(:checked)").prop( "disabled", false );
        $(".single_topping input[type=checkbox]:not(:checked)").parent().removeClass("disabled");
    }
}

//Clean the cart's visualizations and data
function clean_cart(){
    
    shopping_cart.length = 0;
    counter = 0;
    toppings_limit = 1;
    selected_toppings = [];
    last_pick = 'None';
    sessionStorage.clear();
    
    $('#shopping_cart_btn_counter').html(counter);
    $('#shopping_cart_btn_counter').addClass('shrink');
    $('#shopping_cart_content').html('There are no items in the shopping cart');
}

// Expand order's details in an order list
$(function (){
    $( ".order_list" ).click(function() {
        $(this).next().toggle("hidden");
    });
});

// Buy items in a shopping cart
function buy(){
    
    status = 'No Status';
    
    let parameters = {
        order_id: 8,
        cart: shopping_cart,
        full_price: total_price
    };
    
    $.postJSON_SYNC( 'buy', parameters)
        .done(function(data) {
            status = data['status'];
        });
        
    return status;
}

// Extend jquery, add JSON data support for jquery post, 3rd party code
// Source - https://stackoverflow.com/questions/2845459/jquery-how-to-make-post-use-contenttype-application-json/2845471
jQuery.extend({

  postJSON: function(url, data, callback, type) {
	// shift arguments if data argument was omited
    if (jQuery.isFunction(data)) {
  		type = type || callback;
  		callback = data;
  		data = {};
	  }
    return jQuery.ajax({
      'headers': { "X-CSRFToken": getCookie("csrftoken")},
      'type': 'POST',
      'url': url,
      'contentType': 'application/json',
      'data': JSON.stringify(data),
      'dataType': 'json',
      'success': callback,
	  });
  }
});

// Extend jquery, add JSON data support for jquerry post, 3rd party code --- with SYNC
jQuery.extend({

  postJSON_SYNC: function(url, data, callback, type) {
	// shift arguments if data argument was omited
    if (jQuery.isFunction(data)) {
  		type = type || callback;
  		callback = data;
  		data = {};
	  }
    return jQuery.ajax({
      'headers': { "X-CSRFToken": getCookie("csrftoken")},
      'type': 'POST',
      'url': url,
      'contentType': 'application/json',
      'data': JSON.stringify(data),
      'dataType': 'json',
      'success': callback,
      'async': false,
	  });
  }
});

//https://docs.djangoproject.com/en/2.2/ref/csrf/
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


