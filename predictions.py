import pandas as pd
from joblib import load

model = load(r'assets\model.joblib')
scaler_object = load(r'assets\scaler.joblib')

def predict(user_input):

    def scaling_data(user_input):

        def processed_inputs(user_input):
            expected_cols = [
                'credit_utilization_ratio',
                'loan_to_income',
                'average_dpd',
                'loan_tenure_months',
                'sanction_amount',
                'number_of_open_accounts',
                'age',
                'delinquency_ratio',
                'loan_purpose_Education',
                'loan_purpose_Home',
                'loan_purpose_Personal',
                'residence_type_Owned',
                'residence_type_Rented',
                'loan_type_Unsecured'
                ]
            

            df = pd.DataFrame(0, columns=expected_cols, index=[0])

            df['loan_to_income'] = user_input['loan_amount']/user_input['income']
            df['delinquency_ratio'] = user_input['delinquent_months']/user_input['loan_tenure_months']
            
            if user_input['delinquent_months'] != 0:
                df['average_dpd'] = user_input['total_dpd']/user_input['delinquent_months']

            else: 
                df['average_dpd'] = 0

            rem_data = ['loan_amount','delinquent_months','total_dpd','income']

            for key in rem_data:
                del user_input[key]

            for x,y in user_input.items():

                if isinstance(y, int):
                    df[x] = y

                if isinstance(y, str):
                    if x == 'loan_purpose':

                        if y == 'Education':
                            df['loan_purpose_Education'] = 1
                        
                        elif y == 'Home':
                            df['loan_purpose_Home'] = 1
                        
                        elif y == 'Personal':
                            df['loan_purpose_Personal'] = 1

                    
                    if x == 'residence_type':

                        if y == 'Owned':
                            df['residence_type_Owned'] = 1
                        
                        elif y == 'Rented':
                            df['residence_type_Rented'] = 1
                        

                    if x == 'loan_type':

                        if y == 'Unsecured':
                            df['loan_type_Unsecured'] = 1

            
            df = df[expected_cols]
            
            return df


        df = processed_inputs(user_input)

        for col in ['number_of_open_accounts', 'number_of_closed_accounts', 'enquiry_count',
        'credit_utilization_ratio', 'age', 'number_of_dependants',
        'years_at_current_address', 'zipcode', 'sanction_amount',
        'loan_tenure_months', 'bank_balance_at_application', 'loan_to_income',
        'delinquency_ratio', 'average_dpd']:
            
            if col not in df.columns:
                df[col] = None

        cols_to_scale = ['number_of_open_accounts', 'number_of_closed_accounts', 'enquiry_count',
        'credit_utilization_ratio', 'age', 'number_of_dependants',
        'years_at_current_address', 'zipcode', 'sanction_amount',
        'loan_tenure_months', 'bank_balance_at_application', 'loan_to_income',
        'delinquency_ratio', 'average_dpd']


        scaler_tool = scaler_object['scaler']

        df[cols_to_scale] = scaler_tool.transform(df[cols_to_scale])

        df = df.dropna(axis=1)

        scaled_df = df

        return scaled_df

    scaled_df = scaling_data(user_input)

    prediction = model.predict(scaled_df)

    return prediction