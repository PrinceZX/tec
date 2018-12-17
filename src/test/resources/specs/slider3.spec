@objects
	s3titleh2        css    .comp-mixed-grid .comp-heading .component-content h2
	s3titlep		 css	.comp-mixed-grid .comp-heading .component-content p
	filterspan-*	 css    .filter span
	ann			     css	.first-card .inner .content-left span
	celebrate	     css	.first-card .inner .content-left h3
	celediv		     css	.first-card .inner .content-left div
	date-*		     css	.first-card .inner .content-right .date-text p
	dic				 css	.content-right .business-park
	allann			 css	[title='View All Announcement']
		
= Slider 3 =	
	@on desktop
		s3titleh2:
                height 141px
                width 250px
                aligned vertically left s3titlep
                above s3titlep 0 to ~20px
		 
		s3titlep:   
				height 44px
                width 266px
                aligned vertically left s2titleh2-3
        		near filterspan 30px top, 144px left
 
= Filter Radio Btn =      
	@on desktop 	 
        filterspan-1:   
				height 22px
                width 85px
                
        filterspan-2:   
				height 22px
                width 76px
              
        filterspan-3:   
				height 22px
                width 171px
                
= Announcement =
	@on desktop
		ann:
				height 16px
				width 96px
				
		celebrate:
				height 	36px
				width 200px
				
		celediv:
				height 36px
				width 400px		
				
= Date Box =
	@on desktop
		date-1:
				height 26px
				width 54px
				
		date-2:
				height 26px
				width 54px
				
= dic Titlebox =
	@on desktop
		dic:
				height 21px
				width 108px		
				
= All Announcement =
	@on desktop
		allann:
				width 200px
				height 22px

		