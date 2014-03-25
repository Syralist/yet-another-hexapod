//Robotbase RB-65PG servo

module fitting(fwidth, flength, fheight)
{
	//fitting
	mdiam=4.5;
	difference()
	{
		cube([fwidth,flength,fheight]);
		translate([fwidth/2-mdiam/2-2.5,mdiam/2,0])
		cylinder(h=fheight,r=mdiam/2);
		translate([fwidth/2+mdiam/2+2.5,mdiam/2,0])
		cylinder(h=fheight,r=mdiam/2);
	}
}

module rb65pg()
{
	//main body
	swidth=19.7;
	slength=40.6;
	sheight=39.5;
	cube([swidth,slength,sheight]);
	
	//fitting 1
	fwidth=17;
	flength=7;
	fheight=2;
	translate([(swidth-fwidth)/2,-flength,26])
	fitting(fwidth, flength, fheight);

	//fitting 2
	translate([(swidth-fwidth)/2,slength,26])
	translate([fwidth/2,flength/2,0])
	rotate([0,0,180])
	translate([-fwidth/2,-flength/2,0])
	fitting(fwidth, flength, fheight);
	
	//axis
	adiam=swidth/3;
	translate([swidth/2,slength-1.5*adiam,sheight])
	cylinder(h=adiam,r=adiam/2);
	
}
//$fn=50;
rb65pg();
