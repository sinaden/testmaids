from xml.etree import ElementTree

import xml.etree.cElementTree as ET
import pandas as pd

from mdutils.mdutils import MdUtils
from datetime import datetime

def xstr(s):
    if s is None:
        return ''
    return str(s)

def create_markdown(out_df, xmltitle ):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d-"+xmltitle+"-Subsets-and-Features")
    
    mdFile = MdUtils(file_name="../_posts/"+dt_string)



    
    mdFile.new_line("<style> th { padding: 7px;} .markdown-body { max-width:1400px} </style>")
    mdFile.new_paragraph("Bellow the subsets and their corresponding features are presented.")

    for i in range(len(out_df.ID)):
        #print("hhh" + out_df.ID[i] + " " + out_df.Name[i] + " " + out_df.Name[i]
       #   + " " + out_df['Last Update'][i] + " " + out_df.Modality[i] + " " + out_df.Format[i] + " " + out_df.Size[i])
        
        list_of_strings = ["ID", "Name", "Last Update", "Modality","Format","Size", "Parent","Purpose","Link"]
        #print(list_of_strings)
        mdFile.new_line("Subset " +str(i + 1), bold_italics_code='b', align='left')
        mdFile.new_line()
        
        
        list_of_strings.extend([xstr(out_df.ID[i]), xstr(out_df.Name[i]), xstr(out_df['Last Update'][i]),
                                xstr( out_df.Modality[i]) , xstr(out_df.Format[i]), xstr(out_df.Size[i]),
                                xstr(out_df.Parent[i]), xstr(out_df.Purpose[i]), xstr(out_df.Link[i])])
        #print(list_of_strings)
        mdFile.new_line()
        mdFile.new_table(columns=9, rows=2, text=list_of_strings)

        mdFile.new_line()

        #features_list_of_strings = ["Name","ID", "Date of Intro","Values","Meaning of Nan","Meaning of Zero","Meaning of blankvoid", "Sparsity","Mean","std","Modality","Median","IQR","Parents","Unit","Definition","Purpose","Encoding"]
        features_list_of_strings = ["Name","ID", "Date of Intro","Values","Meaning of Nan","Meaning of Zero","Meaning of blankvoid","Parents","Unit","Definition","Purpose","Encoding"]

        
        #{"f_name": f_name, "f_id": f_id, "f_date_of_introduction" : f_date, "f_values": f_val, 
         #              "f_mean_nan": f_nan, "f_mean_zero": f_zero, "f_mean_blankvoid": f_bl, "f_sparsity": f_spa, "f_mean": f_mean,
          #             "f_std": f_std, "f_modality": f_modality, "f_median": f_med, "f_iqr": f_iqr, "f_parents": f_par,
           #            "f_unit": f_un, "f_definition": f_def, "f_purpose": f_pu, "f_encoding": f_en})
            
        numberof_features = len(out_df.Features[i])

        for k in range(numberof_features):

            #print(features_list_of_strings)   
            tdic = out_df.Features[i][k] 
            
            for key, v in tdic.items():
                if v is None:
                    tdic[key] = ""
            
            features_list_of_strings.extend([tdic.get("f_name", ""), 
                                    
                                        tdic.get("f_id", ""), 
                                    
                               tdic.get("f_date_of_introduction", ""), 
                                    
                                    tdic.get("f_values", ""), 
                                    
                                        tdic.get("f_mean_nan",""), 
                                    
                               tdic.get("f_mean_zero", ""), 
                                    
                                    tdic.get("f_mean_blankvoid", ""), 
                                    
                               #         tdic.get("f_sparsity", ""), 
                                    
                              # tdic.get("f_mean",  ""), 
                                    
                               #     tdic.get("f_std", ""), 
                                    
                                #        tdic.get("f_modality",  ""), 
                                    
                              # tdic.get("f_median",  ""), 
                                    
                               #     tdic.get("f_iqr", ""), 
                                    
                                        tdic.get("f_parents", ""), 
                                    
                               tdic.get("f_unit",  ""), 
                                    
                                    tdic.get("f_definition", ""), 
                                    
                                        tdic.get("f_purpose", ""), 
                                    
                               tdic.get("f_encoding", "")])
            
    
        #print(features_list_of_strings)   
        mdFile.new_line()
        if numberof_features != 0:
            mdFile.new_line("Features of Subset " +str(i + 1), bold_italics_code='i', align='left')
            mdFile.new_line()
            mdFile.new_table(columns=12, rows=numberof_features+1, text=features_list_of_strings)
            mdFile.new_line()
    mdFile.create_md_file()



#Run this instead of bulding it from scratch
#main_root = xml.etree.ElementTree.parse("subsets_features_test.xml")

xml_file = ET.parse("../xmls/subsetfeature.xml")
ghxml = xml_file.getroot()
xmltitle = ghxml.attrib.get("name")

sfd = ghxml.find('Subset_Feature_Dataset')

df_cols = ["ID", "Name", "Last Update","Modality","Format","Size","Parent","Purpose","Link", "Features"]
rows = []



print("______________________________________")
print("_________O000000000000000O________________")
print("__________\-----_-------/______________")
print("___________\-----------/_________")
print("____________\---------/_________")
print("_____________\-------/____")
print("______________\-----/___")
print("_______________\---/___")
print("________________\-/___")
print("_________________:___")
print("________________The xml file was found, it was filled by " + xmltitle + " __________")

print("______________________________________")
print("______________________________________")
print("______________________________________")
print("______________________________________")
print("______________________________________")


for subset in sfd:
    #print(subset.attrib.get("name"))
    
    _id = subset.find("A0").text
    name = subset.find("A1").text
    lu = subset.find("A2").text
    mod = subset.find("A3").text
    fmt = subset.find("A4").text
    sz = subset.find("A5").text
    parent = subset.find("A6").text
    purp = subset.find("A7").text
    lnk = subset.find("A8").text
    
    fs = subset.find("Features")
    
    #print(name + " " + _id + " " + lu)
    #print("Features")
    
    f_rows = []
    for feature in fs:
        f_id = feature.find("A0").text
                            # A1 is not needed, we already know the subset due to xml's architecture. 
        f_date = feature.find("A2").text
        f_name = feature.find("A3").text
        f_val = feature.find("A4").text
        f_nan = feature.find("A5").text
        
        f_zero = feature.find("A6").text
        f_bl = feature.find("A7").text
        f_spa = feature.find("A8").text
        f_mean = feature.find("A9").text
        f_std = feature.find("A10").text
        
        f_modality = feature.find("A11").text
        f_med = feature.find("A12").text
        f_iqr = feature.find("A13").text
        f_par = feature.find("A14").text
        
        f_un = feature.find("A15").text
        f_def = feature.find("A16").text
        f_pu = feature.find("A17").text
        f_en = feature.find("A18").text
        print("\t" + f_id + " " + f_name)
        
        f_rows.append({"f_name": f_name, "f_id": f_id, "f_date_of_introduction" : f_date, "f_values": f_val, 
                       "f_mean_nan": f_nan, "f_mean_zero": f_zero, "f_mean_blankvoid": f_bl, "f_sparsity": f_spa, "f_mean": f_mean,
                       "f_std": f_std, "f_modality": f_modality, "f_median": f_med, "f_iqr": f_iqr, "f_parents": f_par,
                       "f_unit": f_un, "f_definition": f_def, "f_purpose": f_pu, "f_encoding": f_en})
        
    rows.append({"ID": _id, "Name": name, "Last Update": lu,"Modality":mod,"Format":fmt,"Size":sz,"Parent":parent,
                 "Purpose":purp,"Link":lnk, "Features": f_rows})

out_df = pd.DataFrame(rows, columns = df_cols)



print("______________________________________")
print("_________O000000000000000O________________")
print("__________\-----_-------/______________")
print("___________\-----------/_________")
print("____________\---------/_________")
print("_____________\-------/____")
print("______________\-----/___")
print("_______________\---/___")
print("________________\-/___")
print("_________________:___")
print("________________Dataframe created, create_markdown is called_________")


create_markdown(out_df,xmltitle)
print("______________________________________")
print("_________O000000000000000O________________")
print("__________\-------------/______________")
print("___________\-----------/_________")
print("____________\---------/_________")
print("_____________\-------/____")
print("______________\-----/___")
print("_______________\---/___")
print("________________\-/___")
print("_________________:___")
print("________________Finish!______________")

print("________________Post was created under _posts folder___________")
print("______________________________________")
print("______________________________________")
print("______________________________________")
print("______________________________________")
print("______________________________________")
print("______________________________________")