 

const gameQueryParams = {};
(() => {
  try {
    let url = window.location.search;
    if (url) {
      url = decodeURIComponent(url);
    }
    const temp1 = url.split("?");
    if (temp1 && temp1.length > 1) {
      const temp2 = temp1[1].split("&");
      if (temp2 && temp2.length) {
        temp2.forEach((arr) => {
          const temp3 = arr.split("=");
          if (temp3 && temp3.length === 2) {
            gameQueryParams[temp3[0]] = temp3[1];
          }
        });
      }
    }
  } catch (err) {
    console.log(err);
  }
})();	
if (gameQueryParams.adChannelId == 3214043746) {
console.log('landscape set for paytm')
window.parent.postMessage({
   'message': 'setLandscape'
}, "*");
}


