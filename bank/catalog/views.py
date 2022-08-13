from django.shortcuts import render
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Create your views here.
def uploadTransactionHtml(request):
    return render(request, "Transaction.html")

def uploadFileHtml(request):
    
    """
    if request.method == "POST":
        # Fetching the form data
        account_number = request.POST["account_number"]
        attachment = request.FILES["attachment"]
        dframe = pd.read_csv(attachment)

        print(dframe)
    """   
    return render(request, "test.html")