$('.vote-truth').on('click', function(e){
    e.preventDefault()

    let vote = 'true';

    let poll = $(this).attr('id')
    console.log(poll)
    $.ajax({
    type: 'POST',
    url: '/new-vote',
    datatype: 'json', 
    data: 
    {
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        vote: vote,
        the_poll: poll
    },
    success:function(response_data){
        console.log('submitted')
        $('#bs-vote-count-'+ response_data['poll_pk']).text(response_data['bs_votes'])
        $('#true-vote-count-'+ response_data['poll_pk']).text(response_data['true_votes'])
    }
})
})

$('.vote-bs').on('click', function(e){
    e.preventDefault()

    let vote = 'false';

    let poll = $(this).attr('id')

    let count = $(this).text()

    $.ajax({
    type: 'POST',
    url: '/new-vote',
    datatype: 'json', 
    data: 
    {
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        vote: vote,
        the_poll: poll
    },
    success:function(response_data){
        console.log('submitted')

        $('#bs-vote-count-' + response_data['poll_pk'] ).text(response_data['bs_votes'])
        $('#true-vote-count' + response_data['poll_pk']).text(response_data['true_votes'])

    }
})
})