const timeToRefresh = document.querySelector("#timeToRefresh");

if(timeToSwitch != null){
	var now = new Date();
	var timeLeft = parseInt((timeToSwitch.getTime() - now.getTime()) / 1000) -1;
	var timeToReplace = timeLeft;
	
	document.getElementById("timeRefreshPanel").classList.remove("hide");
	document.getElementById("showTimer").classList.add("hide");
	if(timeLeft >= 0){
			if(timeLeft <= 5){
						timeToRefresh.style.color="red";
					}
			timeToRefresh.innerHTML = new Date(timeLeft * 1000).toISOString().substring(14, 19);
			setInterval(function() {
				if(timeLeft > 0){
					now = new Date();
					timeLeft = parseInt((timeToSwitch.getTime() - now.getTime()) / 1000) -1;
					timeToRefresh.innerHTML = new Date(timeLeft * 1000).toISOString().substring(14, 19);
					if(timeLeft <= 5 && timeToRefresh.style.color != "red"){
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
