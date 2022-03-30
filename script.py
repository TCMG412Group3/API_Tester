import requests
import sys

urlbase = input("Enter the hostname(including https), if you mess it up i'm not doing anything helpful:")
#urlbase = 'https://test-enviroment.yatagansabre.repl.co'

def tester(endpoint, exresult, exstatus):
  #combines everything to function
  url = urlbase + endpoint
  
  #print(url) #placeholder, here to make sure it works
  r = requests.get(url) #posts the url and then takes the "output" to variable r
  
  if r.status_code == exstatus:
    if exstatus == 200:
      try:
        r = r.json() #converts it to a diciontary
      except:
        return False
      if r["output"] == exresult:  #gets the value attatched to the output
        return True  
    else:
      return True
  else:
    return False
#MD5
print("Starting MD5 Testing")
print(tester("/md5/test", "098f6bcd4621d373cade4e832627b4f6", 200))
print(tester("/md5/!!!!", "98abe3a28383501f4bfd2d9077820f11", 200))
print(tester("/md5/-23123", "98454b6dcebcf2a62b34f8cca54ef743", 200))  

#Factorial
print("Starting Factorial Testing")
print(tester("/factorial/14", 87178291200, 200))
print(tester("/factorial/5", 120, 200))
print(tester("/factorial/03", 6, 200))
print(tester("/factorial/0.45", None, 404))
print(tester("/factorial/-45", None, 404))
print(tester("/factorial/hello", None, 404))


#Fibonacci
print("Starting Fibonacci Testing")
print(tester("/fibonacci/5", [0,1,1,2,3,5], 200))
print(tester("/fibonacci/14", [0,1,1,2,3,5,8,13], 200))
print(tester("/fibonacci/89", [0,1,1,2,3,5,8,13,21,34,55,89], 200))
print(tester("/fibonacci/test_3", None , 404))
print(tester("/fibonacci/-1", None , 404))
print(tester("/fibonacci/hello", None, 404))
print(tester("/fibonacci/0.03", None, 404))

#Prime
print("Starting Prime Testing")
print(tester("/is-prime/7", True, 200))
print(tester("/is-prime/21", False, 200))
print(tester("/is-prime/030", False, 200))
print(tester("/is-prime/0.5", None, 404))
print(tester("/is-prime/0", None, 404))
print(tester("/is-prime/-1", None, 404))
print(tester("/is-prime/random", None, 404))

#Slack
print("Starting Slack Testing")
print(tester("/slack-alert/I%20HAVE%20NO%20MOUTH%20AND%20I%20MUST%20SCREAM", True , 200))
print(tester("/slack-alert/suffering", True , 200))
print(tester("/slack-alert/.>'\"/#$%^&*()_+", None , 404))

sys.exit(0)
