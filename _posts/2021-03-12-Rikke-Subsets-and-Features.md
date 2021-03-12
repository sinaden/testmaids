


  
<style> th { padding: 7px;} </style>

Bellow the subsets and their corresponding features are presented.  
**Subset 1**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|1|ptdata92|28/1 2020|TABULAR|sav|538|0|NOPHO ALL-92, patient cohort with background information. Follow-up until 20.04.04||
  
  
  
*Features of Subset 1*
|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PTNR|1|1/28/2020|Unique patient identifier character|Not possible in format.|None recorded |None recorded ||||||||None|Unique patient identifier character|Unique patient identifier character||
|MTDURATION|2|1/28/2020|[115-1049];integer|Not possible in format.|None recorded |None recorded ||||||||Days|MTSLUT - MTSTART|defines length of maintenanace therapy|Numeric|
|CENSDAYS|3|1/28/2020|[0-1495];integer|no censoring dates receorded|None recorded |no censoring dates receorded||||||||Days|Number of days until censtoring from start of maintainence therapy|Censoring|Numeric|
|CENGRUND|4|1/28/2020|[0-10];Integer |Not possible in format.|No censoring|None recorded ||||||||None|Reason for censoring|Reason for censoring|Categorial|
|RANDOM|5|1/28/2020|K/S|Not possible in format.|None recorded |None recorded ||||||||None|Randomisation group of maintenance therapy||Categorical|
|RISIKOGP|6|1/28/2020|HR /  IR /  SR|Not possible in format.|None recorded |None recorded ||||||||None|Treatment risk group, SR= stnadard risk, IR = intermediate risk, HR = high risk|Treatment risk group, SR= stnadard risk, IR = intermediate risk, HR = high risk|Categorical|
|RECTIME|7|1/28/2020|[115-4129]; integer|No relapse|None recorded |No relapse||||||||Days|Time to relapse from start of maintenance therapy|Time to relapse|Numeric|
|RECKM|8|1/28/2020|T/F|No relapse|No relapse|No relapse||||||||None|Bone marrow relapse|Bone marrow relapse|T=True, F=FALSE|
|DOWN|9|1/28/2020|T/F|No Down's syndrome|No Down's syndrome|No Down's syndrome||||||||None|Downs syndomr|Exclude if DOWN=T|T=True, F=FALSE|
|ALDER|10|1/28/2020|[1.032-14.872];float|Not possible in format.|Not possible in format.|Not possible in format.||||||||years|Age of patient at diagnosis of leukemia. |Age at diagnosis|Numeric|
|RECIDIV|11|1/28/2020|0/1|Not possible in format.|Not possible in format.|Not possible in format.||||||||None|Relapse yes/no|Relapse yes/no|Binary|
|WBC|12|1/28/2020|[0.50-500];float|Not possible in format.|Not possible in format.|Not possible in format.||||||||x10^9 cells/L blood|White blood cell count|White blood cell count|Numeric|
|anthdm|13|1/28/2020|[1-7]; integer|No HD-MTX cure|No HD-MTX cure|No HD-MTX cure||||||||None|Number of HD-MTX cure|Number of HD-MTX cure|Numeric|
  
  
**Subset 2**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|2|prdata92|28/1 2021|TABULAR|sav|9209|0|NOPHO ALL-92, blood samples, one row per sample per patient to determine EMTX and E6TGN levels ||
  
  
  
*Features of Subset 2*
|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PTNR|14|1/28/2020|Unique patient identifier character|Not possible in format.|None recorded |None recorded ||||||||None|Unique patient identifier character|Unique patient identifier character||
|DAGEDATO|15|1/28/2020|[91-1006];integer|missing value|missing value|missing value||||||||Days|Sampe days since diagnosis|Sampe days since diagnosis|Integer|
|EMTX|16|1/28/2020|[0-20.40];float|Not reported |Not reported |Not reported ||||||||None|erythrocyte-methotrexate|erythrocyte-methotrexate|float|
|E6TGN|17|1/28/2020|[0-1796];float|Not reported |Not reported |Not reported ||||||||None|erythrocyte-TGN|erythrocyte-TGN|float|
  
  
**Subset 3**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|3|meddata92|28/1 2022|TABULAR|sav|28582|0|NOPHO ALL-92, one line per patient reporting medicine, medicine dose or blood sample to determine leukocyte count||
  
  
  
*Features of Subset 3*
|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PTNR|18|1/28/2020|Unique patient identifier character|Not possible in format.|None recorded |None recorded ||||||||None|Unique patient identifier character|Unique patient identifier character||
|ALAT|19|1/28/2020|[0-4420];float|missing value|missing value|missing value||||||||None|ALAT|ALAT||
|ASAT|20|1/28/2020|[0-6180];float|missing value|missing value|missing value||||||||None|ASAT|ASAT||
|leuk|21|1/28/2020|[0.1 - 35.3];float|missing value|missing value|missing value||||||||None|Leukocyte count|Leukocyte count|Numeric|
|lymf|22|1/28/2020|[0-21];float|missing value|missing value|missing value||||||||None|Lymphocyte count|Lymphocyte count|Numeric|
|neut|23|1/28/2020|[0-28,460];float|missing value|missing value|missing value||||||||None|Neutrophil count|Neutrophil count|Numeric|
|trom|24|1/28/2020|[1-1053];interger|missing value|missing value|missing value||||||||None|Platelet count|Platelet count|Numeric|
|DOS_6MP|25|1/28/2020|[0-300];integer|missing value|missing value|missing value||||||||Dose|6-MP dose|6-MP dose|integer|
|DOS_MTX|26|1/28/2020|[0-50];interger|missing value|missing value|missing value||||||||Dose|MTX-dose|MTX-dose|integer|
  
  
**Subset 4**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|4|snitdata92|28/1 2023|TABULAR|sav|538|0|NOPHO ALL-92, Contains a line for each patient with various averages and patient-specific information. The majority of the averages are taken from the course file and how they are determined therefore appears from the description of the course file.||
  
  
  
*Features of Subset 4*
|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PTNR|27|1/28/2020|Unique patient identifier character|Not possible in format.|None recorded |None recorded ||||||||None|Unique patient identifier character|Unique patient identifier character||
|hoejde|28|1/28/2020|[75,0-179,4]; float|missing value|missing value|missing value||||||||cm|height|height|numeric|
|VAEGT|29|1/28/2020|[8,9-96];float|missing value|missing value|missing value||||||||kg|weight|weight|numeric|
|tpmtsnit|30|1/28/2020|[0.52-27.61];float|missing value|missing value|missing value||||||||None|average tpmt|average tpmt|numeric|
  
  
**Subset 5**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|5|ptdata08|28/1 2024|TABULAR|sav|3162|0|NOPHO ALL-2008, patient cohort with background information.||
  
  
  
*Features of Subset 5*
|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PTNR|31|1/28/2020|Unique patient identifier character|Not possible in format.|None recorded |None recorded ||||||||None|Unique patient identifier character|Unique patient identifier character||
|sex|32|1/28/2020|1: Male, 2: Female|Not possible in format.|Not possible in format|Missing value||||||||None|Sex of a patient|Used to define the sex of a person, often used to tsratify patients or as a covariate in analysis. |Binary|
|diagdate|33|1/28/2020|YYYY-MM-DD|Not possible in format.|Not possible in format|Missing value||||||||None|Date of leukemia diagnosis|Used for longitudinal analysis of data|Dates|
|age|34|1/28/2020|1-18; float|Not possible in format.|Zero years since diagnosis|Missing value|||||||birthdate and diagdate|Years|Age of patient at diagnosis of leukemia. |Often used in analysis as many biological features can be influenced by age. |None|
|imm2008|35|1/28/2020|1: B-precursor ALL, 2: T-cell ALL, 3: Bilineage ALL = excl. from SR and Rand., 4: mature B-cell ALL, 9: Missing data|Missing value|Not possible in format|Missing value||||||||None|Immunophenotype/Cell lineage of acute lymphoblastic leukemia (ALL)|Used to stratify patients as the different subtypes have much biological variation. |Categorical|
|wbchival|36|1/28/2020|0..inf; float|Missing value|Not possible in format|Missing value||||||||x10^9 cells/L blood|Highest measure of white blood cells in peripheral blood. Measured before any treatment/at diagnosis of ALL. |Used as a stratification measure in the first treatment stratification. Measure of tumor burden in leukemia. |None|
|excluded|37|1/28/2020|0: No, 1: Yes||No to excluded|Missing value||||||||None|Decides if a patient has been excluded for any clinical or non-clinical reason. |Patients can be excluded from the protocol, and potentially also from analysis. |Binary|
|exclusionclinical       |38|1/28/2020|0: no reasons for exclusion, 1: clinical decision to exclude patient for other reason|Reason for exclusion not relevant|no reasons for exclusion|Reason for exclusion not relevant||||||||None|Gives the reason for exclusion as either clinical or not|Can be used to determine if excluded patients should still be in analysis. |Binary|
|strat1|39|1/28/2020|0: Insufficient data, 1 & 2: NOPHO-2008 Non-HighRisk, 3: NOPHO-2008 High Risk, 9: Excluded|None recorded |Insufficient data|None recorded||||||||None|Defines the stratification group applied at diagnosis (day 0), which decides the intensity of leukemia treatement. |Based on clinical measures of stratification and can give information on the initial treatment intensity. |Categorical|
|therapyind|40|1/28/2020|1: NOPHO-2008 induction therapy with Prednisolone only, 2: NOPHO-2008 induction therapy with Dexa. +/- pred-prephase, 3: Other induction therapy|MIssing value|Not possible in format|Missing value||||||||None|Defines the type of induction therapy administered. ||Categorical|
|strat2|41|1/28/2020|0: Insufficient data, 1 & 2: NOPHO-2008 Non-HighRisk, 3: NOPHO-2008 High Risk, 9: Excluded|Not possible in format.|Insufficient data|None recorded||||||||None|Defines the stratification group applied after genetic analysis. |Based on clinical measures of stratification and can give information on the initial treatment intensity. |Categorical|
|strat3|42|1/28/2020|0: Insufficient data, 1 & 2: NOPHO-2008 Non-HighRisk, 3: NOPHO-2008 High Risk, but had standard risk induction therapy, 4: NOPHO-2008 High Risk blocksDirect, 9: Excluded|Not possible in format.|Insufficient data|None recorded||||||||None|Defines the stratification group at day 15 after early response therapy. |Based on clinical measures of stratification and can give information on the continued treatment intensity. |Categorical|
|therapyd15|43|1/28/2020|1: NOPHO-2008 Standard/Intermediate risk (continue induction therapy Pred), 2: NOPHO-2008 High Risk (continue induction therapy Dexa), 3: NOPHO-2008 High risk (block therapy), 9: Other therapy used. |Missing value|Not possible in format|Missing value||||||||None|Defines the type of therapy administered after the stratification at day 15. ||Categorical|
|therapyd15comm|44|1/28/2020|Character string|||||||||||None|Comment on the therapy applied from day 15. ||String|
|remjn|45|1/28/2020|0: Too early, 1: Yes, 2: No|Not possible in format.|Too early to see remission response|None recorded||||||||None|Defines if a remission response is seen. |Helps define the individual patient response to treatment. |Categorical|
|strat4|46|1/28/2020|0: Insufficient data, 1: NOPHO-2008 Standard Risk, 2: NOPHO-2008 Intermediate Risk, 5: NOPHO-2008 High Risk chemo, 6: NOPHO-2008 High Risk stem cell transplant (SCT) in first complete remission (CR1), 9: Excluded|Not possible in format.|Insufficient data|None recorded||||||||None|Defines the risk stratificiation after intermediate response on day 29. |Determines the continued treatment intensity at day 29 and current risk of treatment failure or relapse. |Categorical|
|therapyd29|47|1/28/2020|1: NOPHO-2008 Standard risk, 2: NOPHO-2008 Intermediate risk, 3: NOPHO-2008 High risk chemo, 4: NOPHO-2008 High risk stem cell transplant (SCT) in first complete remission (CR1), 5: Other therapy administered. |Missing value|Not possible in format|None recorded||||||||None|Defines the therapy type administered from day 29||Categorical|
|therapyd29comm|48|1/28/2020|Character string|||||||||||None|Comment on the therapy applied from day 29. ||String|
|strat5|49|1/28/2020|0: Insufficient data, 1: NOPHO-2008 Standard Risk, 2: NOPHO-2008 Intermediate Risk, 5: NOPHO-2008 High Risk chemo, 6: NOPHO-2008 High Risk stem cell transplant (SCT) in first complete remission (CR1), 7: Event, 9: Excluded|Not possible in format.|Insufficient data|None recorded||||||||None|Defines the final risk stratificiation at day 79|Determines the final treatment intensity at day 79 and current risk of treatment failure or relapse. |Categorical|
|therapyd79|50|1/28/2020|1: NOPHO-2008 Standard risk, 2: NOPHO-2008 Intermediate risk, 3: NOPHO-2008 High risk chemo, 4: NOPHO-2008 High risk stem cell transplant (SCT) in first complete remission (CR1), 5: Other therapy administered. |Missing value|Not possible in format|None recorded||||||||None|Defines the therapy type administered after the final treatment stratification from day 79. ||Categorical|
|therapyd79comm|51|1/28/2020|Character string|Missing value||||||||||None|Comment on the therapy applied from day 79. ||String|
|primevstatus|52|1/28/2020|0: first complete remission (CR1), 1: induction failure, 2: resistant disease, 3: relapse, 4: death in first complete remission (DCR1), 5: development of second malignant neoplasms (SMN)|Missing value|Insufficient data|Missing value||||||||None|Status of primary event|The events tell about how the treatement and disease progress. |Categorical |
|deadccr|53|1/28/2020|1: yes, 2: no|Missing value|Not possible in format|Missing value||||||||None|Defines if a patient died following continued complete remission (was alive during first complete remission (CR1)). |||
  
  
**Subset 6**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|6|prdata08|28/1 2025|TABULAR|xlxs|43896|0|NOPHO ALL-08, blood samples, one row per sample per patient to determine metabolite levels incl. Methylated metabolites ||
  
  
  
*Features of Subset 6*
|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|PTNR|54|1/28/2020|Unique patient identifier character|Not possible in format.|None recorded |None recorded ||||||||None|Unique patient identifier character|Unique patient identifier character||
|SAMPLETIME|55|1/28/2020|Sampling time since diagnosis|Not possible in format.|None recorded |None recorded ||||||||Days|Number of days bloodsample taken since diagnosis|Number of days bloodsample taken since diagnosis|Interger|
|TGN|56|1/28/2020|[-1-11087]; float|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value||||||||None|thioguanine nucleotides;  -1 = least standard, 0 = regular value |thioguanine nucleotides;  -1 = least standard, 0 = regular value |Numeric|
|DNA-6TGN|57|1/28/2020|[0-3207]; float|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value||||||||None|DNA-incorporated thioguanine ;   -1 = least standard, 0 = regular value |DNA-incorporated thioguanine ;   -1 = least standard, 0 = regular value |Numeric|
|MMP|58|1/28/2020|[-1-49637];float|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value||||||||None|Methylated 6-MP;   -1 = least standard, 0 = regular value |Methylated 6-MP;   -1 = least standard, 0 = regular value |Numeric|
|TPMT|59|1/28/2020|[5-28];float|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value||||||||None|enzyme thiopurine S-methyl transferase;   -1 = least standard, 0 = regular value |enzyme thiopurine S-methyl transferase;   -1 = least standard, 0 = regular value |Numeric|
|MTX|62|1/28/2020|[-9-0];float|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value||||||||None|methotrexate; -9 means detectable value, -1 = least standard, 0 = regular value |methotrexate; -9 means detectable value, -1 = least standard, 0 = regular value |Numeric|
|MTXpg1|63|1/28/2020|[0-2];float|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value||||||||None|methotrexate (MTX) 1 polyglutamates|methotrexate (MTX) 1 polyglutamates|Numeric|
|MTXpg2|64|1/28/2020|[0-1];float|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value||||||||None|methotrexate (MTX) 2 polyglutamates|methotrexate (MTX) 2 polyglutamates|Numeric|
|MTXpg3|65|1/28/2020|[0-1];float|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value||||||||None|methotrexate (MTX) 3 polyglutamates|methotrexate (MTX) 3 polyglutamates|Numeric|
|MTXpg4|66|1/28/2020|0;float|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value||||||||None|methotrexate (MTX) 4 polyglutamates|methotrexate (MTX) 4 polyglutamates|Numeric|
|MTXpg5|67|1/28/2020|0;float|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value||||||||None|methotrexate (MTX) 5 polyglutamates|methotrexate (MTX) 5 polyglutamates|Numeric|
|MTXpg6|68|1/28/2020|0;float|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value|NULL=no value, 0 = regular value||||||||None|methotrexate (MTX) 6 polyglutamates|methotrexate (MTX) 6 polyglutamates|Numeric|
  
  
**Subset 7**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|7|genotype data08|28/1 2026|files|binary plink|3|0|NOPHO ALL-2008. Genome-wide SNP profiling. 2146021 variants and 1829 people pass filters and QC.||
  
  
