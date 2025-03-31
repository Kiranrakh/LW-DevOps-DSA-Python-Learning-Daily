# Defining and using functions
fun1() { echo "I'm Kiran"; }
fun1

myuser() { cat /etc/passwd | grep bash$ | cut -d: -f1; }
myuser

# Function with argument handling
nfun() {
    name=$1
    echo "I'm $name"
}
nfun "Kiran"
nfun $(cat /etc/passwd | grep bash$ | cut -d: -f1)

# Network test function
mynettest() {
    ping -c 1 www.google.com &> /dev/null
    [ $? -eq 0 ] && echo "Net connected..!" || echo "Issue in net .."  
}
mynettest
