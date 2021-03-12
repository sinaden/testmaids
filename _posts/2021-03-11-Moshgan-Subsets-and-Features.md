<style>
th{
    padding: 7px;
}
</style>




Bellow the subsets and their corresponding features are presented.  
**Subset 1**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|1|Study ID|Jan-21|Tabular/Flat|Redcap (CSV/Excel)|104|0|Project ID and date of enrolment|None|
  
  
*Features of Subset 1*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|id|1|6/25/2019|1..inf; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Pseudonymized patient identifier|Needed to map this subset to the others.|None|
|date|2|6/25/2019|YYYY-MM-DD|Not possible in format.|No zeros|Not possible in format.||||||||None|Date of sampling|Investigate longitudinal effect.|None|
  
  
**Subset 2**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|2|Cause of ICU admission|Jan-21|Tabular/Flat|Redcap (CSV/Excel)|104|0|Describing primary cause of admission, date of admission and date of injury|None|
  
  
*Features of Subset 2*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|date_admission|3|6/25/2019|YYYY-MM-DD|Not possible in format.|No zeros|Not possible in format.||||||||None|Date of sampling|Investigate longitudinal effect.|None|
|date_injury|4|6/25/2019|YYYY-MM-DD|Not possible in format.|No zeros|Not possible in format.||||||||None|Date of sampling|Investigate longitudinal effect.|None|
|reason_icu_ad|5|6/25/2019|1..21; integer|OTHER; Other medical or surgical diagnose not included in the list|No zeros|Not possible in format.||||||||None|Underlying diagnosis|Etiology of unresponsiveness|None|
|stroke_etiology|6|6/25/2019|1…8; integer|Not possible in format.|No zeros|Not ischemic stroke||||||||None|Underlying etiology of ischemic stroke|Investigate association to prognosis|None|
|stroke_oxford|7|6/25/2019|1…5; integer|Not possible in format.|No zeros|Not ischemic stroke||||||||None|Classification of stroke type based on CT scan|Severity of stroke|None|
|ich_etiology|8|6/25/2019|1…9; integer|Not possible in format.|No zeros|Not hemorrhagic stroke||||||||None|Underlying etiology of hemorrhagic stroke|Investigate association to prognosis|None|
|sah|9|6/25/2019|1…3; integer|Not possible in format.|No zeros|Not SAH||||||||None|Underlying etiology of subarachnoid hemorrhage|Investigate association to prognosis|None|
|sah_aneurysm|10|6/25/2019|1…10; integer|Not possible in format.|No zeros|Not (aneurysmal) SAH||||||||None|Type of aneurysm|Investigate association to prognosis|None|
|cold_aneurysm|11|6/25/2019|1…3; integer|Not possible in format.|No zeros|Not (aneurysmal) SAH||||||||None|Additional cold aneurysms not bleeding actively|Investigate association to prognosis|None|
|sah_nonanurysm|12|6/25/2019|1…12; integer|Not possible in format.|No zeros|Not SAH||||||||None|Type of non aneurysm SAH|Investigate association to prognosis|None|
|tbi_mechanism|13|6/25/2019|1…9; integer|OTHER; Other mechanisms to head injury not included in the list of frequent causes|No zeros|Not traumatic brain injury||||||||None|Underlying cause of TBI based on trauma mechanism|Investigate association to prognosis|None|
|tbi_alcohol_drugs|14|6/25/2019|1…5; integer|Not possible in format.|No zeros|Not traumatic brain injury||||||||None|Drug or alcohol intoxication at time of head injury|Investigate association to severity of head injury|None|
|tbi_loc|15|6/25/2019|1…5; integer|Not possible in format.|No zeros|Not traumatic brain injury||||||||None|Localisation of brain injury based on CT scan|Investigate association to severity of head injury|None|
|tbi_pathophysiol|16|6/25/2019|1…16; integer|Not possible in format.|No zeros|Not traumatic brain injury||||||||None|Pathophysiology of brain injury|Investigate association to severity of head injury|None|
|epilepsy_spec_3|17|6/25/2019|1…8; integer|OTHER; Other type of epileptic seizure not listed|No zeros|Not epileptic seizure||||||||None|Type of seizure|Investigate association to prognosis and unresponsiveness|None|
|aut_encephilitis|18|6/25/2019|1…4; integer|Not possible in format.|No zeros|Not autoimmune encephalitis||||||||None|Type of encephalitris|Investigate association to prognosis and unresponsiveness|None|
|neuromusc_weak|19|6/25/2019|1…5; integer|OTHER: Other myopathy or neuropathy not listed|No zeros|Not neuromuscular weakness||||||||None|Type of neuromuscular weakness|Investigate association to prognosis and unresponsiveness|None|
|card_arrest|20|6/25/2019|1…2; integer|Not possible in format.|No zeros|Not cardiac arrest||||||||None|In- or out-of-hospital cardiac arrest|Investigate association to prognosis and unresponsiveness|None|
|anoxia_non_cardiac|21|6/25/2019|1…8; integer|OTHER: Other cause of anoxia not listed|No zeros|Not non cardiac anoxic brain damage||||||||None|Type of anoxic brain damage|Investigate association to prognosis and unresponsiveness|None|
|intox|22|6/25/2019|1…2; integer|Not possible in format.|No zeros|Not intoxication as cause of ICU admission||||||||None|Accidental or non accidental intoxication|Investigate association to prognosis and unresponsiveness|None|
|ac_intox|23|6/25/2019|1…4; integer|OTHER: Other cause of accidental intoxiation not listed|No zeros|Not accidental intoxication as cause of ICU admission||||||||None|Type of accidental intoxication|Investigate association to prognosis and unresponsiveness|None|
|self_intox|24|6/25/2019|1…5; integer|OTHER: Other cause of selfinflicted intoxiation not listed|No zeros|Not selfinflicted intoxication as cause of ICU admission||||||||None|Type of selfinflicted intoxication|Investigate association to prognosis and unresponsiveness|None|
|bact_meningitis|25|6/25/2019|1…6; integer|OTHER: Other cause of bacteriel meningitis not listed|No zeros|Not bacteriel meningitis||||||||None|Etiology of bacteriel meningitis|Investigate association to prognosis and unresponsiveness|None|
|hsv|26|6/25/2019|yes/No|Not possible in format.|Not PCR verified herpes encephalitis|Not herpes encephalitis||||||||None|Verification of Herpes encephalitis|Investigate association to prognosis and unresponsiveness|None|
|other_meningoenc|27|6/25/2019|yes/No|Not possible in format.|Not serologically verified other kind of meningoencephalitis|Not meningoencephalitis||||||||None|Verification of microorganism causing meningoencephalitis|Investigate association to prognosis and unresponsiveness|None|
|inborn_error_of_metabolism|28|6/25/2019|1…4; integer|OTHER: Other cause of inborn error of metabolism not listed|No zeros|Not inborn error of metabolism||||||||None|Etiology of inborn error of metabolism causing brain injury|Investigate association to prognosis and unresponsiveness|None|
|global_cerebral_edema|29|6/25/2019|1…5; integer|OTHER: Other cause of global cerebral edema not listed|No zeros|Not global brain edema||||||||None|Cause of global brain edema|Investigate association to prognosis and unresponsiveness|None|
|other_medical_reason|30|6/25/2019|Text description|Not possible in format.|No zeros|Not other medical reason for icu admission||||||||None|Other medical cause of icu admission |Investigate association to prognosis and unresponsiveness|None|
|other_surgical_reason|31|6/25/2019|Text description|Not possible in format.|No zeros|Not other surgical reason for icu admission||||||||None|Other surgical cause of icu admission |Investigate association to prognosis and unresponsiveness|None|
  
  
**Subset 3**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|3|Baseline data at ICU admission|Jan-21|Tabular/Flat|Redcap (CSV/Excel)|104|0|Demographics (age, sex, previous medical history, previous level of daily function), overall clinical condition at admission (temperature, level of creatinine level of movement, early hypoxia or hypotension)|None|
  
  
*Features of Subset 3*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|sex|32|6/25/2019|1…3; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Gender; Male, Female or transgender|Biological feature|None|
|age|33|6/25/2019|0..inf; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Age since birth at time of admission|Biological feature|None|
|temp|34|6/25/2019|0..45; real|Not possible in format.|No zeros|Not available/not recorded||||||||None|Body temperature measured at time of admission|Basic physiological satte at time of admission|None|
|creat_b|35|6/25/2019|0..1500; real|Not possible in format.|No zeros|Not available/not recorded||||||||None|Creatinine level at time of admission measured in plasma|Basic physiological satte at time of admission|None|
|mrs_prior|36|6/25/2019|0…6; integer|Not possible in format.|0; No symptoms|Not possible in format.||||||||None|Level of daily function prior to admission based on verified scale|Often an important covariate in prognostication|None|
|prev_medical_history|37|6/25/2019|1…3; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Presence of previous medical history recorded in health records|Often an important covariate in prognostication|None|
|prev_med_host_present|38|6/25/2019|1..21; integer|OTHER: Other known medical history not listed|No zeros|Not possible in format.||||||||None|Type of present medical history|Often an important covariate in prognostication|None|
|malign|39|6/25/2019|1..18; integer|OTHER: Other known history of malignancy not listed|No zeros|No history malignancy||||||||None|Type of malignancy according to organs effected|May be an important covariate|None|
|prev_neurol_history|40|6/25/2019|1…3; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Presence of previous neurological history|Often an important covariate in prognostication|None|
|prev_neurol_history_yes|41|6/25/2019|1…34; integer|OTHER: Other neurological disorder not listed|No zeros|No history history of previous neurological disease||||||||None|Type of neurological history|Often an important covariate in prognostication|None|
|prev_stroke_territory|42|6/25/2019|1…12; integer|Not possible in format.|No zeros|No history of ishemic stroke||||||||None|Territory of stroke|Often an important covariate in prognostication|None|
|prev_stroke_etiology|43|6/25/2019|1…8; integer|Not possible in format.|No zeros|No history ischemic stroke||||||||None|Underlying etiology of ischemic stroke|Often an important covariate in prognostication|None|
|prev_ich_loc|44|6/25/2019|1…7; integer|Not possible in format.|No zeros|No history of ICH||||||||None|Localisation of brain hemorrhage|Often an important covariate in prognostication|None|
|prev_ich_etiology|45|6/25/2019|1…9; integer|Not possible in format.|No zeros|No history of ICH||||||||None|Underlying etiology of hemorrhagic stroke|Often an important covariate in prognostication|None|
|prev_sah|46|6/25/2019|1…3; integer|Not possible in format.|No zeros|No history of SAH||||||||None|Underlying etiology of subarachnoid hemorrhage|Often an important covariate in prognostication|None|
|prev_stroke_3|47|6/25/2019|1…16; integer|Not possible in format.|No zeros|No history of SAH||||||||None|Localisation of aneurysm|Often an important covariate in prognostication|None|
|prev_tbi_spec|48|6/25/2019|1…16; integer|Not possible in format.|No zeros|No history traumatic brain injury||||||||None|Type of traumatic brain injury|Often an important covariate in prognostication|None|
|epilepsy_spec|49|6/25/2019|1…6; integer|OTHER; Other type of epileptic seizure not listed, specified i text form|No zeros|No history of epilepsy||||||||None|Type of epilepsy|May be an important covariate in prognostication|None|
|gcs_motor_pre_hosp_v2|50|6/25/2019|0…6 & 9; integer|Not possible in format.|No data available|Not available/not recorded||||||||None|Level of movement pre hospital|Investigate association to prognosis and unresponsiveness|None|
|gcs_motor_admission_v2|51|6/25/2019|0…6 & 9; integer|Not possible in format.|No data available|Not available/not recorded||||||||None|Level of movement at admission|Investigate association to prognosis and unresponsiveness|None|
|normal_pupil_reactivity_v2|52|6/25/2019|0…3; integer|Not possible in format.|No data available|Not available/not recorded||||||||None|Pupil reactivity at admission|Investigate association to prognosis and unresponsiveness|None|
|early_hypotension_v2|53|6/25/2019|0…3; integer|Not possible in format.|Data missing|Not available/not recorded||||||||None|Presence of hypotension < 90mmHg at or prior to admission|Investigate association to prognosis and unresponsiveness|None|
|early_hypertension|54|6/25/2019|0…3; integer|Not possible in format.|Data missing|Not available/not recorded||||||||None|Presence of hypertension > 1800mmHg at or prior to admission|Investigate association to prognosis and unresponsiveness|None|
|late_hypotension|55|6/25/2019|0…3; integer|Not possible in format.|Data missing|Not available/not recorded||||||||None|Presence of hypotension < 90mmHg during ICU admission|Investigate association to prognosis and unresponsiveness|None|
|late_hypertension|56|6/25/2019|0…3; integer|Not possible in format.|Data missing|Not available/not recorded||||||||None|Presence of hypertension > 1800mmHg during ICU admission|Investigate association to prognosis and unresponsiveness|None|
|early_hypoxia|57|6/25/2019|0…3; integer|Not possible in format.|Data missing|Not available/not recorded||||||||None|Presence of hypoxia (SAT < 90%) at or prior to admission|Investigate association to prognosis and unresponsiveness|None|
|late_hypoxia|58|6/25/2019|0…3; integer|Not possible in format.|Data missing|Not available/not recorded||||||||None|Presence of hypoxia (SAT < 90%) during ICU admission|Investigate association to prognosis and unresponsiveness|None|
|hunt_and_hess_sah|59|6/25/2019|1..5; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Grading of SAH according to symptoms|Investigate association to prognosis and unresponsiveness|None|
|wfns_sah|60|6/25/2019|1..5; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Grading of SAH according to consiousness level measured by GCS|Investigate association to prognosis and unresponsiveness|None|
  
  
**Subset 4**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|4|Laboratory investigations|Jan-21|Tabular/Flat|Redcap (CSV/Excel)|104|0|Describing results of brain scans, X-ray, blood tests, electroencephalography and cerebrospinal fluid tests done during the admission|None|
  
  
*Features of Subset 4*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ct_brain_n|61|6/25/2019|0…15; real|Not possible in format.|No CT scan available|Not possible in format.||||||||None|Number of scans done|Paraclinical information |None|
|ct_brain_admission|62|6/25/2019|1…28; integer|OTHER: Other pathology not listed|No zeros|Not possible in format.||||||||None|Type of lesion on CT scan of brain|Prognostic feature|None|
|ct_brain_admission_anatomy|63|6/25/2019|1…21; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Localisation of leasion |Prognostic feature|None|
|cta_available|64|6/25/2019|0/1|Not possible in format.|No CTA available|Not possible in format.||||||||None|Presence af brain vascular scan|Paraclinical information |None|
|marshall|65|6/25/2019|1…6; integer|Not possible in format.|No zeros|No traumatic brain injury on first CT||||||||None|Grading of traumatic brain injury according to features on Ct scan of brain|Prognostic feature|None|
|Rotterdam_ct_score|66|6/25/2019|1…6; integer|Not possible in format.|No zeros|No traumatic brain injury on first CT||||||||None|Grading of traumatic brain injury according to features on Ct scan of brain|Prognostic feature|None|
|stroke_territory|67|6/25/2019|1…12; integer|Not possible in format.|No zeros|No sign of stroke on first CT of brain||||||||None|Localisation of ischemic stroke |Prognostic feature|None|
|aspect_score|68|6/25/2019|1…5; ineteger|Not possible in format.|No zeros|No sign of stroke on first CT of brain||||||||None|Grading of ischemic stroke according to CT scan features|Prognostic feature|None|
|stroke_hemor_score|69|6/25/2019|1…3; integer|Not possible in format.|No zeros|No sign of stroke on first CT of brain||||||||None|Presence of hemorrhagic conformation of ischemic stroke|Prognostic feature|None|
|stroke_territory_2|70|6/25/2019|1…12; integer|Not possible in format.|No zeros|No sign of old ischemic strokes on first CT of brain||||||||None|Presence of old ischemic strokes on CT|Prognostic feature|None|
|cta_occlusion|71|6/25/2019|1..15; integer|Not possible in format.|No zeros|No CTA available||||||||None|Presence of occlusion or clinically significant stenosis of brain vessels|Prognostic feature|None|
|cta_collaterals|72|6/25/2019|1…4; integer|Not possible in format.|No zeros|No CTA available||||||||None|Level of collateral flow|Prognostic feature|None|
|cta_atherosclerotic_burden|73|6/25/2019|1…3; integer|Not possible in format.|No zeros|No CTA available||||||||None|Level of atherosclerotic burden on CTA|Prognostic feature|None|
|cta_pathology_other|74|6/25/2019|1…10; integer|Not possible in format.|No zeros|No CTA available||||||||None|Other pathology on CTA|Prognostic feature|None|
|dsa|75|6/25/2019|1…4; integer|Not possible in format.|No zeros|No DSA available||||||||None|Available DSA and reason for performing DSA|Prognostic feature|None|
|dsa_TICI|76|6/25/2019|0…4; integer|Not possible in format.|0: No perfusion|No DSA available||||||||None|Grading of reperfusion after endovascular treatment of large vessel occclusion causing stroke|Prognostic feature|None|
|ct_venography|77|6/25/2019|0…6; integer|Not possible in format.|0: No cvt performed|No CTA available||||||||None|Localisation of venous sinus thrombosis|Prognostic feature|None|
|intracerebral_hemorhage_ty|78|6/25/2019|1 or 2|Not possible in format.|No zeros|No sign of ICH on first CT scan||||||||None|Type of ICH (typical versus atypical)|Prognostic feature|None|
|ich_location|79|6/25/2019|1…7; integer|Not possible in format.|No zeros|No sign of ICH on first CT scan||||||||None|Localisation of ICH on ct scan|Prognostic feature|None|
|abc_2_volume_round|80|6/25/2019|0.1…200; real|Not possible in format.|No zeros|No sign of round ICH on first CT scan||||||||CM3|Volume of round ICH|Prognostic feature|None|
|abc_2_volume_irreg|81|6/25/2019|0.1…200; real|Not possible in format.|No zeros|No sign of round ICH on first CT scan||||||||CM3|Volume of irregular ICH|Prognostic feature|None|
|intracerebral_hemorhage_i|82|6/25/2019|0…6; integer|Not possible in format.|0% mortality|No sign of ICH on first CT scan||||||||None|ICH score based on patient features and features of ICH (volume, localisation etc.)|Prognostic feature|None|
|modified_fisher_scale|83|6/25/2019|0…4; integer|Not possible in format.|No sah or IVH|No sign of SAH on first CT scan||||||||None|SAH grading predicting risk of complications|Prognostic feature|None|
|subdural_hemat_loc|84|6/25/2019|1…4; integer|Not possible in format.|No zeros|No sign of SDH on first CT scan||||||||None|Localisation of SDH|Paraclinical feature|None|
|subdural_hemat_thick|85|6/25/2019|0.1…200; real|Not possible in format.|No zeros|No sign of SDH on first CT scan||||||||CM|Thickness of SDH|Prognostic feature|None|
|epidural_hemat_loc|86|6/25/2019|1…3; integer|Not possible in format.|No zeros|No sign of EDH on first CT scan||||||||None|Localisation of EDH|Paraclinical feature|None|
|epidural_hemat_thick|87|6/25/2019|0.1…200; real|Not possible in format.|No zeros|No sign of EDH on first CT scan||||||||CM|Thickness of EDH|Prognostic feature|None|
|ivh_loc|88|6/25/2019|1…14; integer|Not possible in format.|No zeros|No sign of IVH on first CT scan||||||||None|Localisation of IVH|Paraclinical feature|None|
|ivh_score|89|6/25/2019|0…23; integer|Not possible in format.|No zeros|No sign of IVH on first CT scan||||||||None|Grading of IVH according to localisation and presence of hydrocephalus (high brain pressure)|Prognostic feature|None|
|ivh_volume|90|6/25/2019|1.2….99.5; real|Not possible in format.|No zeros|No sign of IVH on first CT scan||||||||None|Volume of Ich based on IVH score|Prognostic feature|None|
|diffus_axonal_injury|91|6/25/2019|1…3; integer|Not possible in format.|No zeros|No sign of DAI on first CT scan||||||||None|Severity of shearing leasions on CT|Prognostic feature|None|
|cerebral_edema |92|6/25/2019|1…4; integer|Not possible in format.|No zeros|No sign of cerebral edema on first CT scan||||||||None|Localisation of cerebral edema (subcortical focal/diffus vs. Cortical focal/diffus)|Prognostic feature|None|
|anoxic_ischemic_injury|93|6/25/2019|1…7; integer|Not possible in format.|No zeros|No sign of anoxic brain injury on first CT scan||||||||None|Level of anoxic injury apparent on CT scan|Prognostic feature|None|
|ct_midline_shift|94|6/25/2019|0.1….200; real|Not possible in format.|No zeros|No sign of midline shift on first CT scan||||||||mm|Size opf midline shift on ct scan|Prognostic feature|None|
|ct_brain_admission_2|95|6/25/2019|1…28; integer|OTHER: Other pathology not listed|No zeros|Not possible in format.||||||||None|Type of lesion on CT scan of brain|Prognostic feature|None|
|marshall_2|96|6/25/2019|1…6; integer|Not possible in format.|No zeros|No traumatic brain injury on last CT||||||||None|Grading of traumatic brain injury according to features on Ct scan of brain|Prognostic feature|None|
|Rotterdam_ct_score_2|97|6/25/2019|1…6; integer|Not possible in format.|No zeros|No traumatic brain injury on last CT||||||||None|Grading of traumatic brain injury according to features on Ct scan of brain|Prognostic feature|None|
|new_infarcts_last_ct|98|6/25/2019|0/1|Not possible in format.|No new infarcts compared to first CT|Only 1 CT scan available||||||||None|Presence of new ischemic stroke during admission from first ct scan|Prognostic feature|None|
|new_infarcts_territory|99|6/25/2019|1…12; integer|Not possible in format.|No zeros|No sign of stroke on last CT of brain||||||||None|Localisation of ischemic stroke |Prognostic feature|None|
|stroke_hemor_trans_2|100|6/25/2019|0/1|Not possible in format.|No hemorhagic transformation on ct scan|No sign of stroke on last CT of brain||||||||None|Presence of hemorhagic transformation of ischemic stroke on last CT compared to first ct|Prognostic feature|None|
|modified_fisher_scale_2|101|6/25/2019|0…4; integer|Not possible in format.|No sah or IVH|No sign of SAH on last CT scan||||||||None|SAH grading predicting risk of complications|Prognostic feature|None|
|eeg_n|102|6/25/2019|0…15; integer|Not possible in format.|No eeg available prior to index EEG|Not possible in format.||||||||None|Number of EEGs done during ICU aqdmission|Paraclinical test|None|
|first_eeg|103|6/25/2019|1…18; integer|Not possible in format.|No zeros|No EEG available||||||||None|EEG features as described by a certified neurophysiologist|Prognostic feature|None|
|first_eeg_reactivity|104|6/25/2019|1…8; integer|Not possible in format.|No zeros|No EEG available||||||||None|EEG apparent reaction to different stimulies as described|Prognostic feature|None|
|stess_score_nindex|105|6/25/2019|0…6; integer|Not possible in format.|No sign of status epilepticus|No sign of status epilepticus on first EEG||||||||None|Severity of status epilepticus based on defferent features|Prognostic feature|None|
|emse_eeg_nindex|106|6/25/2019|1…195; integer|Not possible in format.|No zeros|No sign of status epilepticus on first EEG||||||||None|Risk of mortality based on epidemiological features in patients with status epilepticus|Prognostic feature|None|
|last_eeg|107|6/25/2019|1…18; integer|Not possible in format.|No zeros|<=1 EEG available||||||||None|EEG features as described by a certified neurophysiologist|Prognostic feature|None|
|last_eeg_reactivity|108|6/25/2019|1…8; integer|Not possible in format.|No zeros|<=1 EEG available||||||||None|EEG apparent reaction to different stimulies as described|Prognostic feature|None|
|csf_analysis_specify|109|6/25/2019|1…6; integer|OTHER cause for abnormal csf not listet|No zeros|No abnormal csf analysis||||||||None|Cause of abnormal csf tests|Prognostic feature|None|
|chest_x_ray|110|6/25/2019|1…8; integer|Not possible in format.|No zeros|No chest x-ray available||||||||None|Features of chest x-ray described by radiologist|Paraclinical feature|None|
|ecg|111|6/25/2019|1…5; integer|Not possible in format.|No zeros|No ecg available||||||||None|Features of ECG|Paraclinical feature|None|
|blod_tests|112|6/25/2019|1…9; integer|Other abnormalities not listed|No zeros|Not possible in format.||||||||None|Abnormal blodd tests according to organ systems (e.g. lever tests, hematology etc.)|Paraclinical feature|None|
  
  
**Subset 5**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|5|Neurological exam at inclusion|Jan-21|Tabular/Flat|Redcap (CSV/Excel)|104|0|Clinical neurological exams with testing of brainstem reflexes, motor output, consioussness level from a clinical point of view, reaction to stimulies like pain, voice etc. |None|
  
  
*Features of Subset 5*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|date_examination|113|6/25/2019|YYYY-MM-DD|Not possible in format.|No zeros|Not possible in format.||||||||None|Date of index neurological examination|Investigate longitudinal effect.|None|
|time_examination|114|6/25/2019|H:M|Not possible in format.|No zeros|Not possible in format.||||||||None|Time of index neurological examination|Investigate longitudinal effect.|None|
|sedation|115|6/25/2019|1…3; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Was the patient sedated at time of examination|Important covariate when examining level of conscioussness |None|
|Sedative_drugs|116|6/25/2019|1…10; integer|Other drugs than listed|No zeros|Not possible in format.||||||||None|Name of sedative drug|Important covariate when examining level of conscioussness |None|
|Sedative_drugs_dosage|117|6/25/2019|0.1…300; real|Not possible in format.|No zeros|Not possible in format.||||||||mg or ug|Dosage of sedative drug|Important covariate when examining level of conscioussness |None|
|rass|118|6/25/2019|1…12; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Level of sedation based on clinical features|Important covariate when examining level of conscioussness |None|
|brainstem_reflexes|119|6/25/2019|1…4; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Presence/absence of 39 brainstem features|Prognostic feature|None|
|four_score_final|120|6/25/2019|0…16; integer|Not possible in format.|0: No brainstem reflexes, spontaneous respiration, motor output or eye movement.|Not possible in format.||||||||None|Verified score for evaluating level of concsioussnes in ICU patients based on score from 4 different features|Prognostic feature|None|
|intubation|121|6/25/2019|1 or 2|Not possible in format.|No zeros|Not intubated||||||||None|Orally intubated or tracheostomized|Clinical feature|None|
|gcs_score_final|122|6/25/2019|3…15; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Verified score for evaluating level of concsioussnes in patients with disorders of concsioussness based on score from 3 different features|Prognostic feature|Prognostic feature|
|command_following_consistent|123|6/25/2019|1…4; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Consistent presence of 5 command following features (e.g. blinking, gaze, visuel pusuit, nect/facial movement or limb movement)|Prognostic feature|None|
|command_following_inconsistent|124|6/25/2019|1…4; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Inconsistent presence of 5 command following features (e.g. blinking, gaze, visuel pusuit, nect/facial movement or limb movement)|Prognostic feature|None|
|spontaneous_motor_behavior_inconsistent|125|6/25/2019|1…4; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Spontaneous behavious scored by 8 different clinical features|Prognostic feature|None|
|nociception_final_score|126|6/25/2019|0…9; integer|Not possible in format.|0: no reaction to pain|Not possible in format.||||||||None|Reaction to pain stimulies|Prognostic feature|None|
|overall_the_degree_of_cons|127|6/25/2019|1…9; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Final level of concsioussness based on all the clinical features |Prognostic feature|None|
|treatment_level_1|128|6/25/2019|1…5; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Restriction to treatment level |Prognostic feature|None|
  
  
**Subset 6**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|6|MRI |Jan-21|Tabular/Flat|Redcap (CSV/Excel)|104|0|Describing structural MRI of brain with sites of lesion, form of lesions (hemmorhage, ischemia, diffus contusion etc.), which sequences were done and final conclusion of the scan described by a radiologist|None|
  
  
*Features of Subset 6*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|date_mri|129|6/25/2019|YYYY-MM-DD|Not possible in format.|No zeros|Not possible in format.||||||||None|Date of index mri|Logitudinel data|None|
|mri_field_strength|130|6/25/2019|1…3; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Quality of MRI (1.5 , 3 tesla or unknown)|Quality control of exam|None|
|mri_sequences|131|6/25/2019|1…10; integer|Other specific sequences than listed|No zeros|Not possible in format.||||||||None|Different radiologically predefined sequences adding different information about brain structure|Quality control of exam|None|
|mri_diagnosis|132|6/25/2019|1…25; integer|Other diagnosis than listed|No zeros|Major artefacts effecting mri interpretation||||||||None|Radiological diagnosis|Prognostic feature|None|
|mri_anatomy|133|6/25/2019|1…21; integer|Not possible in format.|No zeros|Major artefacts effecting mri interpretation||||||||None|Lesion to specific brain sites|Prognostic feature especially coupled to concsioussness level|None|
|stroke_territory_mri|134|6/25/2019|1…11; integer|Not possible in format.|No zeros|No stroke evident on MRI||||||||None|Territory of ischemic stroke according to main cerebral vessels|Prognostic feature |None|
|new_infarcts_mri|135|6/25/2019|0/1|Not possible in format.|0 = No|Major artefacts effecting mri interpretation||||||||None|Evidence of new infarcts om mri compared to last CT|Prognostic feature |None|
|stroke_hemor_trans_3|136|6/25/2019|0/1|Not possible in format.|0 = No|No stroke evident on MRI||||||||None|Evidence of hemorrhagic transformation of infarct|Prognostic feature |None|
|stroke_territory_4|137|6/25/2019|1…11; integer|Not possible in format.|No zeros|No old ischemic stroke evident on MRI||||||||None|Territory of old ischemic stroke according to main cerebral vessels|Prognostic feature |None|
|mr_angio_occlusion|138|6/25/2019|1…15; integer|Not possible in format.|No zeros|No MRI angiography available||||||||None|Territory of large vessel occlusion or cliniccaly significant stenosis|Prognostic feature - disease burden|None|
|mr_angio_other_pathology|139|6/25/2019|1…12; integer|Not possible in format.|No zeros|No MRI angiography available||||||||None|Other vessel disease not including occlusion or stenosis|Prognostic feature - disease burden|None|
|mr_venography|140|6/25/2019|1…6; integer|Not possible in format.|No zeros|No MRI venography available||||||||None|Venous thrombosis or other venous disease|Prognostic feature - disease burden|None|
|ich_location_2|141|6/25/2019|1…10; integer|Not possible in format.|No zeros|No ICH evident on mri||||||||None|Location of ich|Prognostic feature especially coupled to concsioussness level|None|
|subdural_hemat_loc_2|142|6/25/2019|1…4; integer|Not possible in format.|No zeros|No sign of SDH on mri||||||||None|Localisation of SDH|Paraclinical feature|None|
|subdural_hemat_thick_2|143|6/25/2019|0.1…200; real|Not possible in format.|No zeros|No sign of SDH on mri||||||||CM|Thickness of SDH|Prognostic feature|None|
|epidural_hemat_loc_2|144|6/25/2019|1…3; integer|Not possible in format.|No zeros|No sign of EDH on mri||||||||None|Localisation of EDH|Paraclinical feature|None|
|epidural_hemat_thick_2|145|6/25/2019|0.1…200; real|Not possible in format.|No zeros|No sign of EDH on mri||||||||CM|Thickness of EDH|Prognostic feature|None|
|diffus_axonal_injury_2|146|6/25/2019|1…3; integer|Not possible in format.|No zeros|No sign of DAI on mri||||||||None|Severity of shearing leasions on mri|Prognostic feature|None|
|cerebral_edema_2|147|6/25/2019|1…4; integer|Not possible in format.|No zeros|No sign of cerebral edema mri||||||||None|Localisation of cerebral edema (subcortical focal/diffus vs. Cortical focal/diffus)|Prognostic feature|None|
|anoxic_ischemic_injury_2|148|6/25/2019|1…7; integer|Not possible in format.|No zeros|No sign of anoxic brain injury mri||||||||None|Level of anoxic injury apparent on mri|Prognostic feature|None|
|midline_shift_mri|149|6/25/2019|0.1….200; real|Not possible in format.|No zeros|No sign of midline shift on mri||||||||mm|Size opf midline shift on mri|Prognostic feature|None|
  
  
**Subset 7**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|7|EEG|Jan-21|Tabular/Flat|Redcap (CSV/Excel)|104|0|Describing brain derived electrical signals measured by surface electrodes and response to different stimuli. |https://www.mayoclinic.org/tests-procedures/eeg/about/pac-20393875|
  
  
*Features of Subset 7*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|date_eeg|150|6/25/2019|YYYY-MM-DD|Not possible in format.|No zeros|Not possible in format.||||||||None|Date of index eeg|Logitudinel data|None|
|index_eeg_baseline|151|6/25/2019|1…18; integer|Not possible in format.|No zeros|No EEG available||||||||None|EEG features as described by a certified neurophysiologist|Prognostic feature|None|
|stess_score|152|6/25/2019|0…6; integer|Not possible in format.|No sign of status epilepticus|No sign of status epilepticus on index EEG||||||||None|Severity of status epilepticus based on different features|Prognostic feature|None|
|emse_eeg|153|6/25/2019|1…195; integer|Not possible in format.|No zeros|No sign of status epilepticus on index EEG||||||||None|Risk of mortality based on epidemiological features in patients with status epilepticus|Prognostic feature|None|
|eeg_reactivity|154|6/25/2019|1…7; integer|Not possible in format.|No zeros|No sign of status epilepticus on index EEG||||||||None|EEG apparent reaction to different stimulies as described|Prognostic feature|None|
  
  
**Subset 8**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|8|Pupillometry|Jan-21|Tabular/Flat|Redcap (CSV/Excel)|104|0|Descriping pupil characteristics (size, difference between the two pupils etc) and response to light|None|
  
  
*Features of Subset 8*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|date_pupillometry|155|6/25/2019|YYYY-MM-DD|Not possible in format.|No zeros|No pupillometry available||||||||None|Date of index pupillometry|Logitudinel data|None|
|sedative_pupillometry|156|6/25/2019|1…10; integer|Other drugs than listed|No zeros|No pupillometry available||||||||None|Name of sedative drug during pupillometry|Covariate when examining level of conscioussness |None|
|npi_right|157|6/25/2019|0…5; real|Not possible in format.|No reaction|No pupillometry available||||||||None|Neurological pupil index based on pupil reaction to light|Covariate when examining level of conscioussness |None|
|npi_left|158|6/25/2019|0…5; real|Not possible in format.|No reaction|No pupillometry available||||||||None|Neurological pupil index based on pupil reaction to light|Covariate when examining level of conscioussness |None|
|pupil_size_right|159|6/25/2019|0,1…20; real|Not possible in format.|No zeros|No pupillometry available||||||||mm|Pupil size|Covariate when examining level of conscioussness |None|
|pupil_size_left|160|6/25/2019|0,1…20; real|Not possible in format.|No zeros|No pupillometry available||||||||mm|Pupil size|Covariate when examining level of conscioussness |None|
|pupil_right_min|161|6/25/2019|0,1…20; real|Not possible in format.|No zeros|No pupillometry available||||||||mm|Minimum pupil size right|Covariate when examining level of conscioussness |None|
|pupil_left_min|162|6/25/2019|0,1…20; real|Not possible in format.|No zeros|No pupillometry available||||||||mm|Minimum pupil size left|Covariate when examining level of conscioussness |None|
|ch_right|163|6/25/2019|0…100; integer|Not possible in format.|No change|No pupillometry available||||||||%|Percentage of change in pupil size due to reaction to light, right side|Covariate when examining level of conscioussness |None|
|ch_left|164|6/25/2019|0…100; integer|Not possible in format.|No change|No pupillometry available||||||||%|Percentage of change in pupil size due to reaction to light, left side|Covariate when examining level of conscioussness |None|
|const_velocity_right|165|6/25/2019|0…10; real|Not possible in format.|No constriction|No pupillometry available||||||||mm/sec|Constriction velocity, right|Covariate when examining level of conscioussness |None|
|const_velocity_left|166|6/25/2019|0…10; real|Not possible in format.|No constriction|No pupillometry available||||||||mm/sec|Constriction velocity, left|Covariate when examining level of conscioussness |None|
|max_const_velocity_right|167|6/25/2019|0…10; real|Not possible in format.|No constriction|No pupillometry available||||||||mm/sec|Maximum constriction velocity, right|Covariate when examining level of conscioussness |None|
|max_const_velocity_left|168|6/25/2019|0…10; real|Not possible in format.|No constriction|No pupillometry available||||||||mm/sec|maximum constriction velocity, left|Covariate when examining level of conscioussness |None|
|latency_right|169|6/25/2019|0…10; real|Not possible in format.|No latency|No pupillometry available||||||||sec|Latency to light reaction, right|Covariate when examining level of conscioussness |None|
|latency_left|170|6/25/2019|0…10; real|Not possible in format.|No latency|No pupillometry available||||||||sec|Latency to light reaction, left|Covariate when examining level of conscioussness |None|
|dilatation_velocity_right|171|6/25/2019|0…10; real|Not possible in format.|No dilatation|No pupillometry available||||||||mm/sec|Dilatation velocity, right|Covariate when examining level of conscioussness |None|
|dilatation_velocity_left|172|6/25/2019|0…10; real|Not possible in format.|No dilatation|No pupillometry available||||||||mm/sec|Dilatation velocity, left|Covariate when examining level of conscioussness |None|
  
  
**Subset 9**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|9|Neurological exam at ICU discharge|Jan-21|Tabular/Flat|Redcap (CSV/Excel)|104|0|Clinical neurological features and conscioussnes level at time of discharge. Cause and date of death if patients die during ICU admission. Final diagnosis. |None|
  
  
*Features of Subset 9*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|date_examination_v2|173|6/25/2019|YYYY-MM-DD|Not possible in format.|No zeros|Not possible in format.||||||||None|Date of neurological examination at discharge from ICU or prior to death in ICU|Logitudinel data|None|
|time_examination_v2|175|6/25/2019|H:M|Not possible in format.|No zeros|Not possible in format.||||||||None|Time of discharge neurological examination|Investigate longitudinal effect.|None|
|treatment_level_2|174|6/25/2019|1…5; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Restriction to treatment level |Prognostic feature|None|
|sedation_v2|176|6/25/2019|1…3; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Was the patient sedated at time of examination|Important covariate when examining level of conscioussness |None|
|Sedative_drugs_v2|177|6/25/2019|1…10; integer|Other drugs than listed|No zeros|Not possible in format.||||||||None|Name of sedative drug|Important covariate when examining level of conscioussness |None|
|Sedative_drugs_dosage_v2|178|6/25/2019|0.1…300; real|Not possible in format.|No zeros|Not possible in format.||||||||mg or ug|Dosage of sedative drug|Important covariate when examining level of conscioussness |None|
|rass_v2|179|6/25/2019|1…12; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Level of sedation based on clinical features|Important covariate when examining level of conscioussness |None|
|brainstem_reflexes_v2|180|6/25/2019|1…4; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Presence/absence of 39 brainstem features|Prognostic feature|None|
|four_score_final_v2|181|6/25/2019|0…16; integer|Not possible in format.|0: No brainstem reflexes, spontaneous respiration, motor output or eye movement.|Not possible in format.||||||||None|Verified score for evaluating level of concsioussnes in ICU patients based on score from 4 different features|Prognostic feature|None|
|intubation_discharge|182|6/25/2019|1 or 2|Not possible in format.|No zeros|Not intubated||||||||None|Orally intubated or tracheostomized|Clinical feature|None|
|gcs_score_final_v2|183|6/25/2019|3…15; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Verified score for evaluating level of concsioussnes in patients with disorders of concsioussness based on score from 3 different features|Prognostic feature|Prognostic feature|
|command_following_consistent_v2|184|6/25/2019|1…4; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Consistent presence of 5 command following features (e.g. blinking, gaze, visuel pusuit, nect/facial movement or limb movement)|Prognostic feature|None|
|command_following_inconsistent_v2|185|6/25/2019|1…4; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Inconsistent presence of 5 command following features (e.g. blinking, gaze, visuel pusuit, nect/facial movement or limb movement)|Prognostic feature|None|
|spontaneous_motor_behavior_inconsistent_v2|186|6/25/2019|1…4; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Spontaneous behavious scored by 8 different clinical features|Prognostic feature|None|
|nociception_final_score_v2|187|6/25/2019|0…9; integer|Not possible in format.|0: no reaction to pain|Not possible in format.||||||||None|Reaction to pain stimulies|Prognostic feature|None|
|overall_the_degree_of_cons_v2|188|6/25/2019|1…9; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Final level of concsioussness based on all the clinical features |Prognostic feature|None|
|discharge_date_4|189|6/25/2019|YYYY-MM-DD|Not possible in format.|No zeros|Not possible in format.||||||||None|Date of hospitalk discharge|Logitudinel data|None|
|patient_dead_alive|190|6/25/2019|0/1|Not possible in format.|0 = no|Not possible in format.||||||||None|Is the patient discharged alive from ICU|Mortality|None|
|cause_of_death|191|6/25/2019|1…6; integer|Other cause than listed|No zeros|Not dead||||||||None|Cause of death|Mortality|None|
|final_diagnosis|192|6/25/2019|Diagnose code based on ICD-10|Not possible in format.|No zeros|Not possible in format.||||||||None|Etiology of admission|Prognostic|Validated diagnose codes based on ICD-10|
  
  
**Subset 10**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|10|3-month follow-up|Jan-21|Tabular/Flat|Redcap (CSV/Excel)|104|0|Description of daily function regained and level of indepency after admission at 3 months described by 3 different scales (CPC, GOS-E and mRS)|https://www.ivr-ias.ch/wp-content/uploads/2020/06/CPC_Scale.pdf; https://manual.jointcommission.org/releases/TJC2018A/DataElem0569.html; https://brohaut.github.io/2017/Post_GOS-E/|
  
  
*Features of Subset 10*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|date_at_follow_up_3mo|193|6/25/2019|YYYY-MM-DD|Not possible in format.|No zeros|Not possible in format.||||||||None|Date of 3 month followup|Logitudinel data|None|
|time_examination_3mo|194|6/25/2019|H:M|Not possible in format.|No zeros|Not possible in format.||||||||None|Time of 3 month followup|Logitudinel data|None|
|hospitalized_3mo|195|6/25/2019|0/1|Not possible in format.|0 = no|Not possible in format.||||||||None|Hospitalization since discharge and follow-up|Covariate which may effect folowup clinical status|None|
|hospitalization_cause_3mo|196|6/25/2019|1…3; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Cause of hospitalization (related or unrelated to admission cause)|Specification of other factor modifying follow up status|None|
|cpc_3months|197|6/25/2019|1…5; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Clinical staus at 3 month|Cerebral outcome|None|
|mrs_3mo|198|6/25/2019|1…6;integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Level of function according to mRS at 3 months|functional outcome at 3 months|None|
|gose_scoring_3mo|199|6/25/2019|1…8; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Level of function according to GOS-E at 3 months|functional outcome at 3 months|None|
|overall_the_degree_of_cons_2|200|6/25/2019|1…10; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Level of concsioussness ar 3 months|Concsioussness level at 3 months|None|
  
  
**Subset 11**  
  

|ID|Name|Last Update|Modality|Format|Size|Parent|Purpose|Link|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|11|12-month follow-up|Jan-21|Tabular/Flat|Redcap (CSV/Excel)|104|0|Description of daily function regained and level of indepency after admission at 12 months described by 3 different scales (CPC, GOS-E and mRS)|https://www.ivr-ias.ch/wp-content/uploads/2020/06/CPC_Scale.pdf; https://manual.jointcommission.org/releases/TJC2018A/DataElem0569.html; https://brohaut.github.io/2017/Post_GOS-E/|
  
  
*Features of Subset 11*  

|Name|ID|Date of Intro|Values|Meaning of Nan|Meaning of Zero|Meaning of blankvoid|Sparsity|Mean|std|Modality|Median|IQR|Parents|Unit|Definition|Purpose|Encoding|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|date_at_follow_up_12mo|201|6/25/2019|YYYY-MM-DD|Not possible in format.|No zeros|Not possible in format.||||||||None|Date of 12 month followup|Logitudinel data|None|
|time_examination_12mo|202|6/25/2019|H:M|Not possible in format.|No zeros|Not possible in format.||||||||None|Time of 12 month follow-up|Logitudinel data|None|
|hospitalized_12mo|203|6/25/2019|0/1|Not possible in format.|0 = no|Not possible in format.||||||||None|Hospitalization since 3 and 12 month follow-up|Covariate which may effect folowup clinical status|None|
|hospitalization_cause_12mo|204|6/25/2019|1…3; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Cause of hospitalization (related or unrelated to admission cause)|Specification of other factor modifying follow up status|None|
|cpc_12months|205|6/25/2019|1…5; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Clinical staus at 12 month|Cerebral outcome|None|
|mrs_12mo|206|6/25/2019|1…6;integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Level of function according to mRS at 12 months|functional outcome at 3 months|None|
|gose_scoring_12mo|207|6/25/2019|1…8; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Level of function according to GOS-E at 12 months|functional outcome at 3 months|None|
|overall_the_degree_of_cons_3|208|6/25/2019|1…10; integer|Not possible in format.|No zeros|Not possible in format.||||||||None|Level of concsioussness ar 12 months|Concsioussness level at 3 months|None|
  
