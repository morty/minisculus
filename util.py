#!/usr/bin/env python

import json
import httplib

def send_answer(answer, destination):
    body = json.dumps({'answer': answer})
    headers = {'Accept': 'application/json', 'Content-type': 'application/json'}

    conn = httplib.HTTPConnection('minisculus.edendevelopment.co.uk')
    conn.request('PUT', destination, body, headers)
    resp = conn.getresponse()
    if resp.status == 303:
        print "New location = %s" % resp.getheader('location')
    elif resp.status == 406:
        print "Wrong answer"
    else:
        print "Error"

