# looks5 (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.add_backdrop('blue_sky_2')
stage.add_backdrop('blue_sky')
stage.create_variable('my variable')
stage.show_builtinvariable("looks_backdropnumbername")
stage.set_monitor_position("looks_backdropnumbername", -235, 148)
stage.show_builtinvariable("looks_size")
stage.set_monitor_position("looks_size", -235, 121)
stage.show_builtinvariable("looks_costumenumbername")
stage.set_monitor_position("looks_costumenumbername", -235, 94)
stage.show_builtinvariable("looks_backdropnumbername")
stage.set_monitor_position("looks_backdropnumbername", -235, 40)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(5)
sprite1.set_y(-121)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_program_starts_1(self):
    self.go_to_front_layer()
    self.wait(1.0)
    self.go_to_back_layer()
    self.wait(1.0)
    self.go_backward(1)
    self.wait(1.0)
    self.go_forward(1)

sprite1.when_program_starts(when_program_starts_1)

stage.play()
