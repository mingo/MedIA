function hideDiv(action){
	const analyse = ["none", "block", sendLink()];
	const back = ["block", "none", () => {document.getElementById("score").innerHTML=""}];

	let now = [];
	if (action === "analyse")
		now = analyse;
	else if (action === "retourner")
		now = back;

	try {
		document.getElementById("p1").style.display = now[0];
		document.getElementById("p2").style.display = now[1];
		now[2];
	} catch(e) {
		console.log(e);
	}
}


function sendLink() {
	let link = document.getElementById("link").value;
	const getUrl = window.location;
	const url = `${getUrl.protocol}//${getUrl.host}/api/v1/ml?link=${link}`;

	fetch(url, {method: 'GET'})
		.then(res => res.json())
		.then(json => {
			console.log(json);
			verify(json);
		})
}

function verify(jsonFile){
	if (jsonFile.SiteYN === 1){
		document.getElementById("failDetail").innerHTML="";

		document.getElementById("YN").innerHTML="Article Fiable!";
		document.getElementById("score").innerHTML=(jsonFile.trustLevel * 100) + "% niveau de confiance";
	} else {
		document.getElementById("YN").innerHTML="Article N'est Pas Fiable!";
		document.getElementById("score").innerHTML=(jsonFile.trustLevel * 100) + "% niveau de confiance";

		let list = "L'article est non fiable pour les raisons suivantes:<ul>";
		if (jsonFile.Explanation[0] == 1){
			list += "<li>Partage de conspirations</li>";
		}
		if (jsonFile.Explanation[1] == 1) {
			list += "<li>Présentation de faits alternatifs à ceux qui sont vérifiables</li>";
		}
		if (jsonFile.Explanation[2] == 1) {
			list +="<li>Encouragement de la méfiance envers la science</li>";
		}
		if (jsonFile.Explanation[3] == 1) {
			list += "<li>Ommission d'informations qui ne conviennent pas à la vision de l'auteur</li>";
		}
		list += "</ul>"

		document.getElementById("failDetail").innerHTML=list;
		console.log(list);

	}
}

