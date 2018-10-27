import requests, lxml.html
s = requests.session()

#url here
login = s.get('')
login_html = lxml.html.fromstring(login.text)
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')

form = {}
#print hidden_inputs

for x in range(len(hidden_inputs)):
   try:
	name = hidden_inputs[x].attrib["name"]
	form[name]=hidden_inputs[x].attrib["value"]
   except:
	continue

#userid and password
form['userid']=''
form['pass']=''

#print form

#Enter form action url here
response = s.post('', data=form)

print "Chinmohan" in response.text
