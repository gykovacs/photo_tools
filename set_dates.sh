#! /bin/bash

# installing exiftool is required

IMAGES=`find -name *.png`
for I in ${IMAGES}
do
    convert ${I} -quality 100 ${I%.png}.jpg
    FILENAME=`basename ${I}`
    JPGNAME=${I%.png}.jpg

    YEAR=${FILENAME:0:4}

    DATE="${YEAR}:02:02 02:02:02"

    exiftool -datetimeoriginal="${DATE}" -createdate="${DATE}" -modifydate="${DATE}" -filemodifydate="${DATE}" ${JPGNAME}

    rm ${JPGNAME}_original
done
