
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from catalog.api.uploadTransaction.serializers import uploadTransactionSerializer
import csv
import smtplib
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from catalog.models import Transaction
from django.core.mail import (
    EmailMultiAlternatives,
    EmailMessage
)
from django.shortcuts import render

from django.core.mail import send_mail




class uploadTransactionViewSet(APIView):

    def setTransaction(self, number, txns):
        try :

            objs = []

            for i in txns.index: 
                print(txns["date"][i])
                print(txns["transaction"][i])
                objs.append(
                    Transaction(
                        account_number = number,
                        date = str(txns["date"][i]),
                        transaccion =str(txns["transaction"][i])
                    )
                )
            Transaction.objects.bulk_create(objs)
            msg = 'true'
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            msg = err
            raise Exception("ERROR EN INSERT")
        return msg



    def getFormatEmail(self,to_sender, totalBalance, credit, debit,  stMonth):
        content = ("""<body style="margin:0;padding:0;"><table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;font-family: Arial, san-serif ">
            <tr><td align="center" style="padding:0;"><table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
            <tr><td style="padding:0;"><table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
            <tr><td align="center" style="padding:40px 0 30px 0;background:#455B83; color:#FFFFFF; font-size: 30px">Resumen de transacciones</td>
            </tr><tr><td style="padding:36px 30px 42px 30px;"><table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0; text-align:center"><tr><td style="padding:20px 30px 20px 30px;">Total balance is """+ "{:.2f}".format(totalBalance) +"""
            </td></tr></table><table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0; text-align:center">
            <tr><td style="padding:20px 30px 20px 30px;">Avarage debit amount: """+ "{:.2f}".format(debit) +"""
            </td><td style="padding:20px 30px 20px 30px;"> Avarage credit amount: """+ "{:.2f}".format(credit) +"""
            </td> </tr></table><table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0; text-align:left">
            <tr><td style="padding:20px 30px 20px 30px;">"""+ stMonth +"""</td></tr></table></td></tr><tr><td align="center" style="padding: 25px 45px;background:#455B83; color:#FFFFFF; font-size: 30px; text-align: right; color:#00C7B1">Stori </td></tr></table></td></tr></table></td></tr></table></body>""")
        
        #serializer = uploadTransactionSerializer(data=request.data)
        try:
            print(settings.EMAIL_HOST_USER)
            subject, from_email, to = "Resumen de transaccion", settings.EMAIL_HOST_USER, [to_sender]
            msg = EmailMultiAlternatives(subject, 'BANK',from_email, to)
            msg.attach_alternative(content, "text/html")
            msg.send()
        except smtplib.SMTPException as e:
            print(str(e))  
        return content

    def getTransacctions(self,attachment):
        MonthList = {
            '1': 'Junary',
            '2': 'February',
            '3': 'March',
            '4': 'April',
            '5': 'May',
            '6': 'June',
            '7': 'July',
            '8': 'August',
            '9': 'September',
            '10': 'Octuber',
            '12': 'November',
            '13': 'December'
        }

        dframe = pd.read_csv(attachment)
        transaction = dframe
        sub = '-'
        dframe["indexes"] = dframe["transaction"].apply(str).str.find(sub)
        dframe['month'] = dframe['date'].str.slice(0, 2).replace({'/':''},regex=True)
        grupbyData = dframe.groupby('month')["month"].count().reset_index(name="count")
        dc = dframe.loc[dframe['indexes'] ==-1, ["transaction"]]
        dd = dframe.loc[dframe['indexes']==0, ["transaction"]]
        credit =  dc['transaction'].sum()/len(dc)
        debit = dd['transaction'].sum()/len(dd)
        totalBalance = dframe['transaction'].sum()
        stMonth = ""
        for i in grupbyData.index: 
            print("mont")
            print(grupbyData["month"][i])
            
            strCount = str(grupbyData["count"][i])
            print(strCount)
            for item in MonthList:
                if item == grupbyData["month"][i]:
                    stMonth = stMonth + "Number of transaction in " + MonthList[item] + ": " + strCount + " </br>" 
        return totalBalance, credit, debit,  stMonth , transaction

    def post(self,request, *args, **kwargs): 
        result = {
            'success':True
        }
       
        account_number = request.POST["account_number"]
        to_sender = request.POST["email"]
        attachment = request.FILES["attachment"]
        totalBalance, credit, debit,  stMonth , transaction = self.getTransacctions(attachment)
        res = self.setTransaction(account_number, transaction)
        if res == 'true':
            self.getFormatEmail(to_sender, totalBalance, credit, debit,  stMonth)
        #print(totalBalance)

        #gd = dframe.groupby('date')
        #print(gd.first())
        #print(dframe.shape)
        #print(dframe.head(1))
        #uploadedFile = request.FILES["attachment"]
       
        
        return render(request, "Transaction.html")
        #return Response(result,status=status.HTTP_201_CREATED)

    def get(self,request, *args, **kwargs):
        result = {
            'success' : True
        }
        return Response(result,status=status.HTTP_201_CREATED)
        