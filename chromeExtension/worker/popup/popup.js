import { getCurrentTab } from '../scripts/utils.js'

document.addEventListener("DOMContentLoaded", async () => {

    const scanBtn = document.querySelector('#scan-btn');
    const msg = document.querySelector('#msg-box'); 

    const activeTab = await getCurrentTab() ; 

    if(activeTab.url.includes('x.com')){
        msg.innerHTML = `${ activeTab.url }`;
    }else{
        msg.innerHTML = 'this is not twitter page';
        scanBtn.style.display = 'none';
    }

    scanBtn.onclick = () => {
        chrome.tabs.sendMessage(activeTab.id, {
            action: "grab"
        })
        .then( response => {

            const tweetBox = document.querySelector('#tweet-box'); 
            let result = JSON.parse(response);
            console.log(result);
            tweetBox.innerHTML = ""

            // for (let i = 0; i < result.length; i++){
            //     if(i%2 !== 0){
            //         tweetBox.innerHTML += '<li>' + result[i] + '</li>'; 
            //     }
            // }

            result.forEach(element => {
                if (element !== " " && element !== null ){
                    tweetBox.innerHTML += '<li>' + element + '</li>';  
                }
            });
            
            
            
        })
    }

})

const connectServer = new Promise((resolve, reject) => {

    fetch("http://localhost:5000/", {
        body: JSON.stringify()
    })
    .then(reponse = reponse.json())
    .then(result => {
        console.log(result)
        resolve(result);
    })
    .catch(error => {
        console.log(error); 
    })

})