

from conn.odbc_conn import odbcConn
from dateutil.relativedelta import relativedelta
import pandas as pd
import datetime as dt




def primary_function(patient_id):
    
    data_ref = dt.date.today() - dt.timedelta(days = dt.date.today().day - 1)
    

    db =  odbcConn('sqlite')
    
    data = db.select("""select * 
                     from blood_donation_hist 
                     where 
                         patient_id in ({patient_id}) 
                     and donation_date<='{data_ref}'""".format(patient_id = str(patient_id), 
                                                               data_ref = data_ref.strftime('%Y-%m-%d')))
    
    
    donation_date_max = db.select("""select max(donation_date) as donation_date
                     from blood_donation_hist 
                     where 
                         patient_id in ({patient_id}) 
                     and donation_date<='{data_ref}'""".format(patient_id = str(patient_id), 
                                                               data_ref = data_ref.strftime('%Y-%m-%d')))
    
    
    donation_date_max = pd.to_datetime(donation_date_max.donation_date, dayfirst=True).max()
    
    if donation_date_max.day > data_ref.day:
        dt_max_aux = donation_date_max + relativedelta(months = 1, days=-donation_date_max.day+1)
        months_since_last_donation = (data_ref.year - dt_max_aux.year) * 12 + (data_ref.month - dt_max_aux.month)
    

    
    
    
    donation_date_min = db.select("""select min(donation_date) as donation_date
                     from blood_donation_hist 
                     where 
                         patient_id in ({patient_id}) 
                     and donation_date<='{data_ref}'""".format(patient_id = str(patient_id), 
                                                               data_ref = data_ref.strftime('%Y-%m-%d')))
    
    donation_date_min = pd.to_datetime(donation_date_min.donation_date, dayfirst=True).max()

    
    if donation_date_min.day> data_ref.day:
        dt_min_aux = donation_date_min + relativedelta(months = 1, days=-donation_date_min.day+1)
        months_since_first_donation = (data_ref.year - dt_min_aux.year) * 12 + (data_ref.month - dt_min_aux.month)
    
    
    
    
    data = db.select("""select count(*) quant, sum(volume_donated_cc) as vol
                     from blood_donation_hist 
                     where 
                         patient_id in ({patient_id}) 
                     and donation_date<='{data_ref}'""".format(patient_id = str(patient_id), 
                                                               data_ref = data_ref.strftime('%Y-%m-%d')))
    
    
    number_of_donations = data.quant.max()
    total_volume_donated_cc = data.vol.max()
    
    db.close()
    
    return {"months_since_last_donation": months_since_last_donation, 
                    "number_of_donations": number_of_donations, 
                    "total_volume_donated_cc": total_volume_donated_cc, 
                    "months_since_first_donation": months_since_first_donation}
