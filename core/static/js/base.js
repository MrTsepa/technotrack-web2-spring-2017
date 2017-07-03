// (function() {
    var data = document.querySelector('#centrifuge').dataset || {};
    var centrifuge = new Centrifuge({
        url: data.url,
        user: data.user,
        timestamp: data.timestamp,
        token: data.token,
    });


    centrifuge.subscribe("news", function (message) {
        console.log(message);
        const popup = `
            <div> 
                ${message.data.msg} 
            </div>
        `

        const el = document.createElement('div');
        el.innerHTML = popup;
        document.querySelector('.msg_list').append(el);
        setTimeout(function(){
            el.remove();
        }, 10000);
    });

    centrifuge.connect();
// });
