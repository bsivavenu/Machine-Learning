class CompoundButton:
    def cbfun(self):
        print("This Button Will Behave in 2 states")
        print("i.e On and Off  or Checked and Unchecked")


class CheckBox(CompoundButton):
    pass

class RadioButton(CompoundButton):
    pass

class Switch(CompoundButton):
    pass

class ToggleButton(CompoundButton):
    pass

#-------------------------------


s1 = CheckBox()
s1.cbfun()







