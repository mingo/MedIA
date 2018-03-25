// const result = #;
const jsonFile = [1,0.85];
function verify(jsonFile){
	if (jsonFile[0] === 1){
		document.getElementById("score").innerHTML="Article Fiable!";

	} else {

	}


}
function hideDiv1(){
	document.getElementById("p1").style.display = "none";
	document.getElementById("p2").style.display = "block";
	verify(jsonFile);
}
function hideDiv2(){
	document.getElementById("p1").style.display = "block";
	document.getElementById("p2").style.display = "none";
}

