


  
<style> th { padding: 7px;} .markdown-body { max-width:1400px} </style>

Bellow the subsets and their corresponding features are presented.  
**Subset 1**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|1|Stability assay|3/9/2021|TABULAR|CSV|4919|0|Measurements of peptide:MHC stability. ELISA measurement, quantitative labels.||
  
  
  
*Features of Subset 1*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Peptide|1|3/9/2021|Combination;String|Not possible|Not possible|Not possible||None|Combination of amino acids making up the peptide.|Different combinations of amino acids yield different binding affinities; can we predict this based solely on any given combination?|None|
|ELISA_Stability|2|3/9/2021|0..1;Float|Not possible|Unstable|Not possible||None|A measure of MHC binding stability as determined by ELISA.|A measure of MHC binding stability as determined by ELISA.|None|
  
  
**Subset 2**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|2|MS dataset 1|3/9/2021|TABULAR|CSV|2827|0|Measurements of peptide:MHC binding. Mass Spectroscopy, binary labels.||
  
  
  
*Features of Subset 2*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Peptide|3|3/9/2021|Combination;String|Not possible|Not possible|Not possible||None|Combination of amino acids making up the peptide.|Different combinations of amino acids yield different binding affinities; can we predict this based solely on any given combination?|None|
|MASS_Bind|4|3/9/2021|0,1;Binary|Not possible|No binding|Not possible||None|A YES/NO on whether binding is detected by Mass spec.|A YES/NO on whether binding is detected by Mass spec.|None|
  
