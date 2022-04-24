const decBtn = document.querySelector("#dec");
const incBtn = document.querySelector("#inc");
const timeVal = document.querySelector("#timeValue");
const timerToOn = document.querySelector("#timerToOn");
const timerToOff = document.querySelector("#timerToOff");
const showTimer = document.querySelector("#showTimer");
const timerPanel = document.querySelector(".timerPanel");
		

decBtn.addEventListener("click", function(){
	if(timeVal.value>1)
		timeVal.value--;
});
incBtn.addEventListener("click", function(){
	if(timeVal.value<60)
				timeVal.value++;
});
timeVal.addEventListener("change", function(){
	if(timeVal.value>60)
		timeVal.value = 60;
	else if(timeVal.value<1)
		timeVal.value = 1;
});
timerToOn.addEventListener("click", function(){
	timerToOn.classList.add("clicked");
	timerToOff.classList.remove("clicked");
})
timerToOff.addEventListener("click", function(){
	timerToOn.classList.remove("clicked");
	timerToOff.classList.add("clicked");
})
showTimer.addEventListener("click", function(){
	timerPanel.classList.add("showTmr");
})
