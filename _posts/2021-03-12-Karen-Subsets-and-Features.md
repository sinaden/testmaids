


  
<style> th { padding: 7px;} .markdown-body { max-width:1400px} </style>

Bellow the subsets and their corresponding features are presented.  
**Subset 1**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|1|MADS_data||TABULAR|CSV||0|The positive/negative blood culturing results are essentieal for the prediction of blood stream infections||
  
  
  
*Features of Subset 1*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pID|1||0..inf; integer|Not possible in format.|No zeros|Not possible in format.|||pseudonymised identifier||none|
|sex|2||M/K|Not possible in format.|No zeros|Not recorded or lost.|||gender|Risk of infection couæld be associated with gender|none|
|age|3||positive number with decimals|No NA, NULL, or NONE|Zero years since birth have passed.|Not possible in format.||years|age when blood culturing was requested|Risk of infection couæld be associated with age|none|
|sender|4||text, example, 2124C1|No NA, NULL, or NONE|No zeros|Not recorded or lost.|||Department who requested the sampling|could be associated to BSI|none|
|date_received|5||date, format: 16-06-2019|No NA, NULL, or NONE|No zeros|Not possible in format.|||Date the sample was received at KMA|imporant for matching with LABKA data|none|
|date_answered|6||date, format: 16-06-2019|No NA, NULL, or NONE|No zeros|Not recorded or lost.|||Date the sample was answered at KMA|imporant for matching with LABKA data|none|
|sample_type|7||text, list of samples|No NA, NULL, or NONE|No zeros|Not possible in format.|||Type of sample|this could be important for prediction of BSI|none|
|sample_anatomi|8||text|No NA, NULL, or NONE|No zeros|Not recorded or lost.|||Additional information on sampling, e.g. how or shere the blood sample was taken anatomically|this could be important for prediction of BSI|none|
|bacteria|9||text, microbial species or family, Ingen vækst|No NA, NULL, or NONE|zero means no bacteria/fungi detected|Not recorded or lost.|||Which, if any, microbe was detected in the sample|important for prediction of BSI|encoded|
|bacteria_amount|10||1/2, 2/2, 4/5, 1/5, +, ++, +++, 100000, 10000, >100000|No NA, NULL, or NONE|No zeros|Not recorded or lost.||proportion|positive flasks of total number of flasks|important for prediction of BSI|none|
  
  
**Subset 2**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|2|admission_data||TABULAR|CSV||0|This data informs us of when the patient was admitted and is relevant for filtering the clinical blood values to only iclude the ones relavant for the BSI. Additionally, previous admissions can be predictive for BSI development||
  
  
  
*Features of Subset 2*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|admission_department|11||1301XXX, where X represents number or letters|Not possible in format.|No zeros|Not possible in format.|||Admission|could be correlated to BSI risk and focus of infection|encoded|
|admission_start_date|12||date, format: 30JAN2019|Not possible in format.|No zeros|Not possible in format.|||admission start date|indicates hospital and disease history which could predict BSI|none|
|admission_end_date|13||date, format: 30JAN2019|Not possible in format.|No zeros|Not possible in format.|||admission end date|indicates hospital and disease history which could predict BSI|none|
|ICD10_diagnose_codes|14||D followed by 3-6 numbers/letters: DXXXXXX|Not possible in format.|No zeros|Not possible in format.|||diagnose codes|previous and current disease which could predict risk of bacteriaemia|encoded|
  
  
**Subset 3**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|3|labka_data||TABULAR|CSV||0|The clinical blood values are important for the prediction of BSI||
  
  
  
*Features of Subset 3*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|CRP|15||positive number or <5|Not possible in format.|No zeros|Not recorded||mg/L|concentration of CRP in blood|immuneresponse therefore important|none|
|leuusp|16||positive number with decimals or <number|Not possible in format.|No zeros|Not recorded||× 109/L|number of leukocyttes in blood|immuneresponse therefore important|none|
|PROCAL|17||positive number with decimals|Not possible in format.|No zeros|Not recorded||µg/L|procalcitonin concentration in blood|marker of inflamation|none|
|kbdeoxhb|18||positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|haemoglobin content in blood|indicator of bonemarrow function and chronic disease|none|
|CSVERY|19||positive number or <number|Not possible in format.|No zeros|Not recorded||× 109/L|number of erytrocytes in blood|indicator of bonemarrow function and chronic disease|none|
|lymfopoc|20||positive number or <number|Not possible in format.|No zeros|Not recorded||× 109/L|number of lymfocytes in blood|immuneresponse therefore important|none|
|HAPTO|21||positive number with decimals|Not possible in format.|No zeros|Not recorded||g/L|concentration of haptoglobin in blood|indicator of inflammation|none|
|ABKPOC|22||positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of kalium in blood|indicator of kidneyfunction and infection|none|
|ABNAPOC|23||positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of natrium in blood|indicator of kidneyfunction and infection|none|
|eGFR|24||positive number with decimals|Not possible in format.|No zeros|Not recorded||mL/min|estimated glomerular filtration rate|indicator of kidney function|none|
|DICAIAK|25||positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of free calcium|indicator of systemic inflammation|none|
|BCLPOC|26||positive number with decimals|Not possible in format.|No zeros|Not recorded||mmol/L|concentration of chloride in blood|indicator of systemic inflammation|none|
|neutropoc|27||positive number or <number|Not possible in format.|No zeros|Not recorded||× 109/L|number of neutrofils in blood|indicator of viral and bacterial infection|none|
|leuusp|28||positive number or <number|Not possible in format.|No zeros|Not recorded||× 109/L|number of leukocytes in blood|immuneresponse therefore important|none|
|THROMEX|29||positive number or <number|Not possible in format.|No zeros|Not recorded||× 109/L|number of trombocytes in blood|marker of inflamation|none|
|GLUFK|30||positive number with decimals|Not possible in format.|No zeros|Not possible in format.||mmol/L|concentration of glukose in blood|indicator of general health|none|
|sampling_date_time|31||date and time|No NA, NULL, or NONE|No zeros|Not possible in format.|||date sample was requested in Labka|important in order to match with MADS data|none|
|date_answered|32||date and time|Not possible in format.|No zeros|Not possible in format.|||date sample was answered in labka|important in order to match with MADS data|none|
|Requestercode|33||text - list of items|No NA, NULL, or NONE|No zeros|Not possible in format.|||who requested the analysis|could be associated to BSI|encoded|
|analysis_code|34||text - list of items|No NA, NULL, or NONE|No zeros|Not possible in format.|||code of the performed analysis|important for structuring of the data|encoded|
|system|35||text - list of items|No NA, NULL, or NONE|No zeros|Not possible in format.|||which system the analyses was performed in|important for structuring of the data|encoded|
|component|36||text - list of items|No NA, NULL, or NONE|No zeros|Not possible in format.|||which component performed the analyses|important for structuring of the data|encoded|
|reply_unit|37||text|No NA, NULL, or NONE|No zeros|No unit for reply|||unit which received the answer|could be associated to BSI|encoded|
  
