function sendLink() {
	let link = document.getElementById("link").value;
	const getUrl = window.location;
	const url = `${getUrl.protocol}//${getUrl.host}/api/v1/ml?link=${link}`;

	fetch(url, {method: 'GET'})
		.then(res => res.json())
		.then(json => verify(json))
}

function verify(jsonFile){
	if (jsonFile['trustWorthy'] === 1){
		document.getElementById("score").innerHTML="Article Fiable!";

	} else {

	}
}


function hideDiv(action){
	const analyse = ["none", "block", sendLink()];
	const back = ["block", "none", () => {document.getElementById("score").innerHTML=""}]

	let now = [];
	if (action === "analyse")
		now = analyse
	else if (action === "retourner")
		now = back

	try {
		document.getElementById("p1").style.display = now[0];
		document.getElementById("p2").style.display = now[1];
		now[2];
	} catch(e) {
		console.log(e);
	}
}
