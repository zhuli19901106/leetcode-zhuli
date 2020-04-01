# Read from the file file.txt and print its transposed content to stdout.
# cut and paste
for i in $(seq 1 $(cat file.txt | head -n 1 | awk '{print NF}')); do cut -d' ' -f"$i" file.txt | paste -d' ' -s; done
