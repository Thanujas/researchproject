import sqlite3
import json
import re
class database():

 conn = sqlite3.connect('rasa.db')
 print("Opened database successfully")
 cursor = conn.cursor()


 # Display columns
print('\nColumns in events table:')
data = database.cursor.execute('''SELECT * FROM  events''')
for column in data.description:
 print(column[0])

print('\nEntire Quiery :')
text1 = database.cursor.execute('''SELECT data FROM events where data like "%I am going to%" order by timestamp desc limit 1''')
for row in text1:
 str = ''.join(row)
details_dict = json.loads(str)
# print(row)
print(details_dict.get('text'))
s = details_dict.get('text')

start = 'Field_names as:'
end = 'and Field_Xpaths as:'
print("*** field names are ***")
fieldnames = s[s.find(start) + len(start):s.rfind(end)]
print(fieldnames)

startXpaths = 'Field_Xpaths as:'
endXpaths = 'and Fields_Max_Size as:'
print("*** field xpaths are ***")
fieldxpaths = s[s.find(startXpaths) + len(startXpaths):s.rfind(endXpaths)]
print(fieldxpaths)

startMax_Size = 'Fields_Max_Size as:'
endMax_Size = 'and Fields_Min_size as:'
print("*** field max sizes are ***")
fieldMax_Size = s[s.find(startMax_Size) + len(startMax_Size):s.rfind(endMax_Size)]
print(fieldMax_Size)

startMin_Size = 'Fields_Min_size as:'
endMin_Size = 'and Fields_Allowable_datatypes as:'
print("*** field min sizes are ***")
fieldMin_Size = s[s.find(startMin_Size) + len(startMin_Size):s.rfind(endMin_Size)]
print(fieldMin_Size)

startAllowable_datatypes = 'Fields_Allowable_datatypes as:'
endAllowable_datatypes = 'and Fields-Non-Allowable_datatypes as:'
print("*** field Allowable data types ***")
fieldAllowable_datatypes = s[s.find(startAllowable_datatypes) + len(startAllowable_datatypes):s.rfind(
endAllowable_datatypes)]
print(fieldAllowable_datatypes)

startNonAllowable_datatypes = 'Fields-Non-Allowable_datatypes as:'
endNonAllowable_datatypes = 'finaly Fields-otherconcerns as:'
print("*** field Non Allowable data types ***")
fieldNonAllowable_datatypes = s[s.find(startNonAllowable_datatypes) + len(startNonAllowable_datatypes):s.rfind(
endNonAllowable_datatypes)]
print(fieldNonAllowable_datatypes)

startother = 'finaly Fields-otherconcerns as:'
endother = ''
print("*** field other concerns are ***")
fieldother = s[s.find(startother) + len(startother):s.rfind(endother)]
print(fieldother)

database.conn.commit()



def _json_writing ():
    # Data to be written
 dictionary = {
        "fieldnamesfinal":fieldnames,
        "fieldxpathsfinal": fieldxpaths,
        "fieldMax_Sizefinal": fieldMax_Size,
        "fieldMin_Sizefinal": fieldMin_Size,
        "fieldAllowable_datatypesfinal": fieldAllowable_datatypes,
        "fieldNonAllowable_datatypesfinal": fieldNonAllowable_datatypes,
        "fieldotherfinal": fieldother,

    }

    # Serializing json
 json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
 with open("sample.json", "w") as outfile:
   outfile.write(json_object)
   print("#data successfully writte#")

_json_writing ()

data = database.cursor.execute('''DELETE FROM events''')
print("all data deleted")
text2 = database.cursor.execute('''SELECT data FROM events where data like "%I am going to%" order by timestamp desc limit 1''')
for row in text2:
    print("after delete")
    print(text2)