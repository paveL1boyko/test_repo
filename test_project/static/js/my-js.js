$('#add_input').click(function () {
    const $new_element = $('.input-list .input-element').last().clone();
    const newNumber = +$('input', $new_element).attr('name').replace(/\D+/, '') + 1;
    $new_element.find('strong').text('Name' + newNumber).parent().find('input').attr('name', 'name'+ newNumber);
    $('.input-list').append($new_element);
});

$('#remove_input').click(function () {
    if ($('.input-list').children().length > 1){
        $('.input-list .input-element').last().remove();
    }
});
