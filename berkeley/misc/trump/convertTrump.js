
var symbolReplace = [["FAKE NEWS", "NEWS"], ["OBSTRUCTIONISTS", "helpful"], ["delay", "smile"], ["complain", "compliment each other"], ["own", "share"], ["Terrible", "Wonderful!"], ["stronger", "more stable"], ["my", "our"], ["I", "we"], ["fake media", "media"], ["WALL", "lollipops"], ["enemy", "friend"], ["military", "peace-making"], ["disaster", "major success"], ["Fake News", "News"], ["unfairly", "fairly"],["collusion", "jibber-jabber"],["kill", "raise"], ["threaten", "compliment"],["colluding", "jibber-jabbering"],["badly", "with grace"],["Fake news", "News"],["Attack","prayer"],["Weapons","Bandaids"],["hate","love"],["Military","Peace-making"],["Korea","Friends"],["The real story","One version of the story that I feel strongly about"] ];

var tags = ["@international-love", "@world-peace", "@happiness", "@multiculturalism"];

var nonText = [" ", "!"];

var capitals = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];

function convert2(){
	var toReturn = [];
	//translatedTweets
	var parsed = JSON.parse(presTweets);
	var negativeWords = negatives.split(" ");
	var positiveWords = positives.split(" ");

	for (var i = 0; i < 5; i++){
		var jj = Math.floor(Math.random()*parsed.length);

		if (translatedTweets[jj].slice(0,6) == "Andrew"){
			i = i - 1;
			continue;
		}
		changed = translatedTweets[jj];	
		basicEdit = changed;

		while (basicEdit.includes('*')){
			basicEdit = basicEdit.replace('*','\'');
		}

		changed = basicEdit;

		for (var j = 0; j < symbolReplace.length; j++){
			if (changed.includes(symbolReplace[j][0])){
				if (nonText.includes(changed[changed.indexOf(symbolReplace[j][0])-1])){
					if (nonText.includes(changed[changed.indexOf(symbolReplace[j][0])+symbolReplace[j][0].length])){
						changed = changed.replace(symbolReplace[j][0],symbolReplace[j][1]);
					}
				}

			}
		}//This changes occurences of symbols with better symbols


		for (var j = 0; j < changed.length; j++){
			if (changed[changed.length - j - 1] == "@" || changed[changed.length-j-1] == "#"){
				for (var k = changed.length-j; k < changed.length; k++){
					if (changed[k] == " "){
						break;
					}
					if (changed[k] == "."){
						break;
					}
					if (changed[k] == "#"){
						break;
					}
					if (changed[k] == "@"){
						break;
					}
				}
				if (k == changed.length){
					k = k - 1;
				}
				changed = changed.replace(changed.substring(changed.length-j-1,k),tags[Math.floor(Math.random()*tags.length)]);
			}
		}

		toReturn.push([parsed[jj]['text'],changed]);
	}
	return(toReturn);
}

function convert3(){
	var toReturn = [];
	var parsed = JSON.parse(presTweets);
	var negativeWords = negatives.split(" ");
	var positiveWords = positives.split(" ");
	for (var i = 0; i < 5; i++){
		var somethingDone = 0; //this is 1 if something has been done
		var goodChanges = 0;	

		var jj = Math.floor(Math.random()*parsed.length);
		
		changed = parsed[jj]['text'];
		/*
		if (changed[0] == "." && changed[1] == "." && changed[2] == "."){
			console.log('top');
			var toAdd = parsed[jj+1]['text'];	
			if (toAdd[toAdd.length-1] == "." && toAdd[toAdd.length-2] == "." && toAdd[toAdd.length-3] == "."){
				console.log('topin');
				while (changed[0] == "."){
					changed = changed.slice(1);
				}
				while (toAdd[toAdd.length-1] == "."){
					toAdd = toAdd.slice(0,toAdd.length-1);
				}
				changed = toAdd + " " + changed;
			}
		}
		if (changed[changed.length-1] == "." && changed[changed.length-2] == "." && changed[changed.length-3] == "."){
			console.log('bottom');
			var toAdd = parsed[jj-1]['text'];	
			if (toAdd[1] == "." && toAdd[2] == "." && toAdd[0] == "."){
				console.log('bottomin');
				console.log(changed);
				while (changed[changed.length-1] == "."){
					changed = changed.slice(0,changed.length-1);
				}
				while (toAdd[0] == "."){
					toAdd = toAdd.slice(1);
				}
				changed = changed + " " + toAdd; 
			}
		}
		*/

		if (changed[0] == "." && changed[1] == "." && changed[2] == "."){
			i = i -1;
			continue;
		}
		if (changed[changed.length -1] == "." && changed[changed.length -2] == "." && changed[changed.length -3] == "."){
			i = i -1;
			continue;
		}

		basicEdit = changed;

		while (basicEdit.includes('*')){
			basicEdit = basicEdit.replace('*','\'');
		}

		changed = basicEdit;

		for (var j = 0; j < symbolReplace.length; j++){
			if (changed.includes(symbolReplace[j][0])){
				if (nonText.includes(changed[changed.indexOf(symbolReplace[j][0])-1])){
					if (nonText.includes(changed[changed.indexOf(symbolReplace[j][0])+symbolReplace[j][0].length])){
						changed = changed.replace(symbolReplace[j][0],symbolReplace[j][1]);
						somethingDone = 1;
						goodChanges += 1;
					}
				}

			}
		}//This changes occurences of symbols with better symbols

		//changed = changed.toLowerCase();
		for (var j = 0; j < negativeWords.length; j++){
			if (changed.includes(negativeWords[j])){
				if (nonText.includes(changed[changed.indexOf(negativeWords[j])-1])){
					if (nonText.includes(changed[changed.indexOf(negativeWords[j])+negativeWords[j].length])){
						changed = changed.replace(negativeWords[j], positiveWords[Math.floor(Math.random()*positiveWords.length)]);
						somethingDone = 1;
						goodChanges +=1;
					}
				}
			}
		}//Changes negative words for positive words

		for (var j = 0; j < changed.length; j++){
			if (changed[changed.length - j - 1] == "@" || changed[changed.length-j-1] == "#"){
				for (var k = changed.length-j; k < changed.length; k++){
					if (changed[k] == " "){
						break;
					}
					if (changed[k] == "."){
						break;
					}
					if (changed[k] == "#"){
						break;
					}
					if (changed[k] == "@"){
						break;
					}
				}
				if (k == changed.length){
					k = k - 1;
				}
				changed = changed.replace(changed.substring(changed.length-j-1,k),tags[Math.floor(Math.random()*tags.length)]);
				somethingDone = 1;
			}
		}

		for (var j = 0; j < changed.length; j++){
			var broken = 0;
			if (capitals.includes(changed[j]) == false){
				broken = 1;
				break;
			}
		}

		if (somethingDone == 0){
			i = i - 1;
			continue;
		}
		if (goodChanges < 3){
			i = i - 1;
			continue;
		}
		
		toReturn.push([basicEdit,changed]);
	}
	return(toReturn);
}
