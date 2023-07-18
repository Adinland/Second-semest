count=1
pth=$(pwd)
if [ ! -d "$pth/attachments" ]; then
	mkdir $pth/attachments
fi
while [ $count -lt 21 ]
do
	curl https://picsum/photos/800/400 -L > ./attachments/ph_$count.png
	wait
	let count=$count+1
done
