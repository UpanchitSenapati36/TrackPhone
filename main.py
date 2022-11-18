#import packages
import phonenumbers
from phonenumbers import geocoder

#create a variable and store the number with the country extention 
number="+91xxxxxxxxxx"

#geocoder finds the location of the number
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber ,"en"))

#carrier finds the service provider of the number
from phonenumbers import carrier
service_nmber = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_nmber,"en"))