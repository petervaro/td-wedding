#!/bin/bash
IN_DIR="svg";
OUT_DIR="pdf";

mkdir -p "$OUT_DIR";
for source in $IN_DIR/*.svg;
do
    source="${source##*/}";
    source="${source%.*}";
    printf "Converting $IN_DIR/$source.svg to $OUT_DIR/$source.pdf\n";
    convert -density 300 -colorspace CMYK "$IN_DIR/$source.svg" "$OUT_DIR/$source.pdf";
done;
