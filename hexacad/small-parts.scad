module servo_u_holder()
{
	holewidth = 8;
	holeheight = 8;
	partwidth = 20;
	partheight = 26;
	wall = 8;
	
	difference()
	{
		cube([partwidth, partheight, wall]);
		translate([partwidth/2-holewidth/2,0,0])
			cube([holewidth, holeheight, wall]);
	}
}

servo_u_holder();