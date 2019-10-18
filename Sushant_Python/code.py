# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)



# --------------
# code starts here

banks = bank.drop(columns = 'Loan_ID')
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode, inplace= True)
print(banks.isnull().sum())



# --------------
# Code starts here
avg_loan_amount = banks.pivot_table(values = ['LoanAmount'], index = ['Gender','Married','Self_Employed'], aggfunc = np.mean)
print(avg_loan_amount)



# code ends here



# --------------
# code starts here
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)
# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]
# print percentage of loan approved for self employed
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]
#print percentage of loan for non self employed
print (percentage_nse)



# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x : int(x)/12)

big_loan_term = len(loan_term[loan_term >= 25])

print(big_loan_term)

# code ends here


# --------------
# code starts here
column_show = ['ApplicantIncome', 'Credit_History']
loan_groupby = banks.groupby(['Loan_Status'])

mean_values = loan_groupby.agg([np.mean])
print(mean_values)



# code ends here


