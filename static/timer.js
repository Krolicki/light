const timeToRefresh = document.querySelector("#timeToRefresh");

if(timeToSwitch != null){
	var now = new Date();
	var timeLeft = parseInt((timeToSwitch.getTime() - now.getTime()) / 1000);
	var timeToReplace = timeLeft;
	
	document.getElementById("timeRefreshPanel").classList.remove("hide");
	document.getElementById("showTimer").classList.add("hide");
	if(timeLeft >= 0){
			timeToRefresh.innerHTML = timeLeft;
			setInterval(function() {
				if(timeLeft > 0){
					now = new Date();
					timeLeft = parseInt((timeToSwitch.getTime() - now.getTime()) / 1000);
					timeToRefresh.innerHTML = timeLeft;
					if(timeLeft == 5){
						timeToRefresh.style.color="red";
					}
				}
			}, 1000);
	}
}
else{
		document.getElementById("timeRefreshPanel").classList.add("hide");
		document.getElementById("showTimer").classList.remove("hide");
		timeToRefresh.innerHTML = "?";
		var timeToReplace = null;
}
