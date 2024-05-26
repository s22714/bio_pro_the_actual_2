import primer3

results = primer3.bindings.design_primers(
    seq_args={
        'SEQUENCE_ID': 'MH1000',
        'SEQUENCE_TEMPLATE': 'GCTTGCATGCCTGCAGGTCGACTCTAGAGGATCCCCCTACATTTT'
                             'AGCATCAGTGAGTACAGCATGCTTACTGGAAGAGAGGGTCATGCA'
                             'ACAGATTAGGAGGTAAGTTTGCAAAGGCAGGCTAAGGAGGAGACG'
                             'CACTGAATGCCATGGTAAGAACTCTGGACATAAAAATATTGGAAG'
                             'TTGTTGAGCAAGTNAAAAAAATGTTTGGAAGTGTTACTTTAGCAA'
                             'TGGCAAGAATGATAGTATGGAATAGATTGGCAGAATGAAGGCAAA'
                             'ATGATTAGACATATTGCATTAAGGTAAAAAATGATAACTGAAGAA'
                             'TTATGTGCCACACTTATTAATAAGAAAGAATATGTGAACCTTGCA'
                             'GATGTTTCCCTCTAGTAG',
        'SEQUENCE_INCLUDED_REGION': [40, 240]
    },
    global_args={
        'PRIMER_NUM_RETURN': 5,
        'PRIMER_OPT_SIZE': 20,
        'PRIMER_PICK_INTERNAL_OLIGO': 1,
        'PRIMER_INTERNAL_MAX_SELF_END': 8,
        'PRIMER_MIN_SIZE': 18,
        'PRIMER_MAX_SIZE': 25,
        'PRIMER_OPT_TM': 60.0,
        'PRIMER_MIN_TM': 57.0,
        'PRIMER_MAX_TM': 63.0,
        'PRIMER_MIN_GC': 20.0,
        'PRIMER_MAX_GC': 80.0,
        'PRIMER_MAX_POLY_X': 100,
        'PRIMER_INTERNAL_MAX_POLY_X': 100,
        'PRIMER_SALT_MONOVALENT': 50.0,
        'PRIMER_DNA_CONC': 50.0,
        'PRIMER_MAX_NS_ACCEPTED': 0,
        'PRIMER_MAX_SELF_ANY': 12,
        'PRIMER_MAX_SELF_END': 8,
        'PRIMER_PAIR_MAX_COMPL_ANY': 12,
        'PRIMER_PAIR_MAX_COMPL_END': 8,
        'PRIMER_PRODUCT_SIZE_RANGE': [
            [75, 100], [100, 125], [125, 150],
            [150, 175], [175, 200], [200, 225]
        ],
    }
)



print(f"{'Left primer':<24} {'Right primer':<20}")

for i in range(len(results["PRIMER_PAIR"])):
    left = results[f"PRIMER_LEFT_{i}_SEQUENCE"]
    right = results[f"PRIMER_RIGHT_{i}_SEQUENCE"]
    print(f"{left:<20} {'--'} {right:<20}")
