console.log('eddie max website')
console.log ('eddie the best django programmer in east and central africa')

let updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        let productId = this.dataset.product
        let action = this.dataset.action
        // console.log ('productId:', productId, 'action :',action)
        console.log ('USER:', user)
        if (user==='AnonymousUser') {
            console.log('Not loged in')    
        }else{
            updateUserOrder(productId, action)
        }
    })
    
}

function updateUserOrder(productId, action) {
    console.log('User is authenticated, sending data....')

    let url = '/update_item/'

    fetch(url,{
        method:'POST'
    
    }


    )
    
}

console.log ('Eddie is the  coolest programmer and an aspiring billionare and rollys royce buyer')