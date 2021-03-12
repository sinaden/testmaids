


  
<style> th { padding: 7px;} .markdown-body { max-width:1400px} </style>

Bellow the subsets and their corresponding features are presented.  
**Subset 1**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|1|Genetics-Processed|2021/03/10|FILES|VCF|100|0|One VCF file per patient describes the variation in the patients genome with respect to a common reference. |https://samtools.github.io/hts-specs/VCFv4.2.pdf|
  
  
  
**Subset 2**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|2|TruCulture_processed|2021/02/16|TABULAR|CSV/XLSX|1150|0|Summarized biological readouts from TruCulture: induced cytokine protein levels - the functional outcome related to cell-popoulations/phenotypes and genotypes|https://myriadrbm.com/truculture/|
  
  
  
*Features of Subset 2*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|STUDY_ID|1||Many, character/string|Not possible in format.|No zeros|Not possible in format.||None|Pseudonymized patient identifier|Study-specific patient ID needed to map this subset to the others.|All start with "COVIMUN": name of study, followed by "XX": capitalized hospital code, followed by enrollment number at that hospital|
|DC_SAMPLE_ID|2||Two sep by _, (4013..inf; integer) representing sample number, (2020..2021; YYYY) representing sample year|Not possible in format.|No zeros|Not possible in format.||Not possible in format.|Unique sample identifier|Unique ID to identify specific DuraClone sample, always connected to a single STUDY_ID|None|
|SAMPLE_DATE|3||YYYY-MM-DD|Not possible in format.|No zeros|Not possible in format.||None|Date of sampling|Investigate longitudinal effect. Can together with STUDY_ID link samples from different subsets taken at the same time/the same date|None|
|TUBE|4||Many, character/string|Not possible in format.|No zeros|Not possible in format.||None|Identifies the specific flow cytometry tube from which data is derived |Each tube has a specific set of antibody markers, enables backtracking from a feature|T = tube, 1-9 = number of tube|
|VAR_NAME|5||Many, character/string; cell population/phenotype symbol|Not possible in format.|No zeros|Not possible in format.||None|Identifies the specific cell population and phenotype markers|Potential  features/outcome variables|None|
|VAR_UNIT|6||Many, character/string; count, concentration, or mfi|Not possible in format.|No zeros|Not possible in format.||See definition|cnt: events detected for the given variable, "con": corresponding bloodstream concentration, "mfi": mean fluorescence intensity corresponding to a marker's mean expression level|Concentration and mean fluorescence intensity allow for comparison between samples|None|
|VAR_VAL|7||0..inf; real|Measurment missing for a random reason e.g. technical error with assay|Cell population/ marker level not present or under detectible level in sample|Measurement or sample missing||Specified under VAR_UNIT|Value of measurement|Value of measurement|None|
  
  
**Subset 3**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|3|Duraclone_processed|2020/06/05|TABULAR|CSV/XLSX|289200|0|Summarized biological readouts from Duraclone: immune cell popoulation -and phenotype levels - outcome related to  genotypes|https://www.beckman.fr/reagents/coulter-flow-cytometry/antibodies-and-kits/duraclone-panels|
  
  
  
*Features of Subset 3*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|STUDY_ID|1||Many, character/string|Not possible in format.|No zeros|Not possible in format.||None|Pseudonymized patient identifier|Study-specific patient ID needed to map this subset to the others.|All start with "COVIMUN": name of study, followed by "XX": capitalized hospital code, followed by enrollment number at that hospital|
|SAMPLE_DATE|2||YYYY-MM-DD|Not possible in format.|No zeros|Not possible in format.||None|Date of sampling|Investigate longitudinal effect. Can together with STUDY_ID link samples from different subsets taken at the same time/the same date|None|
|TC_SAMPLE_ID|3||(1147..inf; integer) representing TruCulture sample number|Not possible in format.|No zeros|Not possible in format.||Not possible in format.|Unique sample identifier|Unique ID to identify specific TruCulture sample, always connected to a single STUDY_ID|None|
|STIMULI|4||Many, character/string|NULL means unstimulated (control for stimulated samples)|No zeros|Not possible in format.||None|NULL : no stimulation, "LPS" : lipopolysaccharide (bacterial stimuli), "R848" : resiquimod (viral stimuli), "PolyIC" : Polyinosinic:polycytidylic acid (viral stimuli), "HKCA" heat killed candida albicans (fungal stimuli), "CD3/CD28" T-cell stimulation (direct stimulation)|The stimuli correspond to different infectious agents, inducing functional immune responses (cytokine release) ||
|IFNa|5||0..inf; real|Measurment missing for a random reason e.g. technical error with assay|Cytokine protein under detectible level in sample|Measurement or sample missing||concentration (pg/mL)|Value of measurement|Measurement of variable, potential feature/outcome varible|None|
|IFNg|6||0..inf; real|Measurment missing for a random reason e.g. technical error with assay|Cytokine protein under detectible level in sample|Measurement or sample missing||concentration (pg/mL)|Value of measurement|Measurement of variable, potential feature/outcome varible|None|
|IL10|7||0..inf; real|Measurment missing for a random reason e.g. technical error with assay|Cytokine protein under detectible level in sample|Measurement or sample missing||concentration (pg/mL)|Value of measurement|Measurement of variable, potential feature/outcome varible|None|
|IL12|8||0..inf; real|Measurment missing for a random reason e.g. technical error with assay|Cytokine protein under detectible level in sample|Measurement or sample missing||concentration (pg/mL)|Value of measurement|Measurement of variable, potential feature/outcome varible|None|
|IL17A|9||0..inf; real|Measurment missing for a random reason e.g. technical error with assay|Cytokine protein under detectible level in sample|Measurement or sample missing||concentration (pg/mL)|Value of measurement|Measurement of variable, potential feature/outcome varible|None|
|IL1b|10||0..inf; real|Measurment missing for a random reason e.g. technical error with assay|Cytokine protein under detectible level in sample|Measurement or sample missing||concentration (pg/mL)|Value of measurement|Measurement of variable, potential feature/outcome varible|None|
|IL6|11||0..inf; real|Measurment missing for a random reason e.g. technical error with assay|Cytokine protein under detectible level in sample|Measurement or sample missing||concentration (pg/mL)|Value of measurement|Measurement of variable, potential feature/outcome varible|None|
|IL8|12||0..inf; real|Measurment missing for a random reason e.g. technical error with assay|Cytokine protein under detectible level in sample|Measurement or sample missing||concentration (pg/mL)|Value of measurement|Measurement of variable, potential feature/outcome varible|None|
|TNFa|13||0..inf; real|Measurment missing for a random reason e.g. technical error with assay|Cytokine protein under detectible level in sample|Measurement or sample missing||concentration (pg/mL)|Value of measurement|Measurement of variable, potential feature/outcome varible|None|
  
