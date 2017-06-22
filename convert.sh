#!/bin/bash
IN_DIR='svg';
OUT_DIR='pdf';

mkdir -p "$OUT_DIR";
for source in $IN_DIR/*.svg;
do
    source="${source##*/}";
    source="${source%.*}";
    printf "Converting $IN_DIR/$source.svg to $OUT_DIR/$source.pdf\n";
    convert -density 300x300        \
            -units PixelsPerInch    \
            -resize 3579x2551       \
            -repage 3579x2551       \
            -colorspace CMYK        \
            "$IN_DIR/$source.svg"   \
            "$OUT_DIR/$source.pdf";
done;

IN_DIR='./';
for source in $IN_DIR/order-of-service-*.svg;
do
    source="${source##*/}";
    source="${source%.*}";
    printf "Converting $IN_DIR/$source.svg to $OUT_DIR/$source.pdf\n";
    convert -density 300x300        \
            -units PixelsPerInch    \
            -resize 1819x2551       \
            -repage 1819x2551       \
            -colorspace CMYK        \
            "$IN_DIR/$source.svg"   \
            "$OUT_DIR/$source.pdf";
done;
