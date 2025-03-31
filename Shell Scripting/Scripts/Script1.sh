# Prompt the user to pass three arguments
name=${1:?"Error : plz pass name"}
age=${2:?"Error : plz pass age"}
remarks=${3:?"Error : plz pass remark"}

# Check if the number of arguments is less than 3
test $# -lt 3 && echo "not supported u passed $# arguments  i need 3 args " || echo "your name is ${name^} with age "${age}" ur remark is ${remarks^^}"

# Run the script
bash script1.sh kiranRakh 20 vgood
