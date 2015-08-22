from ik.gait import leg_ik
from ik.tf import tf

conf = leg_ik.Configuration()
conf.coxa_min_deg = -40.0
conf.coxa_idle_deg = 0.0
conf.coxa_max_deg = 40.0
conf.coxa_length_mm = 65.0
conf.coxa_sign = 1
conf.coxa_ident = 0

conf.femur_min_deg = -40.0
conf.femur_idle_deg = 0.0
conf.femur_max_deg = 40.0
conf.femur_length_mm = 87.0
conf.femur_sign = 1
conf.femur_ident = 0

conf.tibia_min_deg = -40.0
conf.tibia_idle_deg = 0.0
conf.tibia_max_deg = 40.0
conf.tibia_length_mm = 95.0
conf.tibia_sign = 1
conf.tibia_ident = 0

Hexa = leg_ik.LizardIk(conf)

InitialPos = tf.Point3D(-200, 0, -90)

print Hexa.do_ik(InitialPos)
