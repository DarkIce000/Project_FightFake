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
            try{
                const analysisResult = await sendToServerForAnalysis(PORT, tweetsarray);
                // TODO: after getting result update twitter page 
                analysisResult.forEach(element => {
                    const findTweet = document.getElementById(`${element.id}`)
                    const accuracy = document.createElement('span');


                    if(!element.result.is_fake){
                        findTweet.style.color = "Red";
                    }else if(element.result.is_fake){
                        findTweet.style.color = "Green";
                    }else{
                        findTweet.style.color = "grey";
                    }
                    accuracy.innerHTML += '<br/> <span style="color:black; background-color:white;"> "Confidence Score: " '+ element.result.accuracy + "% </span>";
                    findTweet.appendChild(accuracy);
                    
                })

            }
            catch{
                console.log("cannot fetch");
            }

            // TODO : to send msg back to the pop js to implement fake or not fake in pop js
            tweets.forEach(element => {
                sample_analysis_result =[
                    {
                        "id": "id__lae4wulxjp",
                        "text": "Krunal Pandya was too good in Pushpa 2.",
                        "result": {
                            "sentiment_analysis": "Positive",
                            "confidence_score": 60,
                            "extra_comment": "what gemini has extra to say about this text",
                            "is_fake": false,
                            "sources": [
                                "https://www.cinestaan.com/articles/27754/krunal-pandya-the-cricketer-was-not-in-pushpa-the-rule",
                                "https://www.republicworld.com/sports-news/cricket-news/ipl-2023-krunal-pandya-reveals-all-about-his-pushpa-celebration-after-dismissing-virat-kohli-articles-119234",
                                "https://www.news18.com/cricketnext/news/krunal-pandyas-pushpa-celebration-after-virat-kohlis-wicket-goes-viral-7529279.html"


                            ]
                        }
                    },
                    {
                        "id": "id__h051bt5l8kr",
                        "text": "That's why...🤔",
                        "result": {
                            "sentiment_analysis": "Neutral",
                            "confidence_score": 60,
                            "extra_comment": "what gemini think about this text",
                            "is_fake": "Not verifiable",
                            "sources": []
                        }
                    },
                    {
                        "id": "id__bv9ujpab2m",
                        "text": "Explorable Todo List",
                        "result": {
                            "sentiment_analysis": "Neutral",
                            "confidence_score": 60,
                            "extra_comment": "ai comments about given text",
                            "is_fake": "Not verifiable",
                            "sources": []
                        }
                    },
                    {
                        "id": "id__5qffdw89x5q",
                        "text": "source: tech twitter",
                        "result": {
                            "sentiment_analysis": "Neutral",
                            "confidence_score": 60,
                            "extra_comment": "ai comments about given text",
                            "is_fake": "Not verifiable",
                            "sources": []
                        }
                    },
                    {
                        "id": "id__oo6pxa080v",
                        "text": "We found it in archives. 16 years ago, in 2008, at a summit of Arab leaders in Damascus, Gaddafi, showing the execution of Saddam Hussein, said:",
                        "result": {
                            "sentiment_analysis": "Neutral",
                            "confidence_score": 60,
                            "extra_comment": "ai comments about given text", 
                            "is_fake": "Not verifiable", 
                            "sources": []
                        }
                    }
                ]
                // create a div 
                const tooltipDiv = document.createElement('div');
                tooltipDiv.className = "tooltip";


                tooltipDiv.innerHTML = `
                <p>checker</p>
                        <div class="card">
                            <div class="card-title">
                                <h2>Fake</h2>
                                <hr/>
                            </div>
                            <div class="card-body">
                                <div class="card-subheading">
                                <h3>Analysis Report</h3> 
                                    <hr />
                                    <div class="card-subbody">
                                        <p>confidence score: </p>
                                        <p>extra commment: </p>
                                        <p>sentiment analysis: </p>
                                    </div>
                                </div>
                                <div class="card-subheading">
                                    <h3>Sources</h3> 
                                    <hr />
                                    <div class="card-subbody">
                                        <li><a href="#">google.com</a></li>    
                                        <li><a href="#">google.com</a></li>    
                                        <li><a href="#">google.com</a></li>    
                                    </div>
                                </div>
                            </div>
                        </div> 
                `



                element.appendChild(tooltipDiv);

            })

        }
    })

    console.log('content Script');

})();