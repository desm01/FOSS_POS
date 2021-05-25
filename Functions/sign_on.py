from Objects.alert import alert_messagebox

def check_code_is_correct(self, staff_member, entered_code):
    self.staff_member = staff_member
    self.sign_on_screen.destroy()
    if staff_member.passcode == entered_code:
        self.sign_on = True
        self.current_user = staff_member
        print ("User: " + staff_member.name + " has signed on")
    else:
        alert_messagebox("The passcode you have entered is incorrect")