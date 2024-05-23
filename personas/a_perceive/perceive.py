def get_perceive(person):
    z1 = person.neartiles
    with open("./personas/a_perceive/perceive_template.txt", "r") as f:
            my_near = f.read()
    count = 0
    for i in range(5):
        for j in range(5):
            if z1[i][j].object != "":
                my_near = my_near.replace(f"!<INPUT {count}>!", z1[i][j].object)
                count = count + 1

    if ", !<" in my_near: 
        my_near = my_near.split(", !<")[0]
    
    my_near = my_near + "\n" + "These things currently exist around me."
    # print(my_near)
    return my_near
