// chrome.tabs.onUpdated.addListener((tabId, loadStatus, tab ) => {


//     if(tab.url && tab.url.includes("x.com")){
//         chrome.tabs.sendMessage(tabId, {
//             status: "loaded",
//         })

//     }else {
//         console.log('not x'); 
//     }


// })

// chrome.action.onClicked.addListener((tabId, loadstate, tab) => {

//     if(tab.url && tab.url.includes("x.com")){
//         chrome.tabs.sendMessage(tabId, {
//             status: "loaded",
//         })

//     }else {
//         console.log('not x'); 
//     }

// }u