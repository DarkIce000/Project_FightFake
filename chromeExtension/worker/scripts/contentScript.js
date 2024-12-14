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

        const { action, id } = obj;

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

            // send to the pop up html to display on the pop up
            sendResponse(JSON.stringify(tweetsarray));

            const analysisResult = await sendToServerForAnalysis(PORT, tweetsarray);

            // TODO: after getting result update twitter page 
            analysisResult.forEach(element => {
                const findTweet = document.getElementById(`${element.id}`)
                const accuracy = document.createElement('span');
                if(!element.result.is_fake){
                    findTweet.style.color = "Red";
                    // findTweet.style.backgroundImage += "linear-gradient(315deg, #ffff45 0%, #ff5858 74%)"
                }else if(element.result.is_fake){
                    findTweet.style.color = "Green";

                    // findTweet.style.background = "rgb(46,47,51)";
                    // findTweet.style.background = "radial-gradient(circle, rgba(46,47,51,1) 0%, rgba(181,62,110,0.6362920168067228) 61%, rgba(255,0,0,0.927608543417367) 100%)";
                    // findTweet.style.backgroundColor = "Red";
                }else{
                    findTweet.style.color = "grey";
                }
                accuracy.innerHTML += '<br/> <span style="color:black; background-color:white;"> "Confidence Score: " '+ element.result.accuracy + "% </span>";
                findTweet.appendChild(accuracy);
            })

            // TODO: send a message to the extension to update the pop up page

            // await chrome.tabs.sendMessage(id, {
            //     action: "updatePopup", 
            //     id: id,
            //     result: analysisResult 
            // });

            // const response = await chrome.tabs.sendMessage(id, {
            //     action: "updatePopup",
            //     id: id,
            //     result:analysisResult
            // })
        }
    })

    console.log('content Script');

})();