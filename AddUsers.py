from suds.client import Client
from suds.wsse import *
from getpass import getpass
import pprint
from xml.etree import ElementTree

def getUsersToMessage():
    username = input("Username: ")
    password = input ("Password: ")
    #password = getpass()
    url = 'https://login.swift-kanban.com/axis2/services/TeamMemberService?wsdl'
    client = Client(url )#retxml = True)
    security = Security()
    token = UsernameToken(username, password)
    security.tokens.append(token)
    client.set_options(wsse=security)
    result = client.service.getUserData(username, username)
    #tree = ElementTree.fromstring(result.content)
    pprint.pprint(result[0]["_emailAddress"])

def addUser():
    username = input("Username: ")
    password = input("Password: ")
    firstName = input("What is the new users first name? ")
    lastName = input("What is the new users last name? ")
    email = input("What is the email associated with new account? ")
    role = input("What will this users role be? (member, admin, reader, etc.) ")
    url = 'https://login.swift-kanban.com/axis2/services/TeamMemberService?wsdl'
    client = Client(url)
    security = Security()
    token = UsernameToken(username, password)
    security.tokens.append(token)
    client.set_options(wsse=security)
    user = client.service.addUser(username, [firstName, lastName, email, email, role, "Central Time"])


#getUsersToMessage()
addUser()