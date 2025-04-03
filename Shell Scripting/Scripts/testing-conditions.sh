#!/bin/bash
read -p " Enter your age :" age

if [[ $age -lt 18 ]]
then
	echo " You  are minor!"
elif [[ $age -eq 18 ]]
then
	echo " Congratulation, you've just become major !!"
else
	echo " You are major"
fi
