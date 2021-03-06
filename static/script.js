const timeVal = document.querySelector("#timeValue");
const timerToOn = document.querySelector("#timerToOn");
const timerToOff = document.querySelector("#timerToOff");
const showTimer = document.querySelector("#showTimer");
const timeSlider = document.querySelector("#timeSlider");
const timerPanel = document.querySelector(".timerPanel");
const minBtn = document.querySelector("#timerToMin");
const secBtn = document.querySelector("#TimerToSec");
const actionInp = document.querySelector("#actionInput");
const typeInp = document.querySelector("#typeInput");
const cancel = document.querySelector("#cancel");
		
window.onload = function(){ 
	timerPanel.classList.add("showTmrTr");
	if(timeToReplace != null && timeToReplace >= 0){
			setTimeout(() => { window.location.replace('/');}, timeToReplace * 1000);
	}
	else if(timeLeft < 0)
		window.location.replace('/');
}
		
timeVal.addEventListener("change", function(){
	if(timeVal.value>60)
		timeVal.value = 60;
	else if(timeVal.value<1)
		timeVal.value = 1;
});
timerToOn.addEventListener("click", function(){
	timerToOn.classList.add("turnOn");
	timerToOff.classList.remove("turnOff");
	actionInp.value = "on";
})
timerToOff.addEventListener("click", function(){
	timerToOn.classList.remove("turnOn");
	timerToOff.classList.add("turnOff");
	actionInp.value = "off";
})
showTimer.addEventListener("click", function(){
	timerPanel.classList.toggle("showTmr");
})
timeSlider.addEventListener("input", function(){
	timeVal.value = timeSlider.value;
})
timerToSec.addEventListener("click", function(){
	timerToSec.classList.add("clicked");
	timerToMin.classList.remove("clicked");
	typeInp.value = "sec";
})
timerToMin.addEventListener("click", function(){
	timerToSec.classList.remove("clicked");
	timerToMin.classList.add("clicked");
	typeInp.value = "min";
})
cancel.addEventListener("click", function(){
	document.getElementById("stopping").innerHTML = "Zatrzymywanie";
})
