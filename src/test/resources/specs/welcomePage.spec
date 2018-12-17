@import common.spec
@import slider.spec

@objects 	
    build		   css  	 [data-swiper-slide-index='0']:nth-of-type(2) .field-title p:nth-of-type(1)
    tomo		   css       [data-swiper-slide-index='0']:nth-of-type(2) .field-title p:nth-of-type(2)
    dotslide-*	   css		 [data-fp-styles='null']:nth-of-type(1) .swiper-pagination-bullets span
   	arrow-next     xpath     //div[@class='swiper-controller']/div[2]
   	arrow-prev     xpath     //div[@class='swiper-controller']/div[1]
   
= Content =
    @on desktop
		build:
            inside screen ~175px top 
			height ~175px
			width 570px
	
		tomo:
			height ~175px
			width 1200px
= Arrow =
	@on desktop
		arrow-next:
			height 10px
			width 19px
			near screen 80px left 
			
		arrow-prev:
			height 10px
			width 19px
			left-of arrow-next 70px
			
= contents items =						
	@on mobile,tablet
	 	build:
	 		width 296px
	 		height 121px
	 	
	 	tomo:
	 		width 300px
	 		height 121px	 	
	 	
	 	dotslide-1:
	 		height 8px
	 		width 8px
	 		aligned horizontally all dotslide-2
	 		left-of dotslide-2 15px
	 		
	 	dotslide-2:
	 		height 8px
	 		width 8px
	 		aligned horizontally all dotslide-3
	 		left-of dotslide-3 15px
	 		
	 	dotslide-3:
	 		height 8px
	 		width 8px
	 		aligned horizontally all dotslide-4
	 		left-of dotslide-4 15px
	 		
	 	dotslide-4:
	 		height 8px
	 		width 8px
	 		aligned horizontally all dotslide-5
	 		left-of dotslide-5 15px		
	 	
	 	dotslide-5:
	 		height 8px
	 		width 8px
	 		aligned horizontally all dotslide-1
	 			 		

			
		
