from Bio import SeqIO
import pandas as pd
from datetime import datetime
import sys

def spidr(ab_id,
          fastq):
    # Collect barcode counts
    ocount = {}
    with open(fastq,'r') as f:
        r = f.read()
        for i in ab_id.index:
            ocount[ab_id.loc[i,1]] = r.count(ab_id.loc[i,2])
        
    with open(fastq,'r') as f:
        reads = len(list(SeqIO.parse(f,'fastq')))
    
    ocount['unidentified'] = reads - sum(ocount.values()) 
    ocount['total'] = reads
    
    # Output results
    df = pd.DataFrame(ocount.items(),
                      columns=['antibody-ID','readCounts'])
    
    date = datetime.today().strftime('%Y%m%d')
    fname = '_'.join([date,'oligoCounts.csv'])
    df.to_csv(fname,index=False)

def chipdip(ab_id,
            fastq):
    # Dictionary to hold counts
    ocount = {}
    
    # Read in fastq
    with open(fastq,'r') as f:
        r = list(SeqIO.parse(f,'fastq'))
    
    # Extract sequences
    r = [str(s.seq) for s in r]
    # Drop dupes
    r = list(set(r))
    unique_reads = len(r)
    # Extract id
    r = [s[24:34] for s in r]

    # Loop through ids
    for i in ab_id.index:
        ocount[ab_id.loc[i,1]] = r.count(ab_id.loc[i,2])

    ocount['unidentified'] = unique_reads - sum(ocount.values()) 
    ocount['total'] = unique_reads

    # Output results
    df = pd.DataFrame(ocount.items(),
                      columns=['antibody-ID','readCounts'])
    
    date = datetime.today().strftime('%Y%m%d')
    fname = '_'.join([date,'oligoCounts.csv'])
    df.to_csv(fname,index=False)
        

if __name__ == "__main__":
    # Check arguments
    if len(sys.argv) < 4:
        print('''Please specify a run type (spidr or chipdip) and provide antibody-ID and fastq files.''')
        sys.exit(1)

    # Read in antibody-ID and fastq
    ab_id = pd.read_csv(sys.argv[2],sep='\t',header=None)
    fastq = sys.argv[3]
    
    # Run script
    if sys.argv[1] == 'spidr':
        spidr(ab_id, fastq)
        
    elif sys.argv[1] == 'chipdip':
        chipdip(ab_id,fastq)

    else:
        print('''Run type not recognized. Specify 'spidr' or 'chipdip'.''' )
        sys.exit(1)