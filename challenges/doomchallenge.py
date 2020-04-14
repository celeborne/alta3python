#!/usr/bin/python3

super_powers = {"all": [{"First":"Askia","Last":"Wingfield","Skill Level":"astonishing","Spirit Animal":"lion","Super Power":"Regenerative Healing Factor"},{"First":"Chen","Last":"Xin","Skill Level":"awe-inspiring","Spirit Animal":"porcupine","Super Power":"Adoptive Muscle Memory"},{"First":"Everett","Last":"Strunk","Skill Level":"breathtaking","Spirit Animal":"mandrill","Super Power":"Body Part Substitution"},{"First":"Jacob","Last":"Roe","Skill Level":"fearsome","Spirit Animal":"guinea pig","Super Power":"Anatomical Liberation"},{"First":"Josh","Last":"Ayala","Skill Level":"formidable","Spirit Animal":"camel","Super Power":"Additional Limbs"},{"First":"Kevin","Last":"Martinez","Skill Level":"imposing","Spirit Animal":"panther","Super Power":"Organic Constructs"},{"First":"Luke","Last":"Thompson","Skill Level":"impressive","Spirit Animal":"coati","Super Power":"Deflection"},{"First":"Marco","Last":"Santos","Skill Level":"magnificent","Spirit Animal":"bumblebee","Super Power":"Replication"},{"First":"Michael","Last":"Williams","Skill Level":"overwhelming","Spirit Animal":"fish","Super Power":"Invisibility"},{"First":"Mike","Last":"Wright","Skill Level":"stunning","Spirit Animal":"mink","Super Power":"Needle Projection"},{"First":"Oscar","Last":"Abalos","Skill Level":"wondrous","Spirit Animal":"ermine","Super Power":"Immobility"},{"First":"Ryan","Last":"Larson","Skill Level":"grand","Spirit Animal":"marmoset","Super Power":"Camouflage"},{"First":"Shirley","Last":"Wu","Skill Level":"mind-blowing","Spirit Animal":"koala","Super Power":"Self-Detonation"}]}

def superpowers():
    # errors I found: placement of the { }
    # trying to return two different values in one command (first and last name)
    print(f"My name is {super_powers['all'][6]['First']} {super_powers['all'][6]['Last']} and my spirit animal is {super_powers['all'][6]['Spirit Animal']}.")
    print(f"My name is {super_powers['all'][6]['First']} {super_powers['all'][6]['Last']} and my skills are {super_powers['all'][6]['Skill Level']} {super_powers['all'][6]['Super Power']}.")
for i in super_powers["all"]:
    print(f"""
    Name: {i['First']} {i['Last']}
    Skill Level: {i['Skill Level']}
    Spirit Animal: {i['Spirit Animal']}
    Super Power: {i['Super Power']}
    """)
    print("* * * * * * * * * * * * * * * *")
superpowers()
