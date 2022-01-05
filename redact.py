###########################################################################################
## CLASS : CPSC-449-section-1
## ASSIGNMENT: 1 (HTTP Client and Server with FOAAS and PurgoMalum)
## GROUP: Section 01 (Wednesday) - Group 6
## STUDENTS INFORMATION FROM Group 6::
    # Nidhi Shah- 
    # Priyanka Kadam 
    # Robert Nguyen 

##########################################################################################
########### imporitng require modules #################################
import os
import sys
import http.client
import json
import urllib.parse

#####################################################################

def fooasConnection(path):
    """ fooasConnection function
         -- Connect FOOAS API..
         -- Request a json response from FOAAS for the path provided by user..
         -- Convert the data from FOAAS API response to read in dictionary..
         -- Get the message from Dictionary..
         -- Pass the unprofessional message to PurgoMalum API by calling purgoApiConnection function..
         -- Create a result as dictionary with professional message from purgoApiConnection and
                with subtitle from FOAAS API result..
         -- return that result dictionary """
    ################# FOOAS ##################
    # creating a connection with FOOAS server
    #for FOAAS
    connection = http.client.HTTPSConnection('foaas.com')

    #headers for FOAAS : need to make sure the request to FOAAS
                         #response comes in json format.
                         #providing to FOAAS while sending request.
    header= {'Accept':'application/json'}

    #send FOOAS request with path recieved from user, and with headers
    connection.request('GET',path,headers=header)
    #Get response from FOOAS for the request that just sent
    r= connection.getresponse()

    #read the response
    data=r.read()
    #retrieve data in dict object
    result=json.loads(data)
    #get the message field value from dict object named result
    msg=result.get('message')
    #encode the message
    text=urllib.parse.quote(msg)


    #Now call the purgoApiConnection function with passing the message
    # here message is a text string that need to convert into profession message
    purresult=purgoApiConnection(text)

    # Create a dictionary with professonal message and its subtitle
    finaloutput={}
    finaloutput['message']=purresult['result']
    finaloutput['subtitle']=result['subtitle']

    return finaloutput

#######################################################################################
def purgoApiConnection(text):

    """ purgoApiConnection function
         -- Connect PurgoMalum API..
         -- Request a response from PurgoMalum for the unprofessional message recieved from fooasConnection function..
         -- Convert the data from PurgoMalum API response to read in dictionary..
         -- return that professional message in dictionary to fooasConnection function.."""

    ################## purgomalum ###################
    # creating a connection with purgomalum server
    #for purgomalum
    purgocon=http.client.HTTPSConnection('www.purgomalum.com')
    # creating a path nthat eed for request purgomalum
    purgopath='/service/json?text='+text

    #send purgomalum request with path created from fix path + text,
    purgocon.request('GET',purgopath)

    #Get response from purgomalum for the request that just sent
    r1=purgocon.getresponse()

    #Retrieve the data from HTTP response
    finalresult=json.loads(r1.read())
    return finalresult

#####################################################################################
#checking the redact file call is direct from command line or from import module
if __name__ == '__main__':
    #checking the user have given the path or not
    if len(sys.argv)<=1:
        # providing the message to user to give the path
        print("Usage: redact URL")
    else:
        #getting the path information and calling the FOOAS server with path value
        path=sys.argv[1]
        # printing the result of profession message with indentation in commandline
        print(json.dumps(fooasConnection(path),indent=4))
