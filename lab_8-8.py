#author RED 12/9/22
rows = [["Darick", "Eugene", "Kyle", "Azaan"], ["Ryan",
"Phil", "Eman", "Alex", "Nicholas"],
["Christian", "Josh", "Matt", "Francesco"],
["Patrick", "Nico", "Trevayne"]]

for row in rows:#making loop
    for names in row:#making loop so it prints individua anmes
        if names[-1] == "s":#if the names end in s add '
            names+="'"
        else:
            names+="'s"
        print(names)#print