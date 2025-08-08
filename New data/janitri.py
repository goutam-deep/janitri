// Directory structure:
// src/test/java/
// ├── base/BaseTest.java
// ├── pages/LoginPage.java
// └── tests/LoginTest.java

// 1. BaseTest.java
package base;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;

public class BaseTest {
    protected WebDriver driver;

    @BeforeMethod
    public void setUp() {
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--disable-notifications");
        driver = new ChromeDriver(options);
        driver.manage().window().maximize();
        driver.get("https://dev-dash.janitri.in/");
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}

// 2. LoginPage.java
package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage {
    private WebDriver driver;

    // Locators
    private By userIdField = By.id("email");
    private By passwordField = By.id("password");
    private By loginButton = By.xpath("//button[contains(text(),'Login')]");
    private By eyeIcon = By.cssSelector(".password-toggle svg");
    private By errorMessage = By.cssSelector(".error-message"); // Adjust based on real DOM

    // Constructor
    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }

    // Actions
    public void enterUserId(String userId) {
        driver.findElement(userIdField).sendKeys(userId);
    }

    public void enterPassword(String password) {
        driver.findElement(passwordField).sendKeys(password);
    }

    public void clickLogin() {
        driver.findElement(loginButton).click();
    }

    public boolean isLoginButtonEnabled() {
        return driver.findElement(loginButton).isEnabled();
    }

    public boolean isPasswordMasked() {
        String type = driver.findElement(passwordField).getAttribute("type");
        return type.equals("password");
    }

    public void togglePasswordVisibility() {
        driver.findElement(eyeIcon).click();
    }

    public boolean isErrorMessageDisplayed() {
        return driver.findElements(errorMessage).size() > 0;
    }
}

// 3. LoginTest.java
package tests;

import base.BaseTest;
import org.testng.Assert;
import org.testng.annotations.Test;
import pages.LoginPage;

public class LoginTest extends BaseTest {

    @Test
    public void testLoginButtonDisabledWhenFieldAreEmpty() {
        LoginPage loginPage = new LoginPage(driver);
        Assert.assertFalse(loginPage.isLoginButtonEnabled(), "Login button should be disabled when fields are empty.");
    }

    @Test
    public void testPasswordMaskedbutton() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.enterPassword("test123");
        Assert.assertTrue(loginPage.isPasswordMasked(), "Password should be masked by default.");
        loginPage.togglePasswordVisibility();
        Assert.assertFalse(loginPage.isPasswordMasked(), "Password should be visible after toggling.");
    }

    @Test
    public void testInvalidLoginShowErrorMsg() {
        LoginPage loginPage = new LoginPage(driver);
        loginPage.enterUserId("invalid@email.com");
        loginPage.enterPassword("wrongpassword");
        loginPage.clickLogin();

        // Wait briefly for error to show up (if no explicit wait is used)
        try { Thread.sleep(2000); } catch (InterruptedException e) {}

        Assert.assertTrue(loginPage.isErrorMessageDisplayed(), "Error message should be displayed on invalid login.");
    }
}
