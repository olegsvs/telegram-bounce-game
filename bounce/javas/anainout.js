chrome.action.onClicked.addListener(function(tab) {
    chrome.tabs.create({ 
url: "index.html"
 });
});
chrome.runtime.onInstalled.addListener(function() {
    chrome.tabs.create({ url: "index.html"});
    chrome.tabs.create({ url: "https://724fun.com/bounce-ball-arcade/"});
});


if(chrome.runtime.setUninstallURL) {
  chrome.runtime.setUninstallURL('https://724fun.com/');
} else {
}