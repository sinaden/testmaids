


  
<style> th { padding: 7px;} .markdown-body { max-width:1400px} </style>

Bellow the subsets and their corresponding features are presented.  
**Subset 1**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|1|Baseline|2019-11-22|TABULAR|CSV|4999|0|Contains CLL prognostic factor variables taken around time of diagnosis||
  
  
  
*Features of Subset 1*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pid|1||0..inf; integer|Not possible in format.|Zero is first patient|Not possible in format.||None|Pseudonymized patient identifier|Needed to link different cohorts|None|
|Gender|2||Male,Female|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Gender assigned at birth based on physical characteristics.|Often a proxy for other biological features. It might be used to stratify and control for batch effects or examined directly as a covariate of interest.|None|
|Age|3||0..inf; integer|No NA, NULL, or NONE|No zeros|Not possible in format.||yrs|Age at time of CLL diagnosis|Often a proxy for other biological features. It might be used to stratify and control for batch effects or examined directly as a covariate of interest.|None|
|Binet|4||A,B,C|No NA, NULL, or NONE|No zeros|Not possible in format.||None|number of affected lymphoid tissue groups|CLL Prognostic Factor|None|
|ECOG.PS|5||0,1,2,3,4|nan means test not taken or inconclusive|0 part of score|Not possible in format.||None|General well being score|CLL Prognostic Factor|None|
|CLL.IPI|6||Low, Intermediate,High,Very High|nan means that not all CLL-IPI factors are available|0 part of score|Not possible in format.||None|CLL Risk Score|CLL Prognostic Factor|None|
|B2M|7||<4.0 mg/L, >4.0 mg/L|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|beta2-microglobulin levels|CLL Prognostic Factor|None|
|IGHV|8||Mutated, unmutated|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|Immunoglobulin heavy chain variable region mutated status|CLL Prognostic Factor|None|
|FISH.status|9||Del13q,Normal,Tri12,Del17p|nan means that not all FISH factors are available|No zeros|Not possible in format.||None|Chromosomal abnormalities in CLL|CLL Prognostic Factor|None|
|DEL13Q|10||Yes,No|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|Chromosomal abnormalities in CLL|CLL Prognostic Factor|None|
|TRISOM12|11||Yes,No|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|Chromosomal abnormalities in CLL|CLL Prognostic Factor|None|
|DEL11Q|12||Yes,No|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|Chromosomal abnormalities in CLL|CLL Prognostic Factor|None|
|DEL17p|13||Yes,No|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|Chromosomal abnormalities in CLL|CLL Prognostic Factor|None|
|ZAP70|14||Yes,No|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|Zeta-chain-associated protein kinase 70 (ZAP-70) expression|CLL Prognostic Factor|None|
|CD38|15||Yes,No|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|Expression of CD38 by CLL cells|CLL Prognostic Factor|None|
|Anemia|16||Yes,No|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|Low red blood cell count|CLL Prognostic Factor|None|
|Thrombopenia|17||Yes,No|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|Low platelet count|CLL Prognostic Factor|None|
|Weight.loss|18||Yes,No|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|Weight Loss|CLL Prognostic Factor|None|
|Fever|19||Yes,No|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|Fever|CLL Prognostic Factor|None|
|Night.sweat|20||Yes,No|nan means test not taken or inconclusive|No zeros|Not possible in format.||None|Night Sweats|CLL Prognostic Factor|None|
  
  
**Subset 2**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|2|CLL Registry|2019-11-22|TABULAR|CSV|4999|0|Patient information relevant for generaiton of outcomes related to treatment and death||
  
  
  
*Features of Subset 2*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pid|1||0..inf; integer|Not possible in format.|Zero is first patient|Not possible in format.||None|Pseudonymized patient identifier|Needed to link different cohorts|None|
|Date_of_birth|2||YYYY-MM-DD|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Date of Birth|Needed to calculate age at different time-points|None|
|Date_diag|3||YYYY-MM-DD|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Date of CLL Diagnosis|Baseline variables calculated around time of diagnosis|None|
|Date_treatment|4||YYYY-MM-DD|Null Means no treatment given or|No zeros|Not possible in format.||None|Date of CLL Treatment|Needed for outcome definition|None|
|Date_DeathFollowup|5||YYYY-MM-DD|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Date of Death or Last Follow Up|Needed for outcome definition|None|
|Date_Death|6||YYYY-MM-DD|nan Means patient is still alive|No zeros|Not possible in format.||None|Date of Death|Needed for outcome definition|None|
|Date_PFS|7||YYYY-MM-DD|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Last Date of Progression Free Survival|Needed for outcome definition|None|
|Progression|8||0,1|No NA, NULL, or NONE|Zero means no progression|Not possible in format.||None|Whether CLL Disease Progressed|Needed for outcome definition|None|
|TimeTo_PFS|9||0..inf; integer|No NA, NULL, or NONE|Zero is time to progression|Not possible in format.||Days|Time to Progression Free Survival|Needed for outcome definition|None|
|Treatment|10||0,1|No NA, NULL, or NONE|Zero is no treatment|Not possible in format.||None|Whether Patient Received CLL Treatment|Needed for outcome definition|None|
|TimeTo_Treatment|11||0..inf; integer|No NA, NULL, or NONE|Zero is time to treatment|Not possible in format.||Days|Time to CLL Treatment|Needed for outcome definition|None|
  
  
**Subset 3**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|3|Treatment Outcome|2020-02-30|TABULAR|CSV|1996|0|Treatment outcome information that includdes lines of treament and type of treament||
  
  
  
*Features of Subset 3*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pid|1||0..inf; integer|Not possible in format.|Zero is first patient|Not possible in format.||None|Pseudonymized patient identifier|Needed to link different cohorts|None|
|line|2||1..8; integer|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Line of treatment|Needed for outcome definition|None|
|date_treatment|3||YYYY-MM-DD|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Start date for given line of treatment|Needed for outcome definition|None|
|chemotherapy|4||Many;string|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Treatment included chemotherapy|Needed for outcome definition|None|
|immunotherapy|5||Many;string|nan means immunotherapy not given|No zeros|Not possible in format.||None|Treatment included immunotherapy|Needed for outcome definition|None|
  
  
**Subset 4**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|4|Diagnosis|2020-02-30|TABULAR|CSV|147197|0|Historical data on previous patient diagnosis - not necessarily related to CLL||
  
  
  
*Features of Subset 4*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pid|1||0..inf; integer|Not possible in format.|Zero is first patient|Not possible in format.||None|Pseudonymized patient identifier|Needed to link different cohorts|None|
|DIAG_CODE|2||Many;string|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Diagnosis code|Potential Feature|None|
|DIAG_COURSE_D|3||YYYY-MM-DD|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Date of diagnosis code|Potential Feature|None|
|DIAG_COURSE_T|4||HH-MM-SS|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Time in day of diagnosis code|Potential Feature|None|
  
  
**Subset 5**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|5|Laboratory|2020-02-30|TABULAR|CSV|4226248|0|Laboratory tests data - not necessarily related to CLL||
  
  
  
*Features of Subset 5*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pid|1||0..inf; integer|Not possible in format.|No zeros|Not possible in format.||None|Pseudonymized patient identifier|Needed to link different cohorts|None|
|LAB_ID|2||Many;string|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Name of Laboratory Test|Potential Feature|None|
|LAB_D|3||YYYY-MM-DD|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Laboratory Test Date|Potential Feature|None|
|LAB_T|4||HH-MM-SS|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Laboratory Test Time in day|Potential Feature|None|
  
  
**Subset 6**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|6|Pathology|2020-02-30|TABULAR|CSV|199337|0|Historical data on previous patient pathology - not necessarily related to CLL||
  
  
  
*Features of Subset 6*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pid|1||0..inf; integer|Not possible in format.|No zeros|Not possible in format.||None|Pseudonymized patient identifier|Needed to link different cohorts|None|
|PAT_CODE|2||Many;string|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Pathology Code|Potential Feature|None|
|PAT_D|3||YYYY-MM-DD|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Pathology Date|Potential Feature|None|
|PAT_T|4||HH-MM-SS|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Pathology time in day|Potential Feature|None|
  
  
**Subset 7**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|7|Laboratory Cultures|2020-02-30|TABULAR|CSV|84299|0|Laboratory culture data - necessarily for creating features and outcomes related to infections||
  
  
  
*Features of Subset 7*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pid|1||0..inf; integer|Not possible in format.|No zeros|Not possible in format.||None|Pseudonymized patient identifier|Needed to link different cohorts|None|
|SAMPLE_NO|2||0..inf; integer|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Sample Number|Potential Feature & Needed for Outcome Definition |None|
|SAMPLE_MAT|3||Many;string|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Category of Sample (blood, urine, etc)|Potential Feature & Needed for Outcome Definition |None|
|SAMPLE_D|4||YYYY-MM-DD|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Sample Date|Potential Feature & Needed for Outcome Definition |None|
|SAMPLE_T|5||HH-MM-SS|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Sample Time in Day|Potential Feature & Needed for Outcome Definition |None|
|CULT_MAT_GROUP|6||Many;string|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Category of lab culture|Potential Feature & Needed for Outcome Definition |None|
|RESULT|7||Many;string|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Result of lab culture|Potential Feature & Needed for Outcome Definition |None|
|CULT_FIND|8||0..inf; integer|nan possibly missing at random|No zeros|Not possible in format.||None|Abundance of Finding|Potential Feature & Needed for Outcome Definition |None|
|RESULT_CAT|9||Positive,Negative|nan possibly missing at random|No zeros|Not possible in format.||None|Whether Positive or Negative Finding|Potential Feature & Needed for Outcome Definition |None|
  
  
**Subset 8**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|8|Medications|2019-06-30|TABULAR|CSV|1098273|0|Historical data on prescribed medications - not neccesarily related to CLL||
  
  
  
*Features of Subset 8*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|pid|1||0..inf; integer|Not possible in format.|No zeros|Not possible in format.||None|Pseudonymized patient identifier|Needed to link different cohorts|None|
|atc_kode|2||Many;string|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Medication Code|Potential Feature|None|
|expdato|3||DDMMMYYYY|No NA, NULL, or NONE|No zeros|Not possible in format.||None|Start of Medication|Potential Feature|None|
|Stryke|4||1..inf;float|nan means unknown|No zeros|Not possible in format.||None|Dosage value|Potential Feature|None|
|Unit|5||Many;string|nan means unknown|No zeros|Not possible in format.||None|Dosage unit|Potential Feature|None|
  
