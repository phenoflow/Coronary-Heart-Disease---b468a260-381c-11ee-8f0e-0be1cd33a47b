# Evangelos Kontopantelis, David Springate, David Reeves, Darren M Ashcroft, Jose M Valderas, Tim Doran, 2023.

import sys, csv, re

codes = [{"code":"G311.11","system":"readv2"},{"code":"G311.14","system":"readv2"},{"code":"G311200","system":"readv2"},{"code":"G311300","system":"readv2"},{"code":"G330000","system":"readv2"},{"code":"G331.00","system":"readv2"},{"code":"G33z300","system":"readv2"},{"code":"G33z600","system":"readv2"},{"code":"4139AT","system":"oxmis"},{"code":"4139C","system":"oxmis"},{"code":"4139CO","system":"oxmis"},{"code":"4139M","system":"oxmis"},{"code":"4139N","system":"oxmis"},{"code":"4139PA","system":"oxmis"},{"code":"4139U","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('coronary-heart-disease-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["coronary-heart-disease-angina---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["coronary-heart-disease-angina---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["coronary-heart-disease-angina---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
