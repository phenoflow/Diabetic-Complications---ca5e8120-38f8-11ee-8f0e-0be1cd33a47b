# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"C107.11","system":"readv2"},{"code":"C109511","system":"readv2"},{"code":"C109512","system":"readv2"},{"code":"C10E600","system":"readv2"},{"code":"C10E611","system":"readv2"},{"code":"C10F500","system":"readv2"},{"code":"C10F511","system":"readv2"},{"code":"R054200","system":"readv2"},{"code":"R054300","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetic-complications-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetic-complications-gangrene---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetic-complications-gangrene---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetic-complications-gangrene---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
