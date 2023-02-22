#!/bin/bash
input="./test.txt"
while IFS= read -r line
do
	echo "$line"	
	for (( i=0; i<${#line}; i++ )); do
		if [[ "${line:$i:1}" =~ [A-Z] ]]; then
			#echo "${line:$i:1}"
			echo "${line:0:$i}"
			echo "" >> LOG"${line:0:$i}".txt
			echo "<date>${line:$i:${#line}}" >> LOG"${line:0:$i}".txt

			break
		fi
	done
done < "$input"
