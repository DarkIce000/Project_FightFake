(() => {

    chrome.runtime.onMessage.addListener((obj,  sender, sendResponse) => {
        console.log(obj, sendResponse, sender)

        const {action} = obj;

        if(action === "grab"){

            const tweets = document.querySelectorAll('[data-testId="tweetText"]');
            const tweetTexts = Array.from(tweets).map((elem) => elem.innerText);
            console.log(tweetTexts);
            sendResponse(JSON.stringify(tweetTexts));
            console.log(JSON.stringify(tweetTexts));
        }
    })

    console.log('content Script'); 

})();