var lastScrollTop = 0;
const returnTop = document.getElementsByClassName("returnTop")[0];
const returnTopHeight =50;


window.addEventListener("scroll", function(){ // or window.addEventListener("scroll"....
   var st = document.body.scrollTop; // Credits: "https://github.com/qeremy/so/blob/master/so.dom.js#L426"
   if (st < lastScrollTop && st>=100 ) {
      // upscroll code
      console.log("ok");
      if (returnTop.offsetHeight==0) {
         console.log("ok2")
         returnTop.style.height = "fit-content";
      }
   } 
   else {
      if (returnTop.offsetHeight>=0) {
         returnTop.style.height = "0px";
      }
   }// else was horizontal scroll
   lastScrollTop = st <= 0 ? 0 : st; // For Mobile or negative scrolling
}, false);


function goToTop (event) {
   document.body.scrollTop = 0;
}