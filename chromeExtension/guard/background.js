chrome.runtime.onInstalled.addListener(() => {
    chrome.action.setBadgeText({
        text: "Scan", 
    }); 


}); 

chrome.runtime.setUninstallURL(
    "https://google.com/"
)