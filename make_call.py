# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 23:25:56 2020

@author: Aboli
"""

import os
from twilio.rest import Client

account_sid=os.environ[""]
auth_token = os.environ[""]

client = Client{account_sid,auth_token}

call = client.calls.create{
    to=os.environ["Myphoneno"],
    from_ = "bought number",
    url ="http://demo.twilio.com/docs.voice.xml"
    
    
    
 }