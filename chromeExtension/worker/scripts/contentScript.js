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
                        text: element.innerText || element.textContent
                    }
                    tweetsarray.push(tweetInfo);
                }
            })

            console.log("tweetsaaray: ", tweetsarray);
            // send to the pop up html to display on the pop up
            sendResponse(JSON.stringify(tweetsarray));

            const analysisResult = await sendToServerForAnalysis(PORT, tweetsarray);
            console.log("analysisresult: ", analysisResult)

            // TODO: after getting result update twitter page 
            analysisResult.forEach(element => {
                const findTweet = document.getElementById(`${element.id}`)
                console.log(element)
                if(element.result.is_fake === "False"){
                    findTweet.style.color = "green";
                }else if(element.result.is_fake === "True"){
                    findTweet.style.color = "red";
                }else{
                    findTweet.style.color = "grey";
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