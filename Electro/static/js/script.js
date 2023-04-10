$(document).ready(function () {
	$('.increment-btn').click(function (e) {
		e.preventDefault();

		var inc_value = $(this).closest('.quantity').find('.qty-input').val();
		var value = parseInt(inc_value,10);
		value = isNaN(value) ? 0 : value;
		if(value < 10)
		{
			value++;
			$(this).closest('.quantity').find('.qty-input').val(value);
		} 
	});

	$('.decrement-btn').click(function (e) {
		e.preventDefault();

		var dec_value = $(this).closest('.quantity').find('.qty-input').val();
		var value = parseInt(dec_value,10);
		value = isNaN(value) ? 0 : value;
		if(value > 1)
		{
			value--;
			$(this).closest('.quantity').find('.qty-input').val(value);
		} 
	});

	// cart = JSON.parse(localStorage.getItem('cart'));
	// document.getElementById('cart').innerHTML = object.keys(cart).length;

	$('.addToCartBtn').click(function (e) {
		e.preventDefault();

		var product_id = $(this).closest('.product_data').find('.pros_id').val();
		var quantity = $(this).closest('.product_data').find('.qty-input').val();
		var token = $('input[name = csrfmiddlewaretoken]').val();

		$.ajax({
			method: "POST",
			url: "/add-to-cart",
			data:{
				'product_id':product_id,
				'quantity':quantity,
				csrfmiddlewaretoken: token
			},
			success: function(response){
				console.log(response)
				alertify.success(response.status)
			}		
		});
	});

    $('.ChangeQuantity').click(function (e) {
		e.preventDefault();

		var product_id = $(this).closest('.product_data').find('.pros_id').val();
		var quantity = $(this).closest('.product_data').find('.qty-input').val();
		var token = $('input[name = csrfmiddlewaretoken]').val();

		$.ajax({
			method: "POST",
			url: "/update-cart",
			data:{
				'product_id':product_id,
				'quantity':quantity,
				csrfmiddlewaretoken: token
			},
			success: function (response) {
				location.reload();
			}
		});
		

	});

    $('.delete-cart-item').click(function (e) {
		e.preventDefault();

		var product_id = $(this).closest('.product_data').find('.pros_id').val();
		var token = $('input[name = csrfmiddlewaretoken]').val();

		$.ajax({
			method: "POST",
			url: "/delete-cart-item",
			data:{
				'product_id':product_id,
				csrfmiddlewaretoken: token
			},
			success: function (response) {
				location.reload();
			}
		});
	});

});