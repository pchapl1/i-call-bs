$('.vote-truth').on('click', function(e){
    e.preventDefault()
    console.log('its a vote for true')
    let vote = 'true';

    let poll = $(this).attr('id')

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
        console.log('true votes: ' + response_data['true_votes'])
        console.log('bs votes: ' + response_data['bs_votes'])
        $('#bs-vote-count-' + response_data['poll_pk']).text(response_data['bs_votes'])
        $('#true-vote-count-' + response_data['poll_pk']).text(response_data['true_votes'])
    }
})
})

$('.vote-bs').on('click', function(e){
    e.preventDefault()
    console.log('its a vote for bs')
    let vote = 'false';

    let poll = $(this).attr('id')

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
        console.log('true votes: ' + response_data['true_votes'])
        console.log('bs votes: ' + response_data['bs_votes'])
        $('#bs-vote-count-' + response_data['poll_pk']).text(response_data['bs_votes'])
        $('#true-vote-count-' + response_data['poll_pk']).text(response_data['true_votes'])

    }
})
})