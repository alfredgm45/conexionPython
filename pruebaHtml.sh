#!/bin/bash
#
<<INFO
Ejemplo de utilización de arrays en bash
http://www.lawebdelprogramador.com
 
${valores[*]}         # Muestra todos los valores de un array
${!valores[*]}        # Muestra todos los indices de un array
${#valores[*]}        # Devuelve el numero de valores en un array
${#valores[0]}        # Devuelve la longitud del indice 0
INFO

echo "hola mundo"

printf "\nCantidad de valores dentro del array\n"

# definimos un array de valores
valores=("primero" "segundo" "tercero")
# añadimos un nuevo valor en la posicion 3 del array
valores[3]="quarto"

# añadimos un nuevo valor en la posicion 5 del array
valores[5]="quinto"

id=(
"36554434" "36554435" "36554436" "36554442" "36554443" "36554444" "36554445" "36554446" "36554447" "36554448" "36554449" "36554450" "36554451" "36554452" "36554453" "36554454" "36554455" "36554456" "36554457" "36554458" "36554459" "36554460" "36554461" "36554462" "36554463" "36554464" "36554465" "36554466")
 
tags=("06MV-1091_FE" "06MV-1091_LOC" "06NIVEL_T09" "06MV-1091" "06MV-01093"  "06MV-01094" "06MV-01095" "06MV-01096" "06MV-01097" "06MV-01098" "06MV-01090" "06MV-01091" "06MV-01092" "06MV-01093_FE" "06MV-01094_FE" "06MV-01095_FE" "06MV-01096_FE" "06MV-01097_FE" "06MV-01098_FE" "06MV-01090_FE" "06MV-01091_FE" "06MV-01092_FE" "06MV-01093_LOC" "06MV-01094_LOC" "06MV-01095_LOC" "06MV-01096_LOC" "06MV-01097_LOC" "06MV-01098_LOC")

printf "\nCantidad de valores dentro del array\n"
printf "   %s\n" ${#id[*]}
printf "   %s\n" ${#tags[*]}
 
printf "\nMostramos un valor dado\n"
printf "   %s\n" ${valores[2]}
 
printf "\nMostramos la longitud del indice 2\n"
printf "   %s\n" ${#valores[2]}
 
# recorremos todos los valores del array
printf "\nmostramos todos los valores\n"
for item in ${valores[*]}
do
    printf "   %s\n" $item
done
 
# recorremos todos los indices del array
printf "\nMostramos todos los indices\n"
for index in ${!valores[*]}
do
    printf "   %d\n" $index
done
 
# mostramos los indices y sus valores
printf "\nMostramos todos los indices con sus valores\n"
for index in ${!valores[*]}
do
    printf "%4d: %s\n" $index ${valores[$index]}
done

printf "\ncalidades\n"
for index in ${!id[*]}
do
   # echo " awk '/$tags[$index]/,/$id[$index]/{print substr($21,14)}' /opt/siog/taecjaa/AcquisitionData.html"
   printf "%s  %s\n" ${tags[$index]} ${id[$index]}
   awk '/'${id[$index]}'/{print substr($21,14)}' /opt/siog/taecjaa/AcquisitionData.html


done