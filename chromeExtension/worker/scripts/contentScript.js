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
                let tweetInfo = {
                    id: element.id,
                    text: element.innerHTML
                }
                tweetsarray.push(tweetInfo);
            })

            // send to the pop up html to display on the pop up
            sendResponse(JSON.stringify(tweetsarray));

            const analysisResult = await sendToServerForAnalysis(PORT, tweetsarray);
            console.log(analysisResult)


            // TODO: after getting result update twitter page 
            // TODO: send a message to the extension to update the pop up page
        }
    })

    console.log('content Script');

})();