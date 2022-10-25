counter = 0 
data = open('Contact.txt', 'r')
counter1 = 0
total = 0.0 
for line in data:
    c= float(line.rstrip("\n"))
    print(line)
    #print(float(data.readline()))
    total += float(c)
    
