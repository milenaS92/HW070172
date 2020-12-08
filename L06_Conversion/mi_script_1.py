import os, yaml

###########################################################
# VARIABLES ###############################################
###########################################################

#file with the name of 3 bib files, in a dict format
settingsFile = "yaml_cp.yml"
#load the bib options in a dictionary (vars)
vars = yaml.load(open(settingsFile))

###########################################################
# FUNCTIONS ###############################################
###########################################################

# analyze bibTeX data; identify what needs to be fixed
def bibAnalyze(bibTexFile):
    #create empty dictionary
    tempDic = {}
    #open and read bibTeXFile, split records
    with open(bibTexFile, "r", encoding="utf8") as f1:
        records = f1.read()
        records = records.split("\n@")
        #for every record
        for record in records[1:]:
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower():
                record = record.strip()
                #make a list of the lines of each record
                record = record.split("\n")[:-1] #leave last char out
                #process every line execpt the first (the @line)
                for r in record[1:]:
                    #save in r the first element of each line e.g. 'title'
                    r = r.split("=")[0].strip()
                    #make a frequency list of the elements in tempDic
                    if r in tempDic:
                        tempDic[r] += 1
                    else:
                        tempDic[r] = 1
    #create an empty list
    results = []
    #save the frequency list (tempDic) in the list
    for k,v in tempDic.items():
        result = "%010d\t%s" % (v, k)
        results.append(result)
    #sort the list from higher to lower frequency
    results = sorted(results, reverse=True)
    #make a string of everything with /n as the separator
    results = "\n".join(results)
    #write the results in a new file
    with open("bibtex_analysis.txt", "w", encoding="utf8") as f9:
        f9.write(results)
#call function, select the name of the file from the yaml file
bibAnalyze(vars['bib_all'])
