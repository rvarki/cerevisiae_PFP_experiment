#!/usr/bin/env python3
import requests
import argparse
import os

Description = """
Download batch of accessions from NCBI

   by Rahul Varki
"""

def start_session(search_term):
    search_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&term={search_term}&retmax=10&retmode=json&usehistory=y"
    response = requests.get(search_url)
    print(response.text)
    data = response.json()
    webenv = data['esearchresult']['webenv']
    query_key = data['esearchresult']['querykey']
    return webenv, query_key

def download_batch(webenv, query_key, outdir, accessions, strains, genome, chromosome):
    base_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&query_key={query_key}&WebEnv={webenv}&rettype=fasta&retmode=text"
    
    for i in range(len(accessions)):
        accession = accessions[i]
        strain = strains[i]

        url = f"{base_url}&id={accession}"
        response = requests.get(url)
        
        if response.status_code == 200:
            fasta_content = response.text
            filename = f"{genome}.{strain}.{chromosome}.fasta"
            fasta_file = os.path.join(outdir, filename)
            with open(fasta_file, "w") as infile:
                infile.write(fasta_content)
            print(f"Downloaded {filename}")
        else:
            print(f"Failed to download {accession}")

def extract_accession_names(accession_file):
    accessions = []
    with open(accession_file, "r") as infile:
        for line in infile:
            accessions.append(line.split()[1])
    
    return accessions

def extract_strain_names(accession_file):
    strains = []
    with open(accession_file, "r") as infile:
        for line in infile:
            strains.append(line.split()[0])
    
    return strains


def main():
    parser = argparse.ArgumentParser(description=Description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-i', '--input', help='Accession text file', type=str, dest="input")
    parser.add_argument('-o', '--output', help='Output directory', type=str, dest="output")
    parser.add_argument('-g', '--genome', help='Genome name', type=str, dest="genome")
    parser.add_argument('-c', '--chromosome', help='Chromosome name', type=str, dest="chromosome")
    args = parser.parse_args()

    # Create output directory if it does not exist
    if not os.path.exists(args.output):
        os.makedirs(args.output, exist_ok=True)

    # Search term (e.g., organism name or other relevant keywords)
    search_term = args.genome

    # Accession numbers
    accessions = extract_accession_names(args.input)

    # Strain names
    strains = extract_strain_names(args.input)

    # Start a session and retrieve webenv and query_key
    webenv, query_key = start_session(search_term)

    # Download the batch of FASTA sequences
    download_batch(webenv, query_key, args.output, accessions, strains, args.genome, args.chromosome)


if __name__ == '__main__':
    main()
