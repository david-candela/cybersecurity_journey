# Linux Shells

`echo $SHELL`to see which shell I'm using

We use `./` before the script to run rather than typing the script name directly because `./` tells the shell to execute the file that is present in the current directory

#!/bin/bash
# Defining the directory to search our flag
directory="/var/log"

# Defining the flag to search
flag="thm-flag01-script"

echo "Flag search in directory: $directory in progress..."

# Defining for loop to iterate over all the files with .log extension in the defined direct>
for file in "/var/log"/*.log; do
    # Check if the file contains the flag
    if grep -q "$flag" "$file"; then
        # Print the filename
        echo "Flag found in: $(basename "$file")"
    fi
done
