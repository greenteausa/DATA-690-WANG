# Individual Project

Find an issue that you are passionate about or are interested in as the topic for this exploratory data analysis project.

Make sure there are publicly available data about this issue to perform exploratory analysis.

The analysis should include descriptive statistics, data visualization, and optionally statistical inference.

## Deliverable #1 - Project Proposal in Markdown format

Write and submit a research proposal in the **Markdown** format that answers the following questions:

### 1. What is your issue of interest (provide sufficient background information)?

There are about 1.7 million people develop sepsis and 270,000 people die from sepsis every year in US. Sepsis is a kind of acute and life-threatening disease and needs to be diagnosed and treated quickly to avoid further damages in tissue and organs. Delayed treatment can lead to death. If the sepsis could be predicted at early stage, it could be very helpful for many patients.

Sepsis is caused by the body's overactive reaction on infection usually caused by bacteria. The infection always starts with a small cut that then gets infected. Later on, the infection spreads in lung, stomach, kidney or bladder. Risk factors of sepsis include age, weak immune system, chronic conditions. 

The medical diagonosis on sepsis involves checking a variety of infectious pathogens and other parameters including vital signs, lab test results. These features are quite diverse among individuals, which makes it chanllege to extract important features. This project aims to analysis the data and try to extract important features for sepsis prediction.



### 2. Why is this issue important to you and/or to others?
The early prediction could help the doctor make valuable and on-time treatment. This could also help to better allocate medical resources to the patient with signs of sepsis. As such, it not only stops further deterioration of sepsis, but also save medical resources.



### 3. What questions do you have in mind and would like to answer?

I want to check
#1 whether the ICULOS (ICU length-of-stay hours since ICU admit) has relationship with the patient's age, since the older people could have low immunity, or there is some other tendance acccording to age.
#2 whether man has more chance to get sepsis than women.
#3 whether the BUN(Blood urea nitrogen), Cretinine, WBC, Hgb(Hemoglobin), Bilirubin_total, glucose and platelets show some diffrence between the people with and without sepsis.


### 4. Where do you get the data to help answer your questions? 
My data is from: https://physionet.org/content/challenge-2019/1.0.0/, which is open-source and can be legally downloaded.
The data is named "Early Prediction of Sepsis from Clinical Data". I am interested how sepsis could be early predicted, and what's the difference in the outcome between early predict and normal predict.
I want to know How to apply machine learning model and predict the future dataset, maybe very challeging.


### 5. What will be your unit of analysis (for example, patient, organization, or country)? Roughly how many units do you expect to analyze?
I will use the patients' medical lab result for analysis. patient is the unit. The dataset includes about 40,000 patients. For each patient, there are several different time points when the vital signs and other measurements were taken to monitor the patients' physiological status. 

### 6. What variables/measures do you plan to use in your analysis?
ICULOS(ICU length-of-stay(hours since ICU admit), HospAdmTime, Age, Gender, SepsisLable.
BUN(Blood urea nitrogen), Cretinine,WBC,Hgb(Hemoglobin), Bilirubin_total, glucose and platelets have some diffrence between the people with and withou sepsis.

### 7. What kinds of techniques do you you plan to use (for example, summary statistics, scatter plot, bar chart, chi-squared test)? 
I plan to mainly use Pandas, OS, Numpy, Matplotlib, Seaborn, and Statsmodels to conduct summary statistics. The results will be visualized by scatter plot, bar chart.

### I will review your proposal and provide feedback before you start the actual work.
