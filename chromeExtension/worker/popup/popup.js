import { getCurrentTab } from '../scripts/utils.js'

document.addEventListener("DOMContentLoaded", async () => {

    const scanBtn = document.querySelector('#scan-btn');
    const msg = document.querySelector('#msg-box'); 

    const activeTab = await getCurrentTab() ; 

    // check for which tab is active
    if(activeTab.url.includes('x.com')){
        msg.innerHTML = `${ activeTab.url }`;
    }else{
        msg.innerHTML = 'this is not twitter page';
        scanBtn.style.display = 'none';
    }

    // send a meassage to the content script to grab
    // text tweets
    scanBtn.onclick = () => {
        chrome.tabs.sendMessage(activeTab.id, {
            action: "grab"
        })
        .then( response => {

            let result = JSON.parse(response);
            // grab box for adding tweets
            const tweetBox = document.querySelector('#tweet-box');
            tweetBox.innerHTML = "" // clean

            result.forEach(element => {
                if (element.text !== " " && element.text !== null ){
                    tweetBox.innerHTML += '<li>' + element.id + ":" + element.text + '</li>';  // append
                }
            });

        })
    }

})