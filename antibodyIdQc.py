from Bio import SeqIO
import pandas as pd
from datetime import datetime
import sys

if __name__ == "__main__":
    # Check arguments
    if len(sys.argv) < 3:
        print('Please provide an antibody-ID file and a fastq')
        sys.exit(1)

    # Read in antibody-ID and fastq
    ab_id = pd.read_csv(sys.argv[1],sep='\t',header=None)
    fastq = sys.argv[2]

    # Collect barcode counts
    ocount = {}
    with open('DHBioN_bcid_R1.fastq','r') as f:
        r = f.read()
        for i in ab_id.index:
            ocount[ab_id.loc[i,1]] = r.count(ab_id.loc[i,2])
    
    with open('DHBioN_bcid_R1.fastq','r') as f:
        reads = len(list(SeqIO.parse(f,'fastq')))

    ocount['unidentified'] = reads - sum(ocount.values()) 
    ocount['total'] = reads

    # Output results
    df = pd.DataFrame(ocount.items(),
                      columns=['antibody-ID','readCounts'])

    date = datetime.today().strftime('%Y%m%d')
    fname = '_'.join([date,'oligoCounts.csv'])
    df.to_csv(fname,sep='\t',index=False)