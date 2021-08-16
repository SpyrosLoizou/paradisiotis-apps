# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 13:25:59 2021

@author: sloizou
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.sidebar.image(my_path + '/Data/paralogo.png', use_column_width=True)


#Hide streamlit settings
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: green;'>Paradisiotis Dashboard</h1>", unsafe_allow_html=True)
st.title("")


st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:") 
select = st.sidebar.selectbox('Type of result', ['Top 5 selling products overall', 'Top 5 products per district', 'Top 5 products per Price Group', 'Recent Products ordered by customer', 'Sales Per Supervisor per month','Sales Per Customer monthly'])

df = pd.read_csv('Data/EXPORT2_Final.csv')

net=df.groupby('MaterialNumber').agg({'NetValue':'sum','MaterialDescription':'min'})
 
net.sort_values(
         by="NetValue",
         ascending=False,
    ).to_csv('sort_netvalue_sum.csv')

df2 = pd.read_csv('sort_netvalue_sum.csv')
 
#Top 5 selling products overall
if select == 'Top 5 selling products overall' :
    
    st.markdown("<h3 style='text-align: center; color: black;'>Top 5 selling products overall</h1>", unsafe_allow_html=True)
    #st.subheader("Top 5 selling products overall")
    fig = px.pie(df2, values=df2['NetValue'][:5], names=df2['MaterialDescription'][:5])
    st.plotly_chart(fig)
    
#Top 5 products per district
elif select == 'Top 5 products per district' :
    select_district = st.sidebar.selectbox('Select district', ['Nicosia', 'Famagusta', 'Larnaca', 'Limassol', 'Paphos'])
    if select_district == 'Nicosia':
        form = st.form(key='my-form')
        int_val = form.number_input('Enter how much products you want to see', min_value=1, max_value=15, value=5, step=1)
        submit = form.form_submit_button('Submit')
        
        st.write('Press submit to see the graph below')
            
        if submit: 
            st.markdown("<h3 style='text-align: center; color: black;'>Top products in Nicosia</h1>", unsafe_allow_html=True)
            #st.subheader("Top products in Nicosia")
            df[df['Salesdistrict'] == 'Nicosia'].groupby('MaterialNumber').agg({'NetValue':'sum','MaterialDescription':'min'}).to_csv('nicosia_dis.csv')
            df3 = pd.read_csv('nicosia_dis.csv')
    
            df3.sort_values(
                     by="NetValue",
                     ascending=False,
                ).to_csv('nicosia_district.csv')
            os.remove('nicosia_dis.csv') 
    
            df3 = pd.read_csv('nicosia_district.csv')
            fig = px.pie(df3, values=df3['NetValue'][:int_val], names=df3['MaterialDescription'][:int_val])
            st.plotly_chart(fig)
    
    elif select_district == 'Famagusta':
            form = st.form(key='my-form')
            int_val = form.number_input('Enter how much products you want to see', min_value=1, max_value=15, value=5, step=1)
            submit = form.form_submit_button('Submit')
            
            st.write('Press submit to see the graph below')
            
            if submit:     
                st.markdown("<h3 style='text-align: center; color: black;'>Top products in Famagusta</h1>", unsafe_allow_html=True)
                #st.subheader("Top products in Famagusta")
                df[df['Salesdistrict'] == 'Famagusta'].groupby('MaterialNumber').agg({'NetValue':'sum','MaterialDescription':'min'}).to_csv('famagusta_dis.csv')
                df3 = pd.read_csv('famagusta_dis.csv')
        
                df3.sort_values(
                         by="NetValue",
                         ascending=False,
                    ).to_csv('famagusta_district.csv')
                os.remove('famagusta_dis.csv')   
        
                df3 = pd.read_csv('famagusta_district.csv')
                fig = px.pie(df3, values=df3['NetValue'][:int_val], names=df3['MaterialDescription'][:int_val])
                st.plotly_chart(fig)
    
    elif select_district == 'Larnaca':
        
            form = st.form(key='my-form')
            int_val = form.number_input('Enter how much products you want to see', min_value=1, max_value=15, value=5, step=1)
            submit = form.form_submit_button('Submit')
            
            st.write('Press submit to see the graph below')
            
            if submit:
                st.markdown("<h3 style='text-align: center; color: black;'>Top products in Larnaca</h1>", unsafe_allow_html=True)
                #st.subheader("Top products in Larnaca")
                df[df['Salesdistrict'] == 'Larnaca'].groupby('MaterialNumber').agg({'NetValue':'sum','MaterialDescription':'min'}).to_csv('larnaca_dis.csv')
                df3 = pd.read_csv('larnaca_dis.csv')
        
                df3.sort_values(
                         by="NetValue",
                         ascending=False,
                    ).to_csv('larnaca_district.csv')   
                os.remove('larnaca_dis.csv') 
                
                df3 = pd.read_csv('larnaca_district.csv')
                fig = px.pie(df3, values=df3['NetValue'][:int_val], names=df3['MaterialDescription'][:int_val])
                st.plotly_chart(fig)
            
    elif select_district == 'Limassol':
        
            form = st.form(key='my-form')
            int_val = form.number_input('Enter how much products you want to see', min_value=1, max_value=15, value=5, step=1)
            submit = form.form_submit_button('Submit')
            
            st.write('Press submit to see the graph below')
            
            if submit:
                st.markdown("<h3 style='text-align: center; color: black;'>Top products in Limassol</h1>", unsafe_allow_html=True)
                #st.subheader("Top products in Limassol")
                df[df['Salesdistrict'] == 'Limassol'].groupby('MaterialNumber').agg({'NetValue':'sum','MaterialDescription':'min'}).to_csv('lim_dis.csv')
                df3 = pd.read_csv('lim_dis.csv')
        
                df3.sort_values(
                         by="NetValue",
                         ascending=False,
                    ).to_csv('limassol_district.csv')
                os.remove('lim_dis.csv')  
        
                df3 = pd.read_csv('limassol_district.csv')
                fig = px.pie(df3, values=df3['NetValue'][:int_val], names=df3['MaterialDescription'][:int_val])
                st.plotly_chart(fig)
            
    else: 
        form = st.form(key='my-form')
        int_val = form.number_input('Enter how much products you want to see', min_value=1, max_value=15, value=5, step=1)
        submit = form.form_submit_button('Submit')

        st.write('Press submit to see the graph below')

        if submit:
            st.markdown("<h3 style='text-align: center; color: black;'>Top products in Paphos</h1>", unsafe_allow_html=True)
            #st.subheader("Top products in Paphos")
            df[df['Salesdistrict'] == 'Paphos'].groupby('MaterialNumber').agg({'NetValue':'sum','MaterialDescription':'min'}).to_csv('paphos_dis.csv')
            df3 = pd.read_csv('paphos_dis.csv')
    
            df3.sort_values(
                     by="NetValue",
                     ascending=False,
                ).to_csv('paphos_district.csv')
            os.remove('paphos_dis.csv')  
    
            df3 = pd.read_csv('paphos_district.csv')
            fig = px.pie(df3, values=df3['NetValue'][:int_val], names=df3['MaterialDescription'][:int_val])
            st.plotly_chart(fig)
            
     
#Top 5 products per Price Group        
elif select == 'Top 5 products per Price Group' :
     select_type = st.sidebar.selectbox('Select type by..', ['Quantity', 'NetValue'])
     if select_type == 'Quantity':
        st.markdown("<h3 style='text-align: center; color: black;'>Top 5 products per Price Group by Quantity</h1>", unsafe_allow_html=True)
        #st.subheader("Top 5 products per Price Group by Quantity")
        price_group = df['PriceGroup'].unique()
        option_gr = st.selectbox('Select a price group', price_group)
        
        
        df[df['PriceGroup'] == option_gr].groupby('MaterialNumber').agg({'Quantity':'sum','MaterialDescription':'min'}).to_csv('pri_gr.csv')
     
        df3 = pd.read_csv('pri_gr.csv')
    
        df3.sort_values(
                     by="Quantity",
                     ascending=False,
                ).to_csv('price_group.csv')
        os.remove('pri_gr.csv')   
    
        df3 = pd.read_csv('price_group.csv')
             
        fig = px.bar(df3, x=df3['MaterialDescription'][:5], y=df3['Quantity'][:5])
        st.plotly_chart(fig)  
     elif select_type == 'NetValue':
        st.markdown("<h3 style='text-align: center; color: black;'>Top 5 products per Price Group by Net Value</h1>", unsafe_allow_html=True)
        #st.subheader("Top 5 products per Price Group by Net Value")
        price_group = df['PriceGroup'].unique()
        option_gr = st.selectbox('Select a price group', price_group)
        
        
        df[df['PriceGroup'] == option_gr].groupby('MaterialNumber').agg({'NetValue':'sum','MaterialDescription':'min'}).to_csv('pri_gr.csv')
     
        df3 = pd.read_csv('pri_gr.csv')
    
        df3.sort_values(
                     by="NetValue",
                     ascending=False,
                ).to_csv('price_group.csv')
        os.remove('pri_gr.csv')   
    
        df3 = pd.read_csv('price_group.csv')
             
        fig = px.bar(df3, x=df3['MaterialDescription'][:5], y=df3['NetValue'][:5])
        st.plotly_chart(fig)  
        
        
#Recent Products ordered by customer        
elif select == 'Recent Products ordered by customer' :
        st.markdown("<h3 style='text-align: center; color: black;'>Top products of customer by Quantity</h1>", unsafe_allow_html=True)
        #st.subheader("Top products of customer")
        payee = df['Name'].unique()
        option = st.selectbox('Select a customer',payee)
        
        df[df['Name'] == option].groupby('MaterialNumber').agg({'Quantity':'sum','MaterialDescription':'min'}).to_csv('payee.csv')
     
        df3 = pd.read_csv('payee.csv')
    
        df3.sort_values(
                     by="Quantity",
                     ascending=False,
                ).to_csv('payee_recent.csv')
        os.remove('payee.csv')   
    
        df3 = pd.read_csv('payee_recent.csv')
             
        fig = px.bar(df3, x=df3['MaterialDescription'][:5], y=df3['Quantity'][:5])
        st.plotly_chart(fig)
        
        st.markdown("<h3 style='text-align: center; color: black;'>Recent products ordered by customer</h1>", unsafe_allow_html=True)
        #st.subheader("Recent products ordered by customer")
               
        df[df['Name'] == option].groupby('MaterialNumber').agg({'Period/Date':'max','Quantity':'max','MaterialDescription':'max'}).to_csv('per.csv')
        df3 = pd.read_csv('per.csv')
        
        df3.sort_values(
                 by="Period/Date",
                 ascending=False,
            ).to_csv('period.csv')
        os.remove('per.csv')
        df3 = pd.read_csv('period.csv')
        st.table(df3[['MaterialNumber','MaterialDescription','Period/Date','Quantity']])
        
        
#Sales Per Supervisor per month        
elif select == 'Sales Per Supervisor per month' : 
        st.markdown("<h3 style='text-align: center; color: black;'>Sales Per Supervisor per month</h1>", unsafe_allow_html=True)       
        #st.subheader("Sales Per Supervisor per month")
        supervisor = df['SupervisorName'].unique()
        option_sup = st.selectbox('Select a Supervisor',supervisor)
        
        df[df['SupervisorName'] == option_sup].groupby('MaterialNumber').agg({'Period/Date':'max', 'NetValue':'sum'}).to_csv('sup_month.csv')
        df3 = pd.read_csv('sup_month.csv')
        
        df3['month'] = pd.DatetimeIndex(df3['Period/Date']).month
      
        
        df3.groupby('month').agg({'NetValue':'sum'}).to_csv('month_final.csv')
        os.remove('sup_month.csv')
        
        df3 = pd.read_csv('month_final.csv')
        
        fig = px.bar(df3, x=df3['month'], y=df3['NetValue'])
        st.plotly_chart(fig)
        
#Sales Per Customer monthly        
elif select == 'Sales Per Customer monthly' : 
        st.markdown("<h3 style='text-align: center; color: black;'>Sales Per Customer per month</h1>", unsafe_allow_html=True)       
        #st.subheader("Sales Per Customer per month")
        custom = df['Name'].unique()
        option_cus = st.selectbox('Select a Customer',custom)
        
        df[df['Name'] == option_cus].groupby('MaterialNumber').agg({'Period/Date':'max', 'NetValue':'sum'}).to_csv('cus_month.csv')
        df3 = pd.read_csv('cus_month.csv')
        
        df3['month'] = pd.DatetimeIndex(df3['Period/Date']).month
      
        
        df3.groupby('month').agg({'NetValue':'sum'}).to_csv('customer_final.csv')
        os.remove('cus_month.csv')
        
        df3 = pd.read_csv('customer_final.csv')
        
        fig = px.bar(df3, x=df3['month'], y=df3['NetValue'])
        st.plotly_chart(fig)

        
       

      

  
        
        
