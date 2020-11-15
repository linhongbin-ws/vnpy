result=$(python ./check_pyVersion.py 2>&1)

if [ $result != "p" ]; then
    echo "Strings are equal"
else
    echo "Strings are not equal"
fi