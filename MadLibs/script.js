function init()
{
	document.querySelector( "button").addEventListener('click',generateMsg);
}



function generateMsg()
{




	//Create a constant array of the ids of the input textfields.*/

 	let values = [];
  const idNames = ["NOUN1", "NOUN2", "VERB", "ADJECTIVE", "PLACE"];
for (let i=0; i <idNames.length; i++){
  let value = document.getElementById(idNames[i]).value;

	if (value === '') {
			values[i]= "Word Not Provided";
	}
	else {
		values[i]=value;
	}
}

	/*Using a for loop, populate the values array with the values of the
	 textfields*/



	let msg = `If anybody is wondering, please know that I am <strong>${values[2]}</strong> at <strong>${values[4]}</strong> without you.
	You might want to consider <strong>${values[3]}</strong> <strong>${values[0]}</strong>... then again, you always preferred
	<strong>${values[1]}</strong>.`;

 document.getElementById('msg').innerHTML=msg;
document.body.style.backgroundColor='blue';
 	//Display the msg string in the paragraph element with id 'msg'
}
