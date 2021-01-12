var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length ; i++)
{
    updateBtns[i].addEventListener('click',function()
    {
        var productId = this.dataset.product
        var action = this.dataset.action
        var type = this.dataset.type

        console.log('productId:',productId,'Action:',action,'type:',type)

        console.log('USER:', user)
        if (user=='AnonymousUser')
        {
            console.log('user is Unauth')
        }
        else
        {
            if (type == 'product')
            {
                updateUserOrder (productId,action)
            }
            else if (type == 'post')
            {
                postupdateUserOrder (productId,action)
            }
        }

    })

}

function updateUserOrder (productId,action)
{
    console.log('user is Auth')

    var url ='/update_item/'

    fetch(url,{
        method: 'POST',
        headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                 },
        body: JSON.stringify({'productId': productId,'action':action})
    })
    .then((response) => {
    return response.json()
    })

    .then((data) => {
    console.log('data: ',data)
    location.reload()
    })
}

function postupdateUserOrder (productId,action)
{
    console.log('user is Auth')

    var url ='/update_itempost/'

    fetch(url,{
        method: 'POST',
        headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                 },
        body: JSON.stringify({'postId': productId,'action':action})
    })
    .then((response) => {
    return response.json()
    })

    .then((data) => {
    console.log('data: ',data)
    location.reload()
    })
}