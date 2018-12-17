package com.galenframework.java.sample.tests;

import java.io.IOException;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.interactions.Action;
import org.openqa.selenium.interactions.Actions;
import org.testng.annotations.Test;

import com.galenframework.java.sample.components.TecomBase;


public class WelcomePageTest extends TecomBase
{

  @Test(dataProvider = "devices")
    public void welcomePage_shouldLookGood_onDevice(TestDevice device) throws IOException, InterruptedException
    {
    	load("/");
    		 for (int i=0; i<25; i++)
    		 { 
    			try 
    		    {
   			    Thread.sleep(1000);
  		    }
 			catch (InterruptedException e)
 			{} 			
 		}
    		 
 		 checkLayout("/specs/welcomePage.spec", device.getTags());
    		
    }
  
   @Test(dataProvider = "devices")
   public void slider1_shouldLookGood_onDevice(TestDevice device) throws IOException  {
	
   	load("/");
		 for (int i=0; i<25; i++)
		 { 
		   try 
		   	{
			   Thread.sleep(1000);
			   getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[2]/a[@href='#']")).click();
			
	    }
		catch (InterruptedException e)
	{} 			
	 }
	 
				 
		 checkLayout("/specs/slider1.spec", device.getTags());
   }
   
    @Test(dataProvider = "devices")
    public void slider2_shouldLookGood_onDevice(TestDevice device) throws IOException  {
   	load("/");
		 for (int i=0; i<25; i++)
		 { 
			try 
		    {
			    Thread.sleep(1000);
			    getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[3]/a[@href='#']")).click();
				
		    }
			catch (InterruptedException e)
			{} 			
		 }

		
		 	 
				 
   checkLayout("/specs/slider2.spec", device.getTags());
 }
    
    @Test(dataProvider = "devices")
    public void slider3_shouldLookGood_onDevice(TestDevice device) throws IOException  {
    	
   	load("/");
   			 for (int i=0; i<25; i++)
		 { 
			try 
		    {
			    Thread.sleep(1000);
			    getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[4]/a[@href='#']")).click();
				
		    }
			catch (InterruptedException e)
			{} 			
		 }
	
   				 
				 
     checkLayout("/specs/slider3.spec", device.getTags());
}
    
    @Test(dataProvider = "devices")
  public void slider4_shouldLookGood_onDevice(TestDevice device) throws IOException  {
    	load("/");
   			 for (int i=0; i<25; i++)
    			 { 
  				try 
			    {
    				    Thread.sleep(1000);
    				    getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[5]/a[@href='#']")).click();
    					
			    }
    				catch (InterruptedException e)
    				{} 			
    			 }
    			
    		 
        checkLayout("/specs/slider4.spec", device.getTags());
    }
   
    @Test(dataProvider = "devices")
   public void slider5_shouldLookGood_onDevice(TestDevice device) throws IOException  {
		
   	load("/");
	 for (int i=0; i<25; i++)
		 { 
 			try 
		    {
		     Thread.sleep(1000);
			 getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[6]/a[@href='#']")).click();
		    }
		catch (InterruptedException e)
		{} 			
		}

       checkLayout("/specs/slider5.spec", device.getTags());
   }
   
  @Test(dataProvider = "devices")
  public void slider6_shouldLookGood_onDevice(TestDevice device) throws IOException  {
	   load("/");
		 for (int i=0; i<25; i++)
			 { 
				try 
			    {
					Thread.sleep(1000);
					getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[7]/a[@href='#']")).click();
			    }
			catch (InterruptedException e)
			{} 			
			}
 
      checkLayout("/specs/slider6.spec", device.getTags());
  }
    
  @Test(dataProvider = "devices")
   public void slider7_shouldLookGood_onDevice(TestDevice device) throws IOException  {
	
	   load("/");
		 for (int i=0; i<25; i++)
			 { 
				try 
			    {
			    Thread.sleep(1000);
			    getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[8]/a[@href='#']")).click();
		    }
			catch (InterruptedException e)
			{} 			
			}
			 
       checkLayout("/specs/slider7.spec", device.getTags());
    }
   
	@Test(dataProvider = "devices")
    public void Footer_shouldLookGood_onDevice(TestDevice device) throws IOException  {
		load("/");
		 for (int i=0; i<25; i++)
		 { 
			try 
		    {
			    Thread.sleep(1000);
			    getDriver().findElement(By.xpath("//div[@id='fp-nav']/ul/li[9]/a[@href='#']/span[2]")).click();
				
		    }
			catch (InterruptedException e)
			{} 			
		 }
		
				 
        checkLayout("/specs/footer.spec", device.getTags());
    }
	
}
   

