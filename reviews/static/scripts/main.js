const user_input = $("#user-input")
const content = $('#replaceable-content')
const endpoint = '/search'
const delay_by_in_ms = 700
let scheduled_function = false




let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
                content.html(response['html_from_view'])
            })
        }



user_input.on('keyup', function () {

    const request_parameters = {
        q: $(this).val()
    }


    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})
