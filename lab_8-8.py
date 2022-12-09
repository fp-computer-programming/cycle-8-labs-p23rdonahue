#author RED 12/9/22
rows = [["Darick", "Eugene", "Kyle", "Azaan"], ["Ryan",
"Phil", "Eman", "Alex", "Nicholas"],
["Christian", "Josh", "Matt", "Francesco"],
["Patrick", "Nico", "Trevayne"]]

for row in rows:
    for names in row:
        if names[-1] == "s":
            names+="'"
        else:
            names+="'s"
        print(names)