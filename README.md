# cerevisiae_PFP_experiment

This repository contains the Snakemake used to run the cerevisiae PFP experiments. From a fresh clone of the repo, the Snakemake will run these rules in order:

1. The Snakemake downloads the chromosome I fasta files of the 93 cerevisiae strains referenced in the paper: *The 100-genomes strains, an S. cerevisiae resource that illuminates its natural phenotypic and genotypic variation and emergence as an opportunistic pathogen* (doi: 10.1101/gr.185538.114). Additionally, the Snakemake downloads the chromosome I fasta file of cerevisiae S288c.
2. The Snakemake will combine the individual fasta files into different sized reference fasta files.
3. The Snakemake will run PFP on the reference fasta files.
4. The Snakemake will combine the PFP stats csv files that into one csv file.
  
