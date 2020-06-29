$('.message .close').on('click', function () {
    $(this)
    .closest('.message')
    .transition('fade');
});

function signin(){

    var formData  = new FormData();
    formData.append('username',$('#signin_form').find('input[name="username"]').val());
    formData.append('password',$('#signin_form').find('input[name="username"]').val());

	fetch($('#server_endpoint').val() + '/user/signin',{
		method: 'POST',
		body: formData
	})
	.then(response => response.json())
	.then((response) => {
        if(response.status == 'success'){
            location.reload();
        } else {
            $('#signin_message').html(response.message);
            $('#signin_fail').show();
        }
    }).catch(err=>{
        console.log(err)
    })
    
}

function signup(){

    var formData  = new FormData();
    formData.append('username',$('#signup_form').find('input[name="username"]').val());
    formData.append('password',$('#signup_form').find('input[name="password"]').val());
    formData.append('repassword',$('#signup_form').find('input[name="repassword"]').val());

	fetch($('#server_endpoint').val()+'/user/signup',{
		method: 'POST',
		body: formData
	})
	.then(response => response.json())
	.then(function(response) {
        
        if(response.status == 'success'){
            $('#signup_success').show();
        } else {
            $('#signup_message').html(response.message);
            $('#signup_fail').show();
        }
    }).catch(err=>console.log(err))

}

function signout(){
    fetch($('#server_endpoint').val()+'/user/signout')
	.then(() => window.location.href = "/")
}
