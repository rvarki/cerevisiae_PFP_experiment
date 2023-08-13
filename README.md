# Cerevisiae PFP experiments

This repository contains the Snakemake used to run the cerevisiae PFP experiments. From a fresh clone of the repo, the Snakemake will run these rules in order by default:

1. The Snakemake will attempt to install Marco Olivia's PFP (https://github.com/marco-oliva/pfp) via the singularity option. This will install an executable called `pfp_sif` in the directory above the working directory. **Note**: If there are issues downloading using the singularity option, please refer to Marco's Github page and try to download PFP using the other options described on the page.  

2. The Snakemake will create a directory called `reference/fasta` and will attempt to download the fasta files corresponding to the accession numbers listed in `chr1_accessions.txt`. By default this file contains the accession numbers of the chromosme I fasta files 
of the 93 cerevisiae strains referenced in this paper: *The 100-genomes strains, an S. cerevisiae resource that illuminates its natural phenotypic and genotypic variation and emergence as an opportunistic pathogen* (doi: 10.1101/gr.185538.114) and the chromosome I of the strain S288c to this directory. These files will be labeled as `{genome}.{strain}.{chr}.fasta`. By default {genome} and {chr} are set to "cerevisiae" and "chr1" respectively, and {strain} will be set to the name provided in `chr1_accessions.txt` **Note**: Occassionally, not all the files will download successfully due to issues with NCBI and the rule might fail. If this happens, re-run the Snakemake again. 
  
3. The Snakemake will attempt to combine subsets of the fasta files into different sized reference pangenome fasta files and write these files to `reference`. By default, the Snakemake will build pangenomes containing 10,20,30,40,50,60,70,80,93 strains. The files will be labeled as {genome}.{chr}.{ref}.pan.fasta where by default {genome} and {chr} are set to "cerevisiae" and "chr1" respectively, and {ref} is the number of strains included in the file.

  
9. The Snakemake will run PFP on the reference fasta files.
10. The Snakemake will combine the PFP stats csv files that into one csv file.
  
