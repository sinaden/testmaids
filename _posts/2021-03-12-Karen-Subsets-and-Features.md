


  
<style> th { padding: 7px;} .markdown-body { max-width:1400px} </style>

Bellow the subsets and their corresponding features are presented.  
**Subset 1**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|1|MADS_data||TABULAR|CSV||0|The positive/negative blood culturing results are essentieal for the prediction of blood stream infections||
  
  
  
*Features of Subset 1*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pID|1|MADS_data|0..inf; integer|Not possible in format.|No zeros|Not possible in format.|||pseudonymised identifier|||
|sex|2|MADS_data|M/K|Not possible in format.|No zeros|Not recorded or lost.|||gender|Gender could be associated to BSI||
|age|3|MADS_data|positive number with decimals|No NA, NULL, or NONE|Zero years since birth have passed.|Not possible in format.||years|age when blood culturing was requested|Age could be associated to BSI||
|sender|4|MADS_data|text, example, 2124C1|No NA, NULL, or NONE|No zeros|Not recorded or lost.|||Department who requested the sampling|Risk of BSI could be associated to department of admission||
|date_received|5|MADS_data|date, format: 16-06-2019|No NA, NULL, or NONE|No zeros|Not possible in format.|||Date the sample was received at KMA|This info is used to combine the datasets so relevant blood values are mapped to the relevant blood culturing sample||
|date_answered|6|MADS_data|date, format: 16-06-2019|No NA, NULL, or NONE|No zeros|Not recorded or lost.|||Date the sample was answered at KMA|This info is used to combine the datasets so relevant blood values are mapped to the relevant blood culturing sample||
|sample_type|7|MADS_data|text, list of samples|No NA, NULL, or NONE|No zeros|Not possible in format.|||Type of sample|Could be correlated to how good the prediction is||
|sample_anatomi|8|MADS_data|text|No NA, NULL, or NONE|No zeros|Not recorded or lost.|||Additional information on sampling, e.g. how or shere the blood sample was taken anatomically|Could be correlated to how good the prediction is||
|bacteria|9|MADS_data|text, microbial species or family, Ingen vækst|No NA, NULL, or NONE|zero means no bacteria/fungi detected|Not recorded or lost.|||Which, if any, microbe was detected in the sample|The species is highly correlated to severity of infection|encoded|
|bacteria_amount|10|MADS_data|1/2, 2/2, 4/5, 1/5, +, ++, +++, 100000, 10000, >100000|No NA, NULL, or NONE|No zeros|Not recorded or lost.||proportion|positive flasks of total number of flasks|This parameter in combination with the identified species could indicate severity of infection, although this is pooprly described to date.||
  
  
**Subset 2**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|2|admission_data||TABULAR|CSV||0|This data informs us of when the patient was admitted and is relevant for filtering the clinical blood values to only iclude the ones relavant for the BSI. Additionally, previous admissions can be predictive for BSI development||
  
  
  
*Features of Subset 2*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|admission_department|11|admission_data|1301XXX, where X represents number or letters|Not possible in format.|No zeros|Not possible in format.|||Admission|could be correlated to BSI risk and focus of infection|encoded|
|admission_start_date|12|admission_data|date, format: 30JAN2019|Not possible in format.|No zeros|Not possible in format.|||admission start date|Illustrates previous and current admissions and duration of admission||
|admission_end_date|13|admission_data|date, format: 30JAN2019|Not possible in format.|No zeros|Not possible in format.|||admission end date|Illustrates previous and current admissions and duration of admission||
|ICD10_diagnose_codes|14|admission_data|D followed by 3-6 numbers/letters: DXXXXXX|Not possible in format.|No zeros|Not possible in format.|||diagnose codes|previous and current disease which could predict risk of bacteriaemia|encoded|
  
  
**Subset 3**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|3|labka_blood_parameters||TABULAR|CSV||0|The clinical blood values are important for the prediction of BSI||
  
  
  
*Features of Subset 3*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|CRP|15|labka_blood_parameters|CRP positive number or <1|Not possible in format.|No zeros|Not recorded||mg/L|concentration of CRP in blood|central indicator of immune response||
|LEU|16|labka_blood_parameters|positive number with decimals or <0.01|Not possible in format.|No zeros|Not recorded||× 109/L|number of leukocyttes in blood|central indicator of immune response||
|PROCAL|17|labka_blood_parameters|positive number with decimals or <0.06|Not possible in format.|No zeros|Not recorded||µg/L|procalcitonin concentration in blood|marker of inflamation||
|HB|18|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|haemoglobin concentration in blood|indicator of bonemarrow function and chronic disease||
|ERY|19|labka_blood_parameters|positive number or <0.09|Not possible in format.|No zeros|Not recorded||× 109/L|number of erytrocytes in blood|indicator of bonemarrow function and chronic disease||
|LYMFO|20|labka_blood_parameters|positive number |Not possible in format.|Zero means no lymfocytes measured|Not recorded||× 109/L|number of lymfocytes in blood|immuneresponse therefore important||
|HAPTO|21|labka_blood_parameters|positive number with decimals or <0.1|Not possible in format.|No zeros|Not recorded||g/L|concentration of haptoglobin in blood|indicator of inflammation||
|K|22|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of kalium in blood|indicator of kidneyfunction and infection||
||23|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of natrium in blood|indicator of kidneyfunction and infection||
|eGFR|24|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mL/min|estimated glomerular filtration rate|indicator of kidney function||
|CAI|25|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of ionized calcium|indicator of systemic inflammation||
|CL|26|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of chloride in blood|indicator of systemic inflammation||
|NEUTRO|27|labka_blood_parameters|positive number with decimals|Not possible in format.|Zero means no netrofilocytes measured|Not recorded||× 109/L|number of neutrofils in blood|indicator of viral and bacterial infection||
|THROM|28|labka_blood_parameters|positive number or <3|Not possible in format.|No zeros|Not recorded||× 109/L|number of trombocytes in blood|marker of inflamation||
|GLU|29|labka_blood_parameters|positive number with decimals or <0.11|Not possible in format.|No zeros|Not possible in format.||mmol/L|concentration of glukose in blood|indicator of general health||
|BASO|30|labka_blood_parameters|positive number |Not possible in format.|No zeros|Not recorded||× 109/L|number of basofilocytes in blood|infection parameter||
|EOS|31|labka_blood_parameters|positive number |Not possible in format.|No zeros|Not recorded||× 109/L|number of eosinofilocytes in blood|infection parameter||
|MONO|32|labka_blood_parameters|positive number |Not possible in format.|No zeros|Not recorded||× 109/L|number of monocytes in blood|infection parameter||
|JERN|33|labka_blood_parameters|positive number with decimals OR <1|Not possible in format.|No zeros|Not recorded||µmol/L|concentration of free iron in blood|illustrator of the general blod status||
|FERRITIN|34|labka_blood_parameters|positive number with decimals OR <2|Not possible in format.|No zeros|Not recorded||µg/L|ferritin concentration in blood|illustrator of the general blod status||
|TRANS|35|labka_blood_parameters|positive number with decimals OR <0.1|Not possible in format.|No zeros|Not recorded||g/L|transferin concentration in blood|illustrator of the general blod status||
|CA |36|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of free calcium in blood|indicator of general health of the patient and comorbidities. Often Ca is low in critically ill patients||
|MG|37|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of magnesium in blood|non-specific indicator of general health of the patient||
|GLUF|38|labka_blood_parameters|positive number with decimals or <0.11|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of glukose in blood fasting|Indicator of comorbidities incl. Diabetes, during infection stress response can induce higher glukose levels.||
|LDL|39|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of LDL cholesterol in blood|illustrator of lipid levels in blood||
|HDL|40|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of HDL cholesterol in blood|illustrator of lipid levels in blood||
|CHOL|41|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of cholesterol in blood|illustrator of lipid levels in blood||
|TRIG|42|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of trigyceride in blood|illustrator of lipid levels in blood||
|ALB|43|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||g/L|concentration of albumin in blood|illustrator of liver function||
|LDH|44|labka_blood_parameters|positive number with decimals or <10|Not possible in format.|No zeros|Not recorded||U/L|concentration of Lactate dehydrogenase in blood|illustrator of liver function||
|ALAT|45|labka_blood_parameters|positive number with decimals or <5|Not possible in format.|No zeros|Not recorded||U/L|concentration of Alanintransaminase in blood|illustrator of liver function||
|GGT|46|labka_blood_parameters|positive number with decimals or <3|Not possible in format.|No zeros|Not recorded||U/L|concentration of gamma-Glutamyltransferase in blood|illustrator of liver function||
|TSH|47|labka_blood_parameters|positive number with decimals or <0.01|Not possible in format.|No zeros|Not recorded||× 103 IU/L|concentration of Thyrotropin in blood|indicator of endeocrine disfunction||
|HBA1C|48|labka_blood_parameters|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/mol|fraction of haemoglobin A with glucose irreversible attached |indicator of endeocrine disfunction||
|INR|49|labka_blood_parameters|positive number with decimals or <0.9 or >4.5|Not possible in format.|No zeros|Not recorded||no unit|coagulation factor II + VII + X|indicator of coagulation function||
|APTT|50|labka_blood_parameters|positive number with decimals or <20 or >240|Not possible in format.|No zeros|Not recorded||s|P-coagulation, surface induced|indicator of coagulation function||
|sampling_date_time|51|labka_blood_parameters|date and time, format: DD-MM-YYYY HH24:MI:SS|No NA, NULL, or NONE|No zeros|Not possible in format.|||date sample was requested in Labka|This info is used to combine the datasets so relevant blood values are mapped to the relevant blood culturing sample||
|date_answered|52|labka_blood_parameters|date and time, format: DD-MM-YYYY HH24:MI:SS|Not possible in format.|No zeros|Not possible in format.|||date sample was answered in labka|This info is used to combine the datasets so relevant blood values are mapped to the relevant blood culturing sample||
|Requestercode|53|labka_blood_parameters|text, example, 2124C1(RH), similar code as MADS_data:sender|No NA, NULL, or NONE|No zeros|Not possible in format.|||Department who requested the sampling|Risk of BSI could be associated to department of admission|encoded|
  
  
**Subset 4**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|4|labka_blood_parameters_poct||TABULAR|CSV||0|The clinical blood values are important for the prediction of BSI. The POCT are requested alone or in combination with analyses in subset 3||
  
  
  
*Features of Subset 4*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|HBPOC|54|labka_blood_parameters_poct|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|haemoglobin concentration in blood|indicator of bonemarrow function and chronic disease||
|KPOC|55|labka_blood_parameters_poct|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of kalium in blood|indicator of kidneyfunction and infection||
|HSCRP|56|labka_blood_parameters|HSCRP - high sensitive CRP (feature 15) is a more sensitive measurement in the low range of CRP, positive number with decimals <0.30 or >20. Either CRP or HSCRP should have been measured at any given time, never both.|Not possible in format.|No zeros|Not recorded||mg/L|concentration of CRP in blood|central indicator of immune response||
|CLPOC|57|labka_blood_parameters_poct|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of chloride in blood|indicator of systemic inflammation||
|CAIPOC|58|labka_blood_parameters_poct|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of ionized calcium|indicator of systemic inflammation||
|NAPOC|59|labka_blood_parameters_poct|positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of natrium in blood|indicator of kidneyfunction and infection||
|GLUPOC|60|labka_blood_parameters_poct|positive number with decimals or <0.11|Not possible in format.|No zeros|Not possible in format.||mmol/L|concentration of glukose in blood|indicator of general health||
|sampling_date_time|61|labka_blood_parameters_poct|date and time, format: DD-MM-YYYY HH24:MI:SS|No NA, NULL, or NONE|No zeros|Not possible in format.|||date sample was requested in Labka|This info is used to combine the datasets so relevant blood values are mapped to the relevant blood culturing sample||
|date_answered|62|labka_blood_parameters_poct|date and time, format: DD-MM-YYYY HH24:MI:SS|Not possible in format.|No zeros|Not possible in format.|||date sample was answered in labka|This info is used to combine the datasets so relevant blood values are mapped to the relevant blood culturing sample||
|Requestercode|63|labka_blood_parameters_poct|text, example, 2124C1(RH), similar code as MADS_data:sender (feature 4) and requestercode (feature 53)|No NA, NULL, or NONE|No zeros|Not possible in format.|||Department who requested the sampling|Risk of BSI could be associated to department of admission|encoded|
  
