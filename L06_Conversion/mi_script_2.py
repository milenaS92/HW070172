import re
import yaml

"""
1. load bibtex file
    - bibliography should be curated in Zotero (one can program cleaning procedures into the script, but this is not as reliable);
    - loading bibtex data, keep only those records that have PDFs;
    - some processing might be necessary (like picking one file out of two and more)
2. convert into other formats
    - csv
    - json
    - yml
"""

###########################################################
# VARIABLES ###############################################
###########################################################
#file with the name of 3 bib files, in a dict format
#settingsFile = "z_config.yml"
settingsFile = "mi_config.yml"
#load the bib options in a dictionary (vars)
settings = yaml.load(open(settingsFile))
#bibKeys = yaml.load(open("zotero_biblatex_keys.yml"))
bibKeys = yaml.load(open("mi_clean_bib.yml"))

###########################################################
# FUNCTIONS ###############################################
###########################################################

# load bibTex Data into a dictionary
def bibLoad(bibTexFile):
    # empty dictionary
    bibDic = {}
    #open and read bibTeXFile, split records
    with open(bibTexFile, "r", encoding="utf8") as f1:
        records = f1.read().split("\n@")
        #for every record
        for record in records[1:]:
            # let process ONLY those records that have PDFs
            if ".pdf" in record.lower():
                #make a list of the lines of each record
                record = record.strip().split("\n")[:-1]
                # save data from the first line (@line) in 2 variables
                rType = record[0].split("{")[0].strip()
                rCite = record[0].split("{")[1].strip().replace(",", "")
                #make a (sub)dictionary for each record
                bibDic[rCite] = {}
                #save data from the record's first line as values
                #in the (sub)dictionary
                bibDic[rCite]["rCite"] = rCite
                bibDic[rCite]["rType"] = rType
                #for each of the resting lines of each record
                for r in record[1:]:
                    #save keys and values as variables
                    key = r.split("=")[0].strip()
                    val = r.split("=")[1].strip()
                    print("VAL: ",val)
                    #val = re.sub(".\{|\},?", "", val)
                    val  = re.sub("[{},]","",val) #delete unnedeed chars
                    #for ch in val:
                    #    if ch in "{},":
                    #        val = val.replace(ch,"")
                    print("VAL: ",val)
                    #save fixed keys in variable (dict from yaml file)
                    fixedKey = bibKeys[key]
                    #save (fixed) keys and values in the dictionary
                    bibDic[rCite][fixedKey] = val

    #print number of recrods
    print("="*80)
    print("NUMBER OF RECORDS IN BIBLIGORAPHY: %d" % len(bibDic))
    print("="*80)
    #return dictionary
    return(bibDic)

# CONVERSION FUNCTIONS
#convert bib file to json file
import json
def convertToJSON(bibTexFile):
    #load data into dictionary
    data = bibLoad(bibTexFile)
    #open file and change extension
    with open(bibTexFile.replace(".bib", ".json"), 'w', encoding='utf8') as f9:
        #write data from dictionary into the new json file
        json.dump(data, f9, sort_keys=True, indent=4, ensure_ascii=False)

#convert bib file to yaml file
import yaml
def convertToYAML(bibTexFile):
    #load data into dictionary
    data = bibLoad(bibTexFile)
    #open file and change extension
    with open(bibTexFile.replace(".bib", ".yaml"), 'w', encoding='utf8') as f9:
        #write data from dictionary into the new yaml file
        yaml.dump(data, f9)

#convert bib file to csv file
# CSV is the trickest because bibTeX is not symmetrical
def convertToCSV(bibTexFile):
    #load data into dictionary
    data = bibLoad(bibTexFile)
    # let's handpick fields that we want to save: citeKey, type, author, title, date
    headerList = ['citeKey', 'type', 'author', 'title', 'date']
    #create a string with the field names, separated by tabs
    header = "\t".join(headerList)
    #save string as first element of a new list
    dataNew = [header]

    for k,v in data.items():
        citeKey = k
        #save the field values in variables
        if 'rType' in v:
            rType = v['rType']
        else:
            rType = "NA"

        if 'author' in v:
            author = v['author']
        else:
            author = "NA"

        if 'title' in v:
            title = v['title']
        else:
            title = "NA"

        if 'date' in v:
            date = v['date']
        else:
            date = "NA"
        #use the variables to make a string, separated by tabs
        tempVal = "\t".join([citeKey, rType, author, title, date])
        #add string to list
        dataNew.append(tempVal)
    # join all the strings(records) into one long string, separated by \n
    finalData = "\n".join(dataNew)
    #open file, change extension and paste the final string
    with open(bibTexFile.replace(".bib", ".csv"), 'w', encoding='utf8') as f9:
        f9.write(finalData)


###########################################################
# RUN EVERYTHING ##########################################
###########################################################

print(settings["bib_all"])

#convertToJSON(settings["bib_all"])
#convertToYAML(settings["bib_all"])
#convertToCSV(settings["bib_all"])


print("Done!")
