# Individual Project

Find an issue that you are passionate about or are interested in as the topic for this exploratory data analysis project.

Make sure there are publicly available data about this issue to perform exploratory analysis.

The analysis should include descriptive statistics, data visualization, and optionally statistical inference.

## Deliverable #1 - Project Proposal in Markdown format

Write and submit a research proposal in the **Markdown** format that answers the following questions:

### 1. What is your issue of interest (provide sufficient background information)?

I know sepsis is a kind of acute and serious disease and hard to diagnose which could delay the treatment. If the sepsis could be predicted on early stage, it  could be very helpful for many patients.
The medical diagonosis on sepsis involves checking a variety of infectious pathogens and other parameters including vital signs, lab test results. These features are quite diverse among individuals, which makes it chanllege to extract important features. This project aims to analysis the data and try to extract important features for sepsis prediction.



### 2. Why is this issue important to you and/or to others?
The early prediction could help the doctor make valuable and on-time treatment, and most important which could help to allocate medical resource to the patient with signs of sepsis, stop further detoration and save the medical resource.



### 3. What questions do you have in mind and would like to answer?

I want to see whether the ICULOS(ICU length-of-stay(hours since ICU admit) has relationship with the patient's age, since the older people could have low immunity, or there is some other tendance acccording to age.
I want to see whether man has more chance to get sepsis  then women.
I want to see whether the BUN(Blood urea nitrogen), Cretinine, WBC, Hgb(Hemoglobin), Bilirubin_total, glucose and platelets have some diffrence between the people with and withou sepsis.


### 4. Where do you get the data to help answer your questions? 
My data is from: https://physionet.org/content/challenge-2019/1.0.0/, which is open-source and can be legally downloaded.
The data is named "Early Prediction of Sepsis from Clinical Data". I am interested how sepsis could be early predicted, and what's the difference in the outcome between early predict and normal predict.
I want to know How to apply machine learning model and predict the future dataset, maybe very challeging.


### 5. What will be your unit of analysis (for example, patient, organization, or country)? Roughly how many units do you expect to analyze?
I will use the patients' medical lab result for analysis.

### 6. What variables/measures do you plan to use in your analysis?
ICULOS(ICU length-of-stay(hours since ICU admit), HospAdmTime, Age, Gender, SepsisLable.
BUN(Blood urea nitrogen), Cretinine,WBC,Hgb(Hemoglobin), Bilirubin_total, glucose and platelets have some diffrence between the people with and withou sepsis.

### 7. What kinds of techniques do you you plan to use (for example, summary statistics, scatter plot, bar chart, chi-squared test)? 
I plan to mainly use Pandas, OS, Numpy, Matplotlib, Seaborn, and I plan to use someothers if needed.

I will review your proposal and provide feedback before you start the actual work.
