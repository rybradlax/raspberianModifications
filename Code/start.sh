if [[ "$EUID" = 0 ]]; then
    echo "(1) already root"
else
    python3 open.py # make sure to ask for password on next sudo
    if open.py true; then
        echo "(2) correct password"
    else
        echo "(3) wrong password"
        exit 1
    fi
fi
# Do your sudo stuff here. Password will not be asked again due to caching.	