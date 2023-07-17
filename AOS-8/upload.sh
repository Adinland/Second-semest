count=1
while [ $count -lt 21 ]
do
	echo "GIGI"
	curl https://picsum/photos/800/400 -L > ./attachments/ph_$count.png
	wait
	let count=$count+1
done
