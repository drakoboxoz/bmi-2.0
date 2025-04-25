import streamlit as s
s.title("bmi calculator")
sex = s.radio("gender",("male","female"), horizontal=True)
w = s.number_input("weight (kg)",min_value=3,max_value=999)
h = s.number_input("height (cm)",min_value=60,max_value=550)
bmi=w/(h/100)**2
if s.button("i shall do math"):
    if sex=="female":
        if bmi<18:
            s.info(f"{bmi}")
            s.info("skinny")
            s.warning("Thou art so frail, that even the essence of anti-matter dost bear greater weight than thyself.")
            s.image("thinveganteacherhorror.png")
        elif bmi<22:
            s.info(f"{bmi}")
            s.info("healthy")
            s.success("Thou art unremarkable, in fine fettle indeed.")
            s.image("jing.png")
        elif bmi<24:
            s.info(f"{bmi}")
            s.info("overweight")
            s.warning("Thou art a trifle portly, partaketh in noble exercises.")
            s.image("kokoro.png")
        elif bmi<29 :
            s.info(f"{bmi}")
            s.info("female caseoh")
            s.error("Thou must shed thine excess weight forthwith; I prithee, embark upon a diet at once!")
            s.image("act.png")
        else:
            s.info(f"{bmi}")
            s.info("extremely fat")
            s.error("Thy life doth reach its fateful close, for the burden thou bearest shall surely bring forth thine demise.")
            s.image("buam.png")
    else:
        if bmi<18.5:
            s.info(f"{bmi}")
            s.info("underweight")
            s.warning("You're so skinny, when you turn sideways, you disappeared.")
            s.image("skinny.png.png")
        elif bmi<23:
            s.info(f"{bmi}")
            s.info("healthy")
            s.success("keep up")
            s.image("normal.png")
        elif bmi<25:
            s.info(f"{bmi}")
            s.info("overweight")
            s.warning("diet please?")
            s.image("chubby walter.png")
        elif bmi<30:
            s.info(f"{bmi}")
            s.info("fat")
            s.error("you make a sumo wrestler look like a supermodel")
            s.image("brainrot have skibidi rizz.png")
        else:
            s.info(f"{bmi}")
            s.info("very fat... infact,u r caseoh reincarnate")
            s.error("You're an absolute gluttonous beast, and the only exercise you get is lifting a fork to your mouth,People mistake you for a planet because of the gravitational pull you have on their food,You're the reason they invented double doors!,You're so fat the only letters of the alphabet you know are KFC.")
            s.image("caseoh.png")
