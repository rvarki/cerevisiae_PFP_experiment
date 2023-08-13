# Cerevisiae PFP experiments

This repository contains the Snakemake used to run the cerevisiae PFP experiments. In these experiments, PFP was applied on pangenomes consisting of chromosome I of different cerevisiae strains. The goal of these experiments was to ascertain whether PFP is a viable option for tokenization of genomic data.

## Platform

The experiments were on HiPerGator, the University of Florida's supercomputing cluster. HiPerGator uses Slurm for managing hardware resources and scheduling jobs. For more information on HiPerGator, see https://www.rc.ufl.edu/about/hipergator/.

## Data

The cerevisiae strains used in these experiments are the strains referenced in this paper:  *The 100-genomes strains, an S. cerevisiae resource that illuminates its natural phenotypic and genotypic variation and emergence as an opportunistic pathogen* (doi: 10.1101/gr.185538.114). According to the paper, these strains are of near reference quality.

## Run Command

The run command provided below assumes that you are working on a computing cluster that uses the Slurm scheduler.

``` bash
snakemake --cluster "sbatch -A {cluster.account} -q {cluster.qos} -c {cluster.cpus-per-task} -N {cluster.Nodes}  -t {cluster.runtime} --mem {cluster.mem} -J {cluster.jobname} --mail-type={cluster.mail_type} --mail-user={cluster.mail} --output {cluster.out} --error {cluster.err}" --cluster-config cluster.json --jobs 100 --latency-wait 120 --configfile run_experiment.json
```


1. The Snakemake will attempt to install Marco Olivia's PFP (https://github.com/marco-oliva/pfp) via the singularity option. This will install an executable called `pfp_sif` in the working directory. **Note**: If there are issues downloading using the singularity option, please refer to Marco's Github page and try to download PFP using the other options described on the page.  

2. The Snakemake will create a directory called `reference/fasta` in the working directory and will attempt to download the fasta files corresponding to the accession numbers listed in `chr1_accessions.txt`. By default this file contains the accession numbers of the chromosme I fasta files of the 93 cerevisiae strains referenced in this paper: *The 100-genomes strains, an S. cerevisiae resource that illuminates its natural phenotypic and genotypic variation and emergence as an opportunistic pathogen* (doi: 10.1101/gr.185538.114) and the chromosome I of the strain S288c to this directory. These files will be labeled as `{genome}.{strain}.{chr}.fasta`. By default {genome} and {chr} are set to "cerevisiae" and "chr1" respectively, and {strain} will be set to the name provided in `chr1_accessions.txt` **Note**: Occassionally, not all the files will download successfully due to issues with NCBI and the rule might fail. If this happens, re-run the Snakemake again. 
  
3. The Snakemake will attempt to combine subsets of the fasta files into different sized reference pangenome fasta files and write these files to the `reference` directory. By default, the Snakemake will build pangenomes containing 10,20,30,40,50,60,70,80,93 strains. The files will be labeled as {genome}.{chr}.{ref}.pan.fasta where by default {genome} and {chr} are set to "cerevisiae" and "chr1" respectively, and {ref} is the number of strains included in the file.
 
4. The Snakemake will attempt to run PFP on the pangenomes. The Snakemake will create a directory called `output` in the working directory where it will write the PFP output files. PFP should output files with these extensions `.csv, .dict, .last, .occ, .parse, .sai`. The csv file contains the statistics reported by PFP. 
   
5. The Snakemake will attempt to combine all the csv files into one larger csv file called `combined.{genome}.{chr}.{w}.{p}.csv` where by default {genome}, {chr}, {w}, {p} are set to "cerevisiae", "chr1", "10", and "100" respectively. The Snakemake wull create a directory called `stats` in the working directory where it will write this file. 
  
