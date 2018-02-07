import Quandl

# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt','r').read()

df = Quandl.get("FMAC/HPI_TX", authtoken=api_key)

print(df.head())
print("_________________________________________________________")
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states)
print("_________________________________________________________")
print(fiddy_states[0])
print("_________________________________________________________")
for abbv in fiddy_states[0][0][1:]:
    print(abbv)
print("_________________________________________________________")
for abbv in fiddy_states[0][0][1:]:
    #print(abbv)
    print("FMAC/HPI_"+str(abbv))
print("_________________________________________________________")

