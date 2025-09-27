# Purpose

When dealing with a large number of .vcf files, consistent ordering of the records (e.g., by chromosome and position) is crucial for downstream bioinformatics analysis, such as merging files or performing comparisons. These scripts automate that process.


# Execution examples :

python3 decoding.py
python3 VCF_Converter.py contacts_global_all.txt contacts_global_all.csv
python3 find_duplicates.py contacts_global_all.txt
python3 simple_vcf_extract.py contacts_global_all.vcf contacts_global_all.txt