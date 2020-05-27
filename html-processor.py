import re
#Λεξικό
dictionary = {'&amp;':'&','&gt;':'>','&lt;':'<','&nbsp;':' '}

#Callback Συνάρτηση
def callback(m):
    group = m.group(1)
    if(group == '&amp;'):
        return dictionary[group]
    if(group == '&gt;'):
        return dictionary[group]
    if(group == '&lt;'):
        return dictionary[group]
    if(group == '&nbsp;'):
        return dictionary[group]

#Μηχανές ταιριάσματος:
#Για τον τίτλο
rexpTitle = re.compile('<title>(.+?)</title>')
#Για τους υπερσυνδέσμους
rexpHref = re.compile('<a(.+?)</a>')
#Για τα scripts και styles
rexp = re.compile('(<script.+?</script>)|(<style.+?</style>)|(<!--.+?-->)',re.DOTALL)
#Για τα tags
rexp2 = re.compile('<[^>]+>')
#Για τους ειδικούς χαρακτήρες
rexp3 = re.compile(r'(&amp|&gt;|&lt;|&nbsp;)')
#Για το whiteboard
rexp4 = re.compile(r'\s+')

#Άνοιγμα αρχείου για ανάγνωση
with open('testpage.txt','r', encoding = 'utf-8') as fp:
    #Ανάθεση κειμένου στην μεταβλητή text
    text = fp.read()
    #Έυρεση περιεχομένου τίτλου
    title = rexpTitle.search(text)
    print(title.group(1))
    #Έυρεση περιεχομένου υπερσυνδέσμων
    for l in rexpHref.finditer(text):
	    print(l.group(1))
    #Απαλοιφή scripts, styles
    newtext = rexp.sub('',text)
    #Απαλοιφή tags
    newtext = rexp2.sub('',newtext)
    #Απαλοιφή ειδικών χαρακτήρων
    newtext = rexp3.sub(callback,newtext)
    #Αντικατάσταση πολλαπλών κενών με ένα κενό
    newtext = rexp4.sub(' ',newtext)
    #Εκτύπωση τελικού κειμένου
    print(newtext)
