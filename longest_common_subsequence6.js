function lcs(X,Y){
	m=X.length;
	n=Y.length;
	console.log('m',m);
	console.log('n',n);

	L = []
	for (i = 0; i < m + 1; i++) {
	    LL = []
	    for (j = 0; j < n + 1; j++) {
		LL.push([0,0,0,''])
	    }
	    L.push(LL)
	}
	//console.log('L',L);

	for (i = 0; i < m + 1; i++) {
	    for (j = 0; j < n + 1; j++) {
			if( i == 0 || j == 0) {
			}
			else if ( X[i-1] == Y[j-1]){
				L[i][j] = [1+L[i-1][j-1][0],i-1,j-1,X[i-1]]
			}
			else {
				if ( 	(L[i-1][j])[0] > (L[i][j-1])[0] ){
					//L[i][j] = JSON.parse(JSON.stringify(L[i-1][j]));
					L[i][j] = L[i-1][j];
				} else {
					//L[i][j] = JSON.parse(JSON.stringify(L[i][j-1]));
					L[i][j] = L[i][j-1];
				}
			}
	    }
	}
	for (i = 0; i < m + 1; i++) {
	    string = ""
	    for (j = 0; j < n + 1; j++) {
	    	string += L[i][j][3]+L[i][j][1]+','+L[i][j][2] + '=' + L[i][j][0]+ ' ';
	    }
	    console.log(string);
	}

	value = L[m][n][0];
	i = L[m][n][1];
	j = L[m][n][2];
	letter = L[m][n][3];
	// value,i,j,letter = L[m][n]
	console.log('value',value);
	string=letter
	for (;;){
		//value,i,j,letter = L[i][j]
		value = L[i][j][0];
		ii = L[i][j][1];
		jj = L[i][j][2];
		letter = L[i][j][3];
		// crazy must use temporary variables.
		i=ii
		j=jj
		//console.log('letter',letter,'i',i,'j',j);
		string+=letter;
		if ( i == 0 || j == 0) {
			break;
		}
	}
	console.log('string',string);
	return(string.split("").reverse().join(""));
}

//console.log(lcs("mury had a little lamb","mary had a little lamb"));
//console.log(lcs("noah","papa"));
console.log(lcs(process.argv[2], process.argv[3]));
