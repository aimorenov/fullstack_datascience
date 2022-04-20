import pandas as pd
import numpy as np

# Convert number coded race to text
def race_code_fn(ls):
    if ls == 1:
        code = "African American"
    elif ls == 2:
        code = "Caucasian_American"
    elif ls == 3:
        code = "Hispanic_American"
    elif ls == 4:
        code = "Asian_American"
    elif ls == 5:
        code = "Native_American"
    else:
        code = "Other"
    return code

# Dataframe of field coded equivalence
field_coded = ['Law', 'Math', 'Social Science/Psychologist', 'Medical/Pharmaceuticals/Biotech','Engineering',
             'English/Creative Writing/Journalism','History/Religion/Philosophy',
             'Business/Econ/Finances', 'Education, Academia ', 'Biological Sciences/Chemistry/Physics', 'Social work', 'Undergrad/undecided',
             'Political Science/International Affairs ', 'Film', 'Fine Arts/Arts Administration', 'Languages', 'Architecture', 'Other']

field_coded_df = pd.DataFrame({'field_cd': range(1,19), 'field_cd_name': field_coded})

# List and dataframe of interests coded
interests_ls = ["sports", "tvsports", "exercise", "dining", "museums", "art", "hiking", "gaming", "clubbing", "reading",
 "tv", "theater", "movies", "concerts", "music", "shopping", "yoga"]

interests_coded_df = pd.DataFrame({'interest': range(0,len(interests_ls)), 'interest_name': interests_ls}) 

# List of 20 color palette
palette_20 =  ["#1F77B4","#FF7F0E","#2CA02C","#D62728", "#9467BD", "#8C564B", "#E377C2", "#7F7F7F", "#BCBD22", "#17BECF", "#AEC7E8", "#FFBB78", "#98DF8A", "#FF9896", "#C5B0D5", "#C49C94", "#F7B6D2", "#C7C7C7", "#DBDB8D", "#9EDAE5"]