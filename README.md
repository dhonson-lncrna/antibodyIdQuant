# antibodyIdQuant

## Purpose
AntibodyIdQuant is a Python script that collects antibody-ID counts from quality control sequencing runs for ChIP-DIP and SPIDR. The script treats the entire FASTQ file as a single string and counts the occurences of antibody-ID sequences across the entire file. This is less precise than running barcode-ID, as it does not account for single-nucleotide sequencing errors or PCR expansion products. For the purpose of a quality control run, however, it is sufficient to get the relative oligo densities of each bead set. 

## Set-up
To run antibodyIdQuant, you must first have [Mamba](https://mamba.readthedocs.io/en/latest/index.html) installed. [Conda](https://docs.conda.io/projects/conda/en/latest/index.html) can also be used but tends to be slower. Once Mamba is activated, navigate to the antibodyIdQuant directory and run:

'''
mamba env create -f setup/antibodyIdQuant.yaml
'''

Once the environment is created, run:

'''
conda activate antibodyIdQuant
'''

## Running the script
AntibodyIdQuant has two inputs and one output. The first input is a tab-separated text file with no header in which column 0 is some descriptor of the type of ID (e.g., DPM), column 1 is the antibody-ID name (e.g., Bead-C1 or H3K9me3), and column 2 is the antibody-ID barcode sequence. An example file can be found in 'exampleData/antibodyId.csv'. 

The second input is an uncompressed FASTQ file for Read 1 of the antibody-ID quality control sequencing run. Read 1 will contain the antibody-ID barcode in the sense orientation. For details on library preparation and sequencing guidance, see the Antibody-ID Bead Quality Control 2 section of the [ChIP-DIP Protocol](https://www.notion.so/ChIP-DIP-17585f46d83b80c3a521ecbfcbf61b46?pvs=4).

The output is a comma-separated text file with the naming convention "YYYYMMDD_oligoCounts.csv" where YYYYMMDD is the current date. The file is deposited in the current working directory. Column 0 is the antibody-ID name (drawn from column 1 of the first input) and column 1 is the number of occurrences in the FASTQ file. 

To test your installation and see the output, navigate to the antibodyIdQuant directory, activate the antibodyIdQuant environment and run:

'''
python antibodyIdQuant.py exampleData/antibodyId.csv exampleData/exampleQcRun.fastq
'''

The example FASTQ file is ~30 Mb and contains only ~100,000 reads, so the script should finish in a few seconds and output a csv to the working directory.
