const addBtns = document.getElementsByClassName('btn-addItem')
const payBtn = document.getElementById("make-payment")
var user = '{{request.user}}';

for (var i = 0; i < addBtns.length ; i++  ){
    addBtns[i].addEventListener('click', function(){
        var bookId = this.dataset.book
        var action = this.dataset.action
        console.log(action)
        if(user === 'AnonymousUser'){
            console.log("User is not authenticated")
        }
        else{
            updateUserOrder(bookId,action)
        }
    })
}

function updateUserOrder(bookId, action){

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'bookId':bookId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}




function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');




function submitFormData(){
    console.log('Payment button clicked')

    var userFormData = {
        'name':null,
        'email':null,
        'total':total,
    }

    var shippingInfo = {
        'address':null,
        'city':null,
        'state':null,
        'zipcode':null,
    }

    var url = "/process_order/"
        fetch(url, {
            method:'POST',
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken':csrftoken,
            }, 
            body:JSON.stringify({'form':userFormData, 'shipping':shippingInfo, "user":user}),
            
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.error == 'Error'){
                    console.log(data.error);
                    localStorage.setItem('orderError', 'Aby dokończyć zamówienie uzupełnij dane profilu');
                    window.location.reload();

            }
            else{
                console.log('Success:', data);
            localStorage.setItem('completed', 'Udało ci się złożyć zamówienie!');
            cart = {}
            document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
            
            url = "http://127.0.0.1:8000/"
            window.location.href = url
            }})
    }

payBtn.addEventListener('click', function(e){
    submitFormData()
})

window.onload = function() {
    var errorMessage = localStorage.getItem('orderError');

    if (errorMessage) {
        Swal.fire({
            position: "center",
            icon: 'info',
            text: errorMessage,
            showConfirmButton: true,
            color: 'White',
            background: 'rgb(243, 144, 205)',
            showClass: {
                popup: 'my-icon'
            },
        });
        localStorage.removeItem('orderError');
    } 
};