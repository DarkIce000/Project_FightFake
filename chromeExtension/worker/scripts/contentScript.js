PORT = 5000

async function sendToServerForAnalysis(PORT, tweetsarray){
    const response = await fetch(`http://localhost:${PORT}/analyse/local/`, {
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
                    accuracy.id = "hover-for-more";
                    accuracy.className = "tooltip"


                    if(!element.result.is_fake){
                        findTweet.style.color = "Red";
                    }else if(element.result.is_fake){
                        findTweet.style.color = "Green";
                    }else{
                        findTweet.style.color = "grey";
                    }
                    accuracy.innerHTML += '<br/> <span style="color:black; background-color:white;"> "Confidence Score: " '+ element.result.accuracy + "% </span>";
                    findTweet.appendChild(accuracy);

                    const tooltipDiv = document.createElement('div');
                    tooltipDiv.id = `popup-for-${element.id}`
                    tooltipDiv.className = "popup";
                    tooltipDiv.innerHTML = `
                                <div class="card">
                                    <div class="card-title">
                                        <h2>${element.result.is_fake }</h2>
                                        <hr/>
                                    </div>
                                    <div class="card-body">
                                        <div class="card-subheading">
                                        <h3>Analysis Report</h3> 
                                            <hr />
                                            <div class="card-subbody">
                                                <p>confidence score: ${ element.result.accuracy }</p>
                                                <p>extra commment: ${ element.result.extra_comment } </p>
                                                <p>sentiment analysis: ${element.result.sentiment_analysis } </p>
                                            </div>
                                        </div>
                                        <div class="card-subheading">
                                            <h3>Sources</h3> 
                                            <hr />
                                            <div class="card-subbody">
                                                ${ element.result.sources
                                                    .map((link) => '<li><a href="#">'+ link +'</a></li>'
                                                ).join('') }
                                            </div>
                                        </div>
                                    </div>
                                </div> 
                    `  
                    const body = document.querySelector('body');
                    body.appendChild(tooltipDiv);
                    accuracy.addEventListener('mouseover', () => {
                        let rect = findTweet.getBoundingClientRect();
                        tooltipDiv.style.top = 10+rect.y + "px";
                        tooltipDiv.style.left = 300+rect.x + "px";
                        tooltipDiv.classList.add('show');
                    })
                    accuracy.parentElement.parentElement.addEventListener('mouseleave', (e) => {
                        tooltipDiv.classList.remove('show');
                    })
                    tooltipDiv.addEventListener('mouseover', () => {
                        tooltipDiv.classList.add('show');
                    })
                    tooltipDiv.addEventListener('mouseleave', () => {
                        tooltipDiv.classList.remove('show');
                    })
                })

            }
            catch{
                console.log("cannot fetch");
            }
        }
    })

    console.log('content Script');

})();