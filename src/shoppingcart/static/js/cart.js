var updateBtn = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function(){
        var productID = this.dataset.product
        var action = this.dataset.action
        console.log('productID: ', productID, 'Action: ', action)
        console.log('User: ', user)

        if (user == 'AnonymousUser') {
            console.log('User is not authenticated')
        }else {
            updateUserOrder(productID, action)
        }
    })
}

function updateUserOrder(productID, action) {
    console.log('User is logged in, sending data...')

    var url = '/cart/update_item/'

    fetch(url, {
        method:'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body:JSON.stringify({'productID': productID, 'action': action})
    })

    .then((respone) => {
        return respone.json()
    })

    .then((data) => {
        console.log('Data: ', data)
        location.reload()
    })
}