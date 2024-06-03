# delete_from_list (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
stage.create_list_variable("delete_list_plz", ['thing2'])
stage.show_list("delete_list_plz", -235, 175)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(0)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_program_starts_1(self):
    self.add_value_to_list("delete_list_plz", "thing")
    self.add_value_to_list("delete_list_plz", "thing2")
    self.wait(1.0)
    self.delete_value_from_list("delete_list_plz", 1)

sprite1.when_program_starts(when_program_starts_1)
stage.play()
