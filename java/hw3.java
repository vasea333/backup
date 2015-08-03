package com.auto.wdb_tests;

import com.thoughtworks.selenium.Selenium;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebDriverBackedSelenium;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;
import java.util.regex.Pattern;
import static org.apache.commons.lang3.StringUtils.join;

public class hw3 {
	private Selenium selenium;

	@Before
	public void setUp() throws Exception {
		WebDriver driver = new FirefoxDriver();
		String baseUrl = "http://hrm.tehportal.net/";
		selenium = new WebDriverBackedSelenium(driver, baseUrl);
	}

	@Test
	public void testHw3() throws Exception {
		selenium.open("/symfony/web/index.php/auth/login");
		assertEquals("OrangeHRM", selenium.getTitle());
		selenium.type("id=txtUsername", "admin");
		selenium.type("id=txtPassword", "Password");
		selenium.click("id=btnLogin");
		selenium.waitForPageToLoad("45000");
		selenium.click("//a[@id='menu_leave_viewLeaveModule']/b");
		selenium.waitForPageToLoad("45000");
		selenium.click("id=menu_leave_assignLeave");
		selenium.waitForPageToLoad("45000");
		selenium.type("id=assignleave_txtEmployee_empName", "");
		selenium.sendKeys("id=assignleave_txtEmployee_empName", "All");
		for (int second = 0;; second++) {
			if (second >= 60) fail("timeout");
			try { if (selenium.isVisible("css=div.ac_results")) break; } catch (Exception e) {}
			Thread.sleep(1000);
		}

		assertTrue(selenium.getText("//div[6]/ul/li").matches("^regexpi:\\.[\\s\\S]*All\\.[\\s\\S]*$"));
		String name = selenium.getText("//div[6]/ul/li");
		selenium.click("//div[6]/ul/li");
		assertEquals(name, selenium.getValue("id=assignleave_txtEmployee_empName"));
		selenium.click("id=welcome");
		selenium.click("link=Logout");
		selenium.waitForPageToLoad("45000");
	}

	@After
	public void tearDown() throws Exception {
		selenium.stop();
	}
}
