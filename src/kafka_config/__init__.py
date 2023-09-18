
import os


#Authentication related 

SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"

#cloud API related 

API_KEY = "YMLIX4vcgv4LHMQCWHFTHNKNTH7"
API_SECRET_KEY = "uXURwdssncEcdcnvBcuMUlK+34jhvfYVGjdK+jmUSSmO7YoX8KSGolkdcYavhs8Wwcdvhhj++NQVfCvdvjLaCdlyy"
BOOTSTRAP_SERVER = "pkc-41psjnc56.asijjhhhacdcdcdc-souccbdjcth1.gcpdcdjjsuhncdc.confluehjjhjnt.cloud:9092"



#SCHEMA related keys 
ENDPOINT_SCHEMA_URL  ="https://psrccjs-1sxJGFG4SKZI3TW"
SCHEMA_REGISTRY_API_SECRET = "n0TXbVAcdcbefP60kJdvsdjfPoycOqKGEr00vRhAWgi+rJbEbpDbTmBdcbdcjdAtPS6PeGRcdjcbdiOwS4c20P"


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

