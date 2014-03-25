module raspi()
{
	piwidth=56;
	pilength=85;
	piheight=1.6;
	mounthole=3;
	
	//the main board with holes
	difference()
	{
		cube([piwidth,pilength,piheight]);
		translate([piwidth-12.5,5,0])
		cylinder(h=piheight,r=mounthole/2);
		translate([18,pilength-25.5,0])
		cylinder(h=piheight,r=mounthole/2);
	}
	
	//the ethernet port
	ewidth=15.4;
	elength=21.8;
	eheight=13;
	translate([2,-1,piheight])
	cube([ewidth,elength,eheight]);
	
	//the usb ports
	uwidth=13.2;
	ulength=17.2;
	uheight=15.3;
	translate([piwidth-18.8-ulength,-7.7,piheight])
	cube([uwidth,ulength,uheight]);
	
	//the audio jack
	awidth=11.4;
	alength=12;
	aheight=10.2;
	adiam=6.7;
	aheight2=3.4;
	translate([piwidth-awidth,14,piheight])
	union()
	{
		translate([awidth,alength/2,adiam/2+3])
		rotate([0,90,0])
		cylinder(h=aheight2,r=adiam/2);
		cube([awidth,alength,aheight]);
	}
	
	//the video jack
	vwidth=10;
	vlength=9.8;
	vheight=13;
	vdiam=8.3;
	vheight2=7;
	translate([piwidth-vwidth-2.1,pilength-40.6-vlength,piheight])
	union()
	{
		translate([vwidth,vlength/2,vdiam/2+4])
		rotate([0,90,0])
		cylinder(h=vheight2,r=vdiam/2);
		cube([vwidth,vlength,vheight]);
	}
	
	//the gpio
	gwidth=5;
	glength=33.2;
	gheight=10;
	translate([piwidth-1.5-gwidth,pilength-1-glength,piheight])
	cube([gwidth,glength,gheight]);
	
	//the hdmi
	hwidth=11.4;
	hlength=15.1;
	hheight=6.15;
	translate([-1.2,pilength-37.5-hlength,piheight])
	cube([hwidth,hlength,hheight]);
	
	//the mini usb
	mwidth=7.6;
	mlength=5.6;
	mheight=2.4;
	translate([3.6,pilength+0.5-mlength,piheight])
	cube([mwidth,mlength,mheight]);
	
	//the sdcard slot
	swidth=27.8;
	slength=19;
	sheight=4.5;
	translate([piwidth-11.5-swidth,pilength-slength,-sheight])
	cube([swidth,slength,sheight]);
}

raspi();