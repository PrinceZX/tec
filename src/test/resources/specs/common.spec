@objects
	header				  css       .wrap-top
	header-list-p-*		  css       .wrap-top .container a
	header-img-*		  css		.wrap-top .container a img
	logo-*			 	  css       .wrap-bottom .container a
	menu-item-*			  css		.wrap-bottom .container .primary .cta-primary 
	search		          css 		.ico-search
	menubtn				  css		[type='button']
		
= Header =
    @on desktop
     header:
            			inside screen 0px top
            			centered horizontally inside screen 1px
            			height 60px
 
= Header item =
	@on desktop
	 header-list-p-1:
						height ~ 34px
						width 251px
						text is "Explore Our Communities"
						near header-img-1 428px left
    					
	 header-img-1:  
						height ~ 22px
						width 12px
						near header-img-3 50px left
						
	 header-img-3:  
						height ~ 13px
						width 39px	
						near header-list-p-4 40px left  					
	
	 header-list-p-4:  
						height ~ 16px
						width 62px
						near header-list-p-5 40px left
						text is "Directory"
						
     header-list-p-5:  
						height ~ 34px
						width 198px		
						text is "Set up your Business"

= Menu =
	@on desktop
  	 logo-1:
          				below header-list-p-1 10 to 43px
	
	@on mobile, tablet
	 logo-1:
          				height 43px
          				width 80px
 
= Menu Items =	
	@on desktop 
	 menu-item-1:
          				height ~ 16px
          				width 65px
          				css font-size is "14px"
          				text is "Discover"
          				near menu-item-2 ~ 40px left
         
     menu-item-2:
          				height ~ 16px
          				width 76px
          				css font-size is "14px"
          				text is "Our Spaces"
          				near  menu-item-3 ~ 40px left
          
     menu-item-3:
          				height ~ 16px
          				width 106px
          				css font-size is "14px"
          				text is "The Community"
          				near menu-item-4 ~ 40px left
    				           				
     menu-item-4:
          				height ~ 16px
          				width 49px
          				css font-size is "14px"
          				text is "Venues"
          				near menu-item-5 ~ 40px left
    				         
     menu-item-5:
          				height ~ 16px
          				width 41px
          				css font-size is "14px"
          				text is "Media"
          				near menu-item-6 ~ 40px left
    				
     menu-item-6:
          				height ~ 16px
          				width 56px
          				css font-size is "14px"
          				text is "Connect"
          				          				         			
= Search btn =    
    @on all 
     search:		    
     					height ~ 25px
	 					width 25px
	 					
= Menu btn = 	 					
	@on all					
	 menubtn:	        
	 					height ~ 11px
	 					width 25px	
	 							
	 
	