# broadcast_and_wait (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable', 0)
stage.show_builtinvariable("timer", -235, 175)

def when_i_receive_1(self):
    self.wait_seconds(3.0)

stage.when_i_receive("message1", when_i_receive_1)
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(150)
sprite1.set_y(0)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.point_in_direction(-15)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)
sprite1.add_sound('meow')

def when_i_receive_message_2(self):
    self.say_for_seconds("Sprite received message", 2.0)
    self.turn_right(15.0)

sprite1.when_i_receive_message("message1", when_i_receive_message_2)

def when_program_starts_3(self):
    self.broadcast_and_wait("message1")
    self.say_for_seconds("broadcast was done", 2.0)

sprite1.when_program_starts(when_program_starts_3)
stage.play()
