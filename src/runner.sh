cd $2
if [ "$3" = "noloop" ]; then
    $1
else
    while true; do
        $1
    done
fi