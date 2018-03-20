#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 19:23:21 2018

@author: ddediu
"""

import pandas, adherer

# Load the test dataset
df = pandas.read_csv('./test-dataset.csv', sep='\t', header=0)

# Change the column names:
df.rename(columns={'ID': 'patientID', 
                   'DATE': 'prescriptionDate', 
                   'PERDAY': 'quantityPerDay', 
                   'CLASS': 'medicationType', 
                   'DURATION': 'prescriptionDuration'}, 
inplace=True)


# Tests:
#x = adherer.__call_adhereR(df, 'CMA1', 'patientID', 'prescriptionDate', 'prescriptionDuration', 
#                followup_window_start_type = 'numeric', followup_window_start = 0, followup_window_start_unit = "days",
#                followup_window_duration_type = 'numeric', followup_window_duration = 365*2, followup_window_duration_unit = "days",
#                observation_window_start_type = 'numeric', observation_window_start = 30, observation_window_start_unit = "days",
#                observation_window_duration_type = 'numeric', observation_window_duration = 365, observation_window_duration_unit = "days",
#                plot_show = True, plot_patients_to_plot = [2,3],
#                save_event_info = True, path_to_adherer = '../')

#y = call_adhereR(df, 'plot_interactive_cma', 
#                 ID_colname='patientID', event_date_colname='prescriptionDate', event_duration_colname='prescriptionDuration',
#                 path_to_adherer = '../') 


testcma = adherer.CMA0(df, 
                       ID_colname='patientID', 
                       event_date_colname='prescriptionDate', 
                       event_duration_colname='prescriptionDuration',
                       event_daily_dose_colname='quantityPerDay',
                       medication_class_colname='medicationType',
                       path_to_adherer = '../')
testcma.plotInteractive(patient_to_plot=3)

