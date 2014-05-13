if [ -r .config ]; then
    echo "Reading settings from config file."
    source .config
    changed=true
fi
if [ -z "$remote_host" ]; then
    default="web.engr.illinois.edu"
    read -e -p "Please enter the hostname: [$default] " remote_host
    remote_host="${remote_host:-$default}"
fi
if [ -z "$remote_user" ]; then
    default=`whoami`
    read -e -p "Please enter your username: [$default] " remote_user
    remote_user="${remote_user:-$default}"
fi
if [ -z "$remote_dest" ]; then
    default="~/public_html/"
    read -e -p "Please enter the destination directory: [$default] " remote_dest
    remote_dest="${remote_dest:-$default}"
fi

if [ -z "$changed" ]; then
    read -p "Would you like to overwrite the config file with these values? [y/N] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        cat << EOF > .config
remote_host=$remote_host
remote_user=$remote_user
remote_dest="$remote_dest"
EOF
    fi
fi
echo "Copying files to $remote_host with username $remote_user at directory $remote_dest."
rsync -rav -e ssh --exclude='*.md' --exclude='*.sh' --exclude='.*' \
. $remote_user@$remote_host:$remote_dest
