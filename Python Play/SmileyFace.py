import play

head2 = play.new_circle (
  color = 'grey',
  x = -100,
  y = 100,
  radius = 75,
)

eyeleft1 = play.new_circle (
  color = 'blue',
  x = -125,
  y = 125,
  radius = 10,
  border_width = 4,
  border_color = 'black',
)


eyeright1 = play.new_circle (
  color = 'blue',
  x = -75,
  y = 125,
  radius = 10,
)

mouth = play.new_line (
  color = 'red',
  x = -115,
  y = 65,
  length = 30,
  thickness = 5,
  angle = -5
)

head = play.new_circle (
 color = 'gold',
  x = 0,
  y = 0,
  radius = 50,
)

eyeleft = play.new_circle (
  color = "red",
  x = -20,
  y = 15,
  radius = 10
)

eyeleft = play.new_circle (
  color = "red",
  x = 20,
  y = 15,
  radius = 10,
  border_width = 2,
)

mouth = play.new_box (
  color ='red',
  x = 0,
  y = -20,
  width = 20,
  height = 5,
)

nose = play.new_circle(
  color = 'yellow',
  x = 0,
  y = 0,
  radius = 5,

)
play.start_program ()
 