PORT = 5000

async function sendToServerForAnalysis(PORT, tweetsarray){
    const response = await fetch(`http://localhost:${PORT}/analyse/gemini/`, {
        method: "POST",
        body: JSON.stringify({
            data: tweetsarray
        }),
    })

    const result = await response.json();

    if(!response.ok){
        throw new Error(`HTTP Error ${response.status}`)
    }

    return result
}

(() => {

    chrome.runtime.onMessage.addListener(async (obj, sender, sendResponse) => {
        console.log(obj, sendResponse, sender)

        const { action } = obj;

        if (action === "grab") {
            const tweets = document.querySelectorAll('[data-testId="tweetText"]');

            // serializing tweets
            let tweetsarray = []
            tweets.forEach((element) => {
                if (element.id !== ""){
                    let tweetInfo = {
                        id: element.id,
                        text: element.innerHTML || element.textContent
                    }
                    tweetsarray.push(tweetInfo);
                }
            })

            // send to the pop up html to display on the pop up
            sendResponse(JSON.stringify(tweetsarray));
            console.log("tweetsaaray: ", tweetsarray);

            const analysisResult = await sendToServerForAnalysis(PORT, tweetsarray);
            console.log("analysisresult: ", analysisResult)

            // TODO: after getting result update twitter page 
            analysisResult.forEach(element => {
                const findTweet = document.getElementById(`${element.id}`)
                if(element.is_fake == true){
                    findTweet.style.color = "red";
                }else if(element.is_fake == false){
                    findTweet.style.color = "green";
                }else{
                    findTweet.style.color = "yellow";
                }
            })

            // TODO: send a message to the extension to update the pop up page
            chrome.tabs.sendMessage(activeTab.id, {
                action: "updatePopup", 
                result: analysisResult 
            })
        }
    })

    console.log('content Script');

})();