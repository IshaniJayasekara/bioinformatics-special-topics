#!/bin/bash

# basic search

pattern=$"WGKWVAEIR"
match=$(grep -r "$pattern" *.fasta| cut -d: -f1| sort -u)
echo $match
grep ">" $match| sed "s/>//" > AP2_basic_headers.txt

# advanced search

regex=$"WGKW[VA]AEIR"
match2=$(grep -r "$regex" *.fasta| cut -d: -f1| sort -u)
echo $match2
grep ">" $match2| sed "s/>//" > AP2_advanced_headers.txt

cat *.fasta| grep ">"| wc -l

for file in *.fasta;do cat "$file";echo "";done > combined.fasta