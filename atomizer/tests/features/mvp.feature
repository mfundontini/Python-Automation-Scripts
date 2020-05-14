# Created by mfundo at 2020/05/14
Feature: Test if behave is playing nicely with other kids

  Scenario: Check if everything runs
     Given we have behave "installed"
      When we implement test number "9"
      Then behave will test it for us!

  Scenario: Test pattern matching
   Given we have behave "installed"
    When we implement test number "x"
    Then behave will test it for us!

  Scenario: Test switching parsers
   Given we have behave "installed"
    When we run test number "6"
    Then behave will test it for us!