#!/bin/bash
read -p " Enter your age:" age
if [[ $age -lt 18 ]] && [[ $age -ge 0 ]]
then
	echo " You are minor !!"
elif [[ $age -eq 18 ]]
then
	echo " Congratulation, You've just become major !!"
elif [[ $age -gt 18 ]] && [[ $age -le 100 ]]
then
	echo " You are Major"
else
	echo " Invalid age!! "
fi
