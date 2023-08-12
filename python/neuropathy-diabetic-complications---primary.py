# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"C106.12","system":"readv2"},{"code":"C106.13","system":"readv2"},{"code":"C108B00","system":"readv2"},{"code":"C108B11","system":"readv2"},{"code":"C108C00","system":"readv2"},{"code":"C108J11","system":"readv2"},{"code":"C108J12","system":"readv2"},{"code":"C109A00","system":"readv2"},{"code":"C109A11","system":"readv2"},{"code":"C109B00","system":"readv2"},{"code":"C109B11","system":"readv2"},{"code":"C109H00","system":"readv2"},{"code":"C109H11","system":"readv2"},{"code":"C109H12","system":"readv2"},{"code":"C10EB00","system":"readv2"},{"code":"C10EC00","system":"readv2"},{"code":"C10EC11","system":"readv2"},{"code":"C10EC12","system":"readv2"},{"code":"C10EJ00","system":"readv2"},{"code":"C10FA00","system":"readv2"},{"code":"C10FA11","system":"readv2"},{"code":"C10FB00","system":"readv2"},{"code":"C10FB11","system":"readv2"},{"code":"C10FH00","system":"readv2"},{"code":"C10FH11","system":"readv2"},{"code":"F372.11","system":"readv2"},{"code":"F372.12","system":"readv2"},{"code":"F372200","system":"readv2"},{"code":"F3y0.00","system":"readv2"},{"code":"M271100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetic-complications-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["neuropathy-diabetic-complications---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["neuropathy-diabetic-complications---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["neuropathy-diabetic-complications---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
